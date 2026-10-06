# EXP-001 independent derivation — before outputs

Author: `/root/exp001_oracle_author`, bounded read-only assignment. Read accepted DESIGN-001 revision3; no candidate source/output access or filesystem writes. Coordinator completed candidate before viewing returned oracle source, then integrated it with whitespace formatting and nonempty-output refusal only. Independence is procedural and construction-based; no enforced hidden-context sandbox is claimed.

Oracle: double absolute-history vector, floor/fraction lookup at absolute n-d*fs, explicit injection/feedback matrices, separately constructed piecewise transition plan and event schedule. Candidate: float circular history and per-sample state machine. No DSP controller/indexing source shared. The common CSV/trace interface is an execution contract.

Static delay samples: 11025 at44100,12000 at48000,24000 at96000. With character c=.5 and feedback g=.5, q=.25. Echo k before character is q^(k-1) R^(k-1) Jx; after character multiply by .5. Stereo J=R=I; Ping-Pong Jx=((L+R)/2,0), R swaps channels.

| Input | Stereo pre first three | Ping-Pong pre first three |
| --- | --- | --- |
| (.125,.125) | (.125,.125);(.03125,.03125);(.0078125,.0078125) | (.125,0);(0,.03125);(.0078125,0) |
| (.125,0) | (.125,0);(.03125,0);(.0078125,0) | (.0625,0);(0,.015625);(.00390625,0) |
| (0,.125) | (0,.125);(0,.03125);(0,.0078125) | (.0625,0);(0,.015625);(.00390625,0) |
| (.125,-.0625) | (.125,-.0625);(.03125,-.015625);(.0078125,-.00390625) | (.03125,0);(0,.0078125);(.001953125,0) |
| (.125,-.125) | (.125,-.125);(.03125,-.03125);(.0078125,-.0078125) | zero throughout |

All post values are half these pre values. Diagnostic mono signal is (L+R)/2; reported fold energy sums its square. Anti-phase Stereo folds to zero; anti-phase Ping-Pong injection is zero. This describes the accepted mono-summed model's cancellation, not a defect threshold or musical preference.

At44100: n0=44100, request at44188, N20=882,N5=221. A first endpoint44982, queued return45864; B44321,44542. C return settles45070 from the retarget request, while identical repeat retains44982. Routing44982,45864. Endpoint-collision next timing finishes A/C45864,B44542; routing45864. Endpoint retirement precedes same-sample event arbitration.

Bound: infinity norms of convex read/interpolation and proposed injection/routing matrices are at most1. With |x|<=.125 and g<=.9, B<=.125+.9B gives B<=1.25. Pluck analytic bound .12 lies inside input envelope. Bound applies only to these memoryless proxies, not nonlinear production character.

Matrix totals independently derived: P1=60,P2=24,P3=3,P4=3,P5=72,P6=12,P7=6,P8=6,P9=12,P10=6, total204. Candidate raw bytes1,933,632,000; reference double bytes3,867,264,000. Four altered negatives separately manifested. Omitted interactions remain omitted per accepted protocol.

Author arithmetic is pre-output advice. Non-authoring technical audit and actual observations are recorded separately in REVIEW-003 and EXP-001-RESULTS.
