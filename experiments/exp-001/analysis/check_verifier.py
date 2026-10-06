"""Targeted regression probes for malformed audit evidence, before DSP outputs."""
import csv
import json
from pathlib import Path
import compare

destination = Path('artifacts/exp-001/verifier-probes')
if destination.exists():
    raise RuntimeError('Refusing to overwrite prior probes')
destination.mkdir(parents=True)
fields = sorted(compare.TRACE_FIELDS)
good = {field: '0' for field in fields}
good['reason'] = 'audit'

def write(name, data, columns=fields):
    path = destination/name
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)
    return path

reference = write('reference.csv', [good])
assert compare.check_trace(reference, reference) == []
observations = []
for name, data, columns in (
    ('nan.csv', [{**good, 'read_old': 'nan'}], fields),
    ('infinity.csv', [{**good, 'read_new': 'inf'}], fields),
    ('duplicate.csv', [good, good], fields),
    ('missing.csv', [{k: v for k, v in good.items() if k != 'route_weight'}],
     [k for k in fields if k != 'route_weight']),
    ('empty.csv', [], fields),
):
    errors = compare.check_trace(write(name, data, columns), reference)
    assert errors, name
    observations.append({'fixture': name, 'rejected': True, 'errors': errors})
(destination/'result.json').write_text(json.dumps(observations, indent=2)+'\n', encoding='utf-8')
print('PASS: valid audit accepted; NaN, infinity, duplicate, missing field and empty audit rejected')
