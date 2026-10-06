"""EXP-001 custody and predeclared numerical checks; no listening verdict."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import numpy as np

MAX_ERROR = 1e-6
RMS_ERROR = 2e-7
STATE_LIMIT = 1.25001
# Discrete trace equality is exact; doubles are checked at 1e-12 seconds/weights.
TRACE_TOLERANCE = 1e-12
FLOAT_TRACE_FIELDS = {
    'desired_delay', 'read_old', 'read_new', 'timing_alpha',
    'timing_destination', 'timing_pending_delay', 'committed_delay', 'route_weight',
}
TRACE_FIELDS = FLOAT_TRACE_FIELDS | {
    'sample', 'reason', 'desired_style', 'timing_active', 'timing_destination_style',
    'timing_pending', 'timing_pending_style', 'committed_style', 'route_active',
    'route_destination', 'route_pending', 'route_pending_mode', 'committed_route',
    'tempo_available',
}

def rows(path):
    with Path(path).open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))

def check_trace(candidate, reference):
    errors = []
    def indexed(path, label):
        indexed_rows = {}
        for row in rows(path):
            missing = TRACE_FIELDS-set(row)
            if missing:
                errors.append(f'{label}: missing fields {sorted(missing)}')
            try:
                sample = int(row['sample'])
            except (KeyError, TypeError, ValueError):
                errors.append(f'{label}: invalid sample index')
                continue
            if sample in indexed_rows:
                errors.append(f'{label}: duplicate sample {sample}')
            indexed_rows[sample] = row
        if not indexed_rows:
            errors.append(f'{label}: empty audit trace')
        return indexed_rows
    actual = indexed(candidate, 'candidate')
    expected = indexed(reference, 'reference')
    for sample, want in expected.items():
        got = actual.get(sample)
        if got is None:
            errors.append(f'missing audit sample {sample}')
            continue
        for field, value in want.items():
            if field in ('sample', 'reason'):
                continue
            if field in FLOAT_TRACE_FIELDS:
                try:
                    a, b = float(got[field]), float(value)
                except (KeyError, TypeError, ValueError):
                    errors.append(f'{sample}:{field}: missing/invalid value')
                    continue
                if not math.isfinite(a) or not math.isfinite(b) or abs(a-b) > TRACE_TOLERANCE:
                    errors.append(f'{sample}:{field}:{got[field]} != {value}')
            elif got.get(field) != value:
                errors.append(f'{sample}:{field}:{got.get(field)} != {value}')
    return errors

def static_checks(row, output):
    if row['schedule'] != 'static':
        return []
    vectors = {
        'impulse_center': (.125, .125), 'impulse_left': (.125, 0),
        'impulse_right': (0, .125), 'impulse_stereo': (.125, -.0625),
        'impulse_antiphase': (.125, -.125),
    }
    injection = np.array(vectors[row['source']], dtype=np.float64)
    if row['mode'] == 'pingpong':
        injection = np.array([np.mean(injection), 0.0])
    g, c = float(row['feedback']), float(row['char_gain'])
    delay = int(.25*int(row['rate']))
    errors = []
    nonzero = np.flatnonzero(np.any(output != 0, axis=1))
    if np.any(injection):
        if not len(nonzero) or int(nonzero[0]) != delay:
            errors.append('first integer arrival')
    elif len(nonzero):
        errors.append('cancelled input has wet output')
    for echo in range(1, 4):
        expect = injection*(g*c)**(echo-1)*(1.0 if row['tap'] == 'pre' else c)
        if row['mode'] == 'pingpong' and echo % 2 == 0:
            expect = expect[::-1]
        if np.max(np.abs(output[echo*delay]-expect)) > MAX_ERROR:
            errors.append(f'echo{echo} amplitude/channel')
    return errors

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while block := stream.read(4*1024*1024):
            h.update(block)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('manifest')
    parser.add_argument('candidate')
    parser.add_argument('reference')
    parser.add_argument('report')
    parser.add_argument('--negative', action='store_true')
    args = parser.parse_args()
    configs = rows(args.manifest)
    candidate_dir, reference_dir = Path(args.candidate), Path(args.reference)
    destination = Path(args.report)
    if destination.exists() and any(destination.iterdir()):
        raise RuntimeError('Refusing nonempty report directory; retain prior attempt.')
    destination.mkdir(parents=True, exist_ok=True)
    actual_metrics = {r['id']: r for r in rows(candidate_dir/'metrics.csv')}
    ref_metrics = {r['id']: r for r in rows(reference_dir/'metrics.csv')}
    observations, custody, partition_base = [], [], {}
    for config in configs:
        run_id, frames = config['id'], 20*int(config['rate'])
        actual_path, ref_path = candidate_dir/(run_id+'.f32'), reference_dir/(run_id+'.f64')
        if actual_path.stat().st_size != frames*8 or ref_path.stat().st_size != frames*16:
            raise RuntimeError(f'wrong raw size: {run_id}')
        actual = np.fromfile(actual_path, dtype='<f4').reshape(frames, 2)
        reference = np.fromfile(ref_path, dtype='<f8').reshape(frames, 2)
        finite = bool(np.isfinite(actual).all() and np.isfinite(reference).all())
        delta = actual.astype(np.float64)-reference
        peak = float(np.max(np.abs(delta)))
        rms = float(np.sqrt(np.mean(delta*delta)))
        trace_errors = check_trace(candidate_dir/(run_id+'.trace.csv'), reference_dir/(run_id+'.trace.csv'))
        impulse_errors = static_checks(config, actual)
        metric = actual_metrics[run_id]
        state = float(metric['state_peak'])
        metrics_ok = (metric['finite'] == '1' and ref_metrics[run_id]['finite'] == '1'
                      and int(metric['frames']) == frames
                      and state <= STATE_LIMIT
                      and float(ref_metrics[run_id]['state_peak']) <= STATE_LIMIT)
        partition_error = 0.0
        partition_rms = 0.0
        key = tuple((k, v) for k, v in config.items() if k not in ('id', 'panel', 'partition'))
        if key in partition_base:
            baseline = np.fromfile(partition_base[key], dtype='<f4').reshape(frames, 2)
            partition_delta = actual.astype(np.float64)-baseline
            partition_error = float(np.max(np.abs(partition_delta)))
            partition_rms = float(np.sqrt(np.mean(partition_delta*partition_delta)))
        else:
            partition_base[key] = actual_path
        fidelity = finite and metrics_ok and peak <= MAX_ERROR and rms <= RMS_ERROR
        passed = (fidelity and not trace_errors and not impulse_errors
                  and partition_error <= MAX_ERROR and partition_rms <= RMS_ERROR)
        negative_detected = not fidelity or bool(trace_errors) or bool(impulse_errors)
        accepted = negative_detected if args.negative else passed
        observations.append({
            **config, 'max_error': peak, 'rms_error': rms, 'finite': finite,
            'state_peak': state, 'partition_max_error': partition_error,
            'partition_rms_error': partition_rms,
            'trace_error_count': len(trace_errors), 'static_error_count': len(impulse_errors),
            'accepted': accepted, 'negative_detected': negative_detected if args.negative else None,
            'trace_errors': trace_errors[:30], 'static_errors': impulse_errors,
            'left_energy': float(metric['left_energy']), 'right_energy': float(metric['right_energy']),
            'fold_energy': float(metric['fold_energy']), 'output_peak': float(metric['output_peak']),
        })
        for raw in (actual_path, ref_path, candidate_dir/(run_id+'.trace.csv'), reference_dir/(run_id+'.trace.csv')):
            custody.append({'path': str(raw.resolve()), 'bytes': raw.stat().st_size, 'sha256': digest(raw)})
        print(f'{len(observations)}/{len(configs)} {run_id}: {"PASS" if accepted else "FAIL"} max={peak:.3g} rms={rms:.3g}', flush=True)
        # An unexpected primary disagreement stops affected execution; preserve evidence.
        if not accepted:
            break
    summary = {
        'planned': len(configs), 'checked': len(observations),
        'all_pass': len(observations) == len(configs) and all(o['accepted'] for o in observations),
        'negative_mode': args.negative, 'max_error_limit': MAX_ERROR,
        'rms_error_limit': RMS_ERROR, 'state_limit': STATE_LIMIT,
        'trace_tolerance': TRACE_TOLERANCE,
        'maximum_observed_error': max(o['max_error'] for o in observations),
        'maximum_observed_rms': max(o['rms_error'] for o in observations),
        'maximum_stored_state': max(o['state_peak'] for o in observations),
        'observations': observations,
    }
    (destination/'summary.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    (destination/'custody.json').write_text(json.dumps(custody, indent=2)+'\n', encoding='utf-8')
    raise SystemExit(0 if summary['all_pass'] else 2)

if __name__ == '__main__':
    main()
