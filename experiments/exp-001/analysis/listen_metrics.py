"""Fixed-gain, opaque listening package and descriptive read-motion diagnostics."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import random
import wave
import numpy as np
from compare import digest, rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('manifest')
    parser.add_argument('candidate')
    parser.add_argument('reference')
    parser.add_argument('comparison')
    parser.add_argument('destination')
    args = parser.parse_args()
    checked = json.loads(Path(args.comparison).read_text(encoding='utf-8'))
    if not checked['all_pass'] or checked['checked'] != 204:
        raise RuntimeError('Require complete numerical PASS before listening package')
    destination = Path(args.destination)
    if destination.exists():
        raise RuntimeError('Refusing to overwrite listening package')
    destination.mkdir(parents=True)
    configs = rows(args.manifest)
    groups = {}
    # All P2/P3/P4/P10 edges/listening rows, plus each rate's irregular P9 diagnostic.
    # Duplicate stress/partition and gain rows remain in numerical evidence.
    for row in configs:
        if row['panel'] in ('P2', 'P3', 'P4', 'P10') or (
                row['panel'] == 'P9' and row['partition'] == 'irregular'):
            key = (row['panel'], row['source'], row['schedule'], row['mode'], row['rate'])
            groups.setdefault(key, []).append(row)
    rng = random.Random(20261005)
    reveal, clips, descriptors = [], [], []
    index = ['# EXP-001 blind listening package', '',
             'Owner listening: PENDING. PCM16 stereo, fixed0dB gain/no normalization.',
             'Each group shares a source/schedule/route/rate; labels A/B/C are shuffled',
             'opaque alternatives. Single-choice groups are diagnostics only.',
             'Do not open reveal.json until recording impressions. Start with retarget',
             'sine and pluck groups; compare both excerpt lengths if useful.', '']
    for group_number, (key, members) in enumerate(groups.items(), 1):
        rng.shuffle(members)
        group = f'group-{group_number:02d}'
        index.extend([f'## {group}: {key[1]}, {key[2]}, {key[3]}, {key[4]}Hz', ''])
        for alternative, row in enumerate(members):
            label = 'ABC'[alternative]
            rate = int(row['rate'])
            path = Path(args.candidate)/(row['id']+'.f32')
            audio = np.fromfile(path, dtype='<f4').reshape(-1, 2)
            window = audio[round(.95*rate):round(1.75*rate)].astype(np.float64)
            descriptors.append({'id': row['id'], 'window_seconds': [.95, 1.75],
                                'peak': float(np.max(np.abs(window))),
                                'rms': float(np.sqrt(np.mean(window*window))),
                                'maximum_adjacent_sample_change': float(np.max(np.abs(np.diff(window, axis=0))))})
            for endpoint, suffix in ((1.2, 'short'), (1.75, 'long')):
                excerpt = audio[round(.95*rate):round(endpoint*rate)]
                if not np.isfinite(excerpt).all() or np.max(np.abs(excerpt)) >= 1:
                    raise RuntimeError('Clipping/nonfinite clip; no silent normalization')
                encoded = np.rint(excerpt.astype(np.float64)*32767).astype('<i2')
                filename = f'{group}-{label}-{suffix}.wav'
                wavpath = destination/filename
                with wave.open(str(wavpath), 'wb') as out:
                    out.setnchannels(2)
                    out.setsampwidth(2)
                    out.setframerate(rate)
                    out.writeframes(encoded.tobytes())
                clips.append({'file': filename, 'frames': len(excerpt), 'rate': rate,
                              'gain_db': 0, 'normalization_db': 0,
                              'sha256': digest(wavpath), 'bytes': wavpath.stat().st_size})
                reveal.append({'file': filename, 'id': row['id'], 'style': row['style']})
                index.append(f'- [{label} {suffix}]({filename})')
        index.append('')
    motion = []
    for row in configs:
        if row['panel'] != 'P9' or row['partition'] != 'irregular':
            continue
        rate = int(row['rate'])
        audio = np.fromfile(Path(args.candidate)/(row['id']+'.f32'), dtype='<f4').reshape(-1, 2)[:, 0]
        reference = np.fromfile(Path(args.reference)/(row['id']+'.f64'), dtype='<f8').reshape(-1, 2)[:, 0]
        start, end = round(1.05*rate), round(1.45*rate)
        segment = audio[start:end].astype(np.float64)
        frequencies = np.fft.rfftfreq(len(segment), 1/rate)
        magnitude = np.abs(np.fft.rfft(segment))
        dominant = float(frequencies[np.argmax(magnitude)])
        # Fixed950Hz least-squares fits in nonoverlapping20ms (19-cycle) windows.
        phases, ref_phases, times = [], [], []
        width = round(.020*rate)
        for first in range(start, end-width+1, width):
            t = np.arange(first, first+width, dtype=np.float64)/rate
            basis = np.column_stack((np.sin(2*np.pi*950*t), np.cos(2*np.pi*950*t)))
            a, b = np.linalg.lstsq(basis, audio[first:first+width], rcond=None)[0]
            ra, rb = np.linalg.lstsq(basis, reference[first:first+width], rcond=None)[0]
            phases.append(np.arctan2(b, a)); ref_phases.append(np.arctan2(rb, ra))
            times.append(float(np.mean(t)))
        phase = np.unwrap(phases); rp = np.unwrap(ref_phases)
        fit_frequencies = 950+np.diff(phase)/(2*np.pi*np.diff(times))
        motion.append({'id': row['id'], 'ideal_frequency_hz': 950,
                       'fft_window_seconds': [1.05, 1.45], 'fft_bin_width_hz': rate/len(segment),
                       'dominant_fft_bin_hz': dominant,
                       'phase_fit_window_seconds': .020,
                       'phase_fit_frequency_min_hz': float(np.min(fit_frequencies)),
                       'phase_fit_frequency_max_hz': float(np.max(fit_frequencies)),
                       'maximum_candidate_reference_fitted_phase_difference_rad': float(np.max(np.abs(phase-rp))),
                       'fitted_phase_times_seconds': times, 'fitted_phase_rad': phase.tolist(),
                       'interpretation': 'Descriptive sampled motion, no production frequency threshold or listening verdict.'})
    (destination/'LISTEN.md').write_text('\n'.join(index)+'\n', encoding='utf-8')
    (destination/'reveal.json').write_text(json.dumps({'shuffle_seed': 20261005, 'mapping': reveal}, indent=2)+'\n', encoding='utf-8')
    (destination/'clips.json').write_text(json.dumps(clips, indent=2)+'\n', encoding='utf-8')
    (destination/'diagnostics.json').write_text(json.dumps({'transients': descriptors, 'motion': motion}, indent=2)+'\n', encoding='utf-8')
    print(f'{len(groups)} groups, {len(clips)} clips; gain0dB; owner listening PENDING')

if __name__ == '__main__':
    main()
