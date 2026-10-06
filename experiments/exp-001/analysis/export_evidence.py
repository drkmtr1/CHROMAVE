"""Portable retained summaries and checksum inventory; excludes binary/audio data."""
import json
from pathlib import Path
import shutil
from compare import digest

root = Path.cwd()
attempt = Path('artifacts/exp-001/attempt-001')
destination = Path('records/evidence/exp-001')
exports = {
    attempt/'comparison-primary/summary.json': 'primary-summary.json',
    attempt/'comparison-negative/summary.json': 'negative-summary.json',
    attempt/'listening/diagnostics.json': 'diagnostics.json',
    attempt/'listening/clips.json': 'listening-clips.json',
    attempt/'listening/reveal.json': 'listening-reveal.json',
    Path('artifacts/exp-001/verifier-probes/result.json'): 'verifier-probes.json',
}
for source, name in exports.items():
    target = destination/name
    if target.exists():
        raise RuntimeError(f'Refusing export overwrite {target}')
    shutil.copyfile(source, target)
custody = []
for report in ('comparison-primary', 'comparison-negative'):
    for entry in json.loads((attempt/report/'custody.json').read_text(encoding='utf-8')):
        path = Path(entry['path']).resolve()
        entry['path'] = path.relative_to(root).as_posix()
        custody.append(entry)
already = {entry['path'] for entry in custody}
# Only task-owned paths: no unrelated recursive scan or sensitive material.
for directory in (Path('artifacts/exp-001'), Path('experiments/exp-001')):
    for path in sorted(directory.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts:
            continue
        relative = path.as_posix()
        if relative in already or path.suffix in ('.f32', '.f64'):
            continue
        custody.append({'path': relative, 'bytes': path.stat().st_size, 'sha256': digest(path)})
for path in sorted(destination.iterdir()):
    if path.is_file() and path.name != 'artifact-custody.json':
        custody.append({'path': path.as_posix(), 'bytes': path.stat().st_size, 'sha256': digest(path)})
target = destination/'artifact-custody.json'
if target.exists():
    raise RuntimeError('Refusing custody overwrite')
target.write_text(json.dumps(custody, indent=2)+'\n', encoding='utf-8')
print(f'Exported6 portable reports;{len(custody)} custody entries;raw bytes retained locally')
