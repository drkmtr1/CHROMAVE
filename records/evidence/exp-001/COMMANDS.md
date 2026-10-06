# EXP-001 commands and retained attempts

Working directory: C:\Users\WILLI\Projects\CHROMAVE. Coordinator execution, existing tools only. Source/manifest audit precedes primary outputs. Output refusal prevents overwriting; each correction/rerun receives a new attempt directory. Failures and negatives remain retained. No production binary or dependency installed.

Executed before render:

```
C:\Python313\python.exe experiments/exp-001/oracle/make_manifest.py records/evidence/exp-001/manifest.csv
cmd /c experiments\exp-001\build.cmd > artifacts\exp-001\build-final.log 2>&1
C:\Python313\python.exe experiments/exp-001/analysis/check_verifier.py
```

Generator reported204 primary/4 negatives/1,933,632,000 primary bytes. Final build exit0, MSVC /std:c++17 /EHsc /O2 /fp:precise /W4; no warnings. Earlier build attempts also exited0; no earlier DSP output was produced. Build log/binaries and source identities are hashed in preflight custody.

Attempt001 planned commands (outcomes separately recorded, no success inferred):

```
artifacts/exp-001/bin/oracle.exe records/evidence/exp-001/primary.csv artifacts/exp-001/attempt-001/oracle-primary
artifacts/exp-001/bin/candidate.exe records/evidence/exp-001/primary.csv artifacts/exp-001/attempt-001/candidate-primary
artifacts/exp-001/bin/oracle.exe records/evidence/exp-001/negative.csv artifacts/exp-001/attempt-001/oracle-negative
artifacts/exp-001/bin/candidate.exe records/evidence/exp-001/negative.csv artifacts/exp-001/attempt-001/candidate-negative
C:\Python313\python.exe experiments/exp-001/analysis/compare.py records/evidence/exp-001/primary.csv artifacts/exp-001/attempt-001/candidate-primary artifacts/exp-001/attempt-001/oracle-primary artifacts/exp-001/attempt-001/comparison-primary
C:\Python313\python.exe experiments/exp-001/analysis/compare.py records/evidence/exp-001/negative.csv artifacts/exp-001/attempt-001/candidate-negative artifacts/exp-001/attempt-001/oracle-negative artifacts/exp-001/attempt-001/comparison-negative --negative
```

PowerShell redirects each render/comparison stdout/stderr to its task-owned attempt log. Exact executable arguments above remain unchanged by logging. Tool exit evidence and compact retained logs/results establish actual outcomes.
