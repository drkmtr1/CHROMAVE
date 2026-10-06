# EXP-001 — retained standalone timing/routing results

Candidate: TASK-003 disposable harness under D-004, accepted DESIGN-001 revision3 hash0A29614548A4868915FCF0E13FDDD5BB9510615C3CAA5854E79144E624185769. Experiment outputs attempt001,20 seconds per render. USER REQUIREMENTS remain MASTER_SPEC section9; actual M1/behavior decisions remain D-004. Numerical observations below do not accept a production DSP contract.

## Actual numerical result

All204 primary renders completed and passed unchanged max1e-6/RMS2e-7 fidelity criteria against independently constructed double absolute-history reference. Maximum observed absolute error1.0920792226087883e-7; maximum RMS9.407937672586133e-9. Outputs and instrumented state finite; maximum stored absolute sample0.7119159698486328, below restricted1.25001 limit. No primary render/comparison failure or DSP correction occurred.

All manifested partition comparisons are bit-identical (maximum and RMS differences0). Static first-arrival/first-three echo amplitude/channel checks and all expected lifecycle/event/endpoint trace checks passed (0 errors). Coverage remains the accepted10 selected panels, not an exhaustive Cartesian matrix. The static250ms first arrivals are sample11025/12000/24000 at rates44100/48000/96000Hz respectively; anti-phase cancellation and these arrival checks are measured for the static fixture family only.

| Panel | Primary renders / result |
| --- | --- |
| P1 static five sources/taps/routes/rates | 60 / PASS |
| P2 controller retarget/mode/return/repeat | 24 / PASS |
| P3 endpoint collision | 3 / PASS |
| P4 routing/return/repeat | 3 / PASS |
| P5 high-feedback timing rate/partition | 72 / PASS |
| P6 high-feedback routing rate/partition | 12 / PASS |
| P7 zero-feedback timing | 6 / PASS |
| P8 feedback baseline | 6 / PASS |
| P9 prescribed read motion | 12 / PASS |
| P10 pluck timing/listening | 6 / PASS |

Four altered negative controls were rejected against the nominal reference: wrong-side and off-by-one each max.0625/RMS~6.59e-5; dropped pending max~.124/RMS~.00954; repeated-target restart max~.00156/RMS~3.90e-5. Comparator negative-mode PASS means successful detection of an intentionally incorrect candidate, not its DSP conformance. Exact errors/traces retained in negative-summary.json and raw custody.

## Descriptive diagnostics and pending listening

Motion's1.05–1.45-second FFT window has2.5Hz bin spacing and dominant950Hz bin at each rate.20ms fixed950Hz least-squares phase windows yield inferred frequencies approximately949.999963–950.000032Hz at44100;48000/96000 near950 to numerical precision. Maximum fitted phase candidate/reference differences~6.19e-10,7.47e-13,1.05e-10 radians respectively. These averaged diagnostics do not establish exact instantaneous950Hz or eliminate sampled interpolation ripple. No frequency, transient/mono-cancellation or subjective production threshold was invented. Channel/fold energies, output/internal peaks and native-gain transient-window descriptors remain in the summaries/diagnostics.

Listening package:17 groups/78 encoded PCM16 stereo clips, opaque shuffled A/B/C alternatives where present, both declared [.95,1.2] and [.95,1.75] excerpts, same retained0dB gain, normalization0dB, no clipping. Includes all P2/P3/P4/P10 rows and irregular P9 at each rate; redundant stress partitions remain numerical evidence. Shuffle seed20261005 and reveal mapping saved. Start with retarget sine and pluck; single-alternative routing/motion groups are diagnostics, not preference comparisons. Local `artifacts/exp-001/attempt-001/listening/LISTEN.md` links clips; reveal.json kept separate. **Owner listening/preferences: PENDING.** No agent claims to have auditioned them or measured genre suitability.

Recommendation/advice only: numerical evidence supports keeping A20ms as the provisional Smooth lead, with B5ms comparison and explicit CRepitch alternative available for owner audition. It does not settle20ms as a released coefficient or authorize production reuse.

## Independence, custody and unfavorable history

Independent oracle author `/root/exp001_oracle_author` had no candidate source/output access. Root finished float-ring candidate before viewing returned double absolute-history/matrix/piecewise source. Non-authoring `/root/exp001_technical_review` checked sources, math and complete manifest before outputs. Construction/procedural independence is evidenced; enforced hidden-context isolation is not claimed. Raw references are retained, not reconstructed from candidate outputs.

Pre-output review identified F-012 omitted partition RMS and F-013 malformed trace acceptance risks; both corrected before any render, without changing criteria. Valid/malformed evidence probes retained. F-014 coordinator listening invocation ran before comparison summary completion; it exited1 with missing-file prerequisite before creating clips. Original listening.log retained. After comparison process exited0, retry exited0 and generated78 clips; no DSP rerun, threshold change or failed audio replacement. All actual commands and dispositions retained; no performance inference from elapsed offline execution.

Portable evidence: records/evidence/exp-001 primary/negative summaries, diagnostics, verifier probes, manifests/events, independent derivation, environment, preflight/source/binary custody and artifact-custody.json (964 entries). Raw candidate primary1,933,632,000 bytes and reference3,867,264,000 bytes, four altered negatives and all traces/logs/binaries/listening retained locally under ignored artifacts/exp-001. Hashes refer to final encoded bytes. Compact evidence exports reproduce original reports byte-for-byte; paths in aggregate custody are repository-relative. No multi-GB raw/audio/binary upload is authorized.

Environment: existing MSVC19.44.35228 x64, Python3.13.5/NumPy2.5.0 x64 on Windows11 ARM hardware. Runtime/component identifiers and unknown CIM metadata recorded in ENVIRONMENT.md. No native-x64 support, plugin build, host, latency/tail/state/preset/bypass/transport, real-time CPU, nonlinear character/filter/ducking/motion module or complete-loop release claim. Arbitrary invalid/out-of-range Free requests and broader combinations remain untested. F-002/F-003 production prerequisites remain open; F-005 template identity limitation remains.

## Review, disposition and stop

Final actual-evidence technical **PASS**, REVIEW-003, including independent all208 waveform/all964 custody checks and F-012–F-016 correction verification. Distinct fresh **PASS for owner presentation**, READINESS-003; no new finding. No Product Owner EXP-001 acceptance received. D-005 now permits the prepared32-path experimental source/evidence publication; numerical evidence/conclusions unchanged. Final checkpoint/push/clean equality outcome belongs to live refs/tool evidence after all planned record mutations, not the earlier tip.

STOP: **EXP001_AWAITING_PRODUCT_OWNER_ACCEPTANCE**. Applicable independent reviews complete; D-005 authorizes public checkpoint reconciliation/push. Owner audition/disposition remains pending and separate from publication. No production or successor work is authorized.
