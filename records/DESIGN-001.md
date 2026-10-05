# DESIGN-001 — M1 core behavior and EXP-001 protocol

Revision 3; **proposed behavior, NOT an accepted DSP contract**. D-002 approves PLAN-001 direction and TASK-002 documentation/design only. USER REQUIREMENTS remain MASTER_SPEC section 9; actual dispositions remain DECISIONS. This document records recommendations, experiment assumptions and unresolved choices, not runtime results or implementation authority. Revisions1–2 and their REVISE findings are preserved under `records/evidence/task-002/` and REVIEW-002; revisions address F-006–F-010 without changing authority or executing experiments.

Leading advice: post-character first echo; channel-preserving Stereo and mono-summed left-first Ping-Pong; explicit Smooth/Repitch timing style with Smooth default. Apply that selected style to manual edits, automation and tempo targets alike, without guessing intent from numeric updates. These proposals serve REQ-01/03/05/07 and repeat evolution; musical quality remains unproved.

## 1. First echo and round trip

For explanatory analysis only: two-channel vectors, fixed integer delay D > 0, injection J, routing R, scalar feedback 0 <= g < 1, identical linear time-invariant per-channel character C, zero initial history:

`a[n] = b[n-D]`; `b[n] = J*x[n] + g*R*C(a)[n]`.

Pre-character audible tap: `w_pre[n] = a[n]`; post-character: `w_post[n] = C(a)[n]`. Read → character → split audible/feedback branches → route feedback → feedback gain → add injected source → store. The pre-tap alternative changes only the audible tap. The dry path preserves original input separately. General C notation means an operator over history, not necessarily a memoryless multiply.

For an isolated impulse-shaped contribution, p1 = J*x and p(k+1) = g*R*C(pk). Pre tap hears pk; post hears C(pk). Under the stated linear, identical-channel assumptions C commutes with channel swapping:

| Echo contribution | Pre tap | Post tap |
| --- | --- | --- |
| First, near D | J*x | C*J*x |
| Second, near 2D | g*R*C*J*x | g*R*C²*J*x |
| Third, near 3D | g²*R²*C²*J*x | g²*R²*C³*J*x |

A real filter spreads a contribution across time; “near” does not promise a single peak. Character processing latency is unresolved. Do not extrapolate linear superposition, g powers or commutation to saturation, differing channel processors or moving reads; retain the actual nested recurrence there. This is an explanatory model, not a stability proof.

Recommendation: post tap makes tone audible immediately and again on each circulation. Alternative: pre tap gives a cleaner first repeat. Neither selects filter topology/order, saturation, smoothing or gain compensation. Owner choice required.

## 2. Stereo and Ping-Pong

Stereo: J = I, R = I. Proposed Ping-Pong: s = (L+R)/2, J*x = (s,0), R swaps L/R. First side is always left, without input-side detection or a hidden alternating reset phase. No actual host-bus contract is selected.

Exact diagnostic model below uses post tap and **memoryless scalar proxy** C(v)=c*v; this is not a real filter/saturation model:

| Source at sample zero | Stereo echoes 1 / 2 / 3 | Ping-Pong echoes 1 / 2 / 3 |
| --- | --- | --- |
| Centered (m,m) | c(m,m) / gc²(m,m) / g²c³(m,m) | (cm,0) / (0,gc²m) / (g²c³m,0) |
| L-only (m,0) | (cm,0) / (gc²m,0) / (g²c³m,0) | (cm/2,0) / (0,gc²m/2) / (g²c³m/2,0) |
| R-only (0,m) | (0,cm) / (0,gc²m) / (0,g²c³m) | Same Ping-Pong sequence as L-only |
| Stereo (l,r), s=(l+r)/2 | c(l,r) / gc²(l,r) / g²c³(l,r) | (cs,0) / (0,gc²s) / (g²c³s,0) |
| Anti-phase (m,-m) | Channel difference preserved with decay | Zero wet excitation |

Conceptual native-mono adapter: x=(m,m), giving full-level left-first excitation. Real mono/stereo bus support remains a host-design prerequisite. Averaging avoids doubled centered amplitude but halves one-sided input, cancels anti-phase content and discards wet stereo differences. Dry input is preserved. Diagnostic fold-down F(L,R)=(L+R)/2 halves a one-sided echo's active-channel amplitude; this is no constant-loudness promise.

Stereo-preserving alternative: J=I and swap feedback R. One-sided components alternate and stereo components cross; centered identical channels stay centered because swapping equal values changes nothing. This preserves wet stereo information but cannot promise centered-source audible alternation. Asymmetrical delays or mid/side injection would be a new substantive design choice. No hidden compensation is proposed.

Routing-mode change candidate: preserve history and linearly interpolate J and R between endpoint matrices over 20 ms, using one shared weight and the common discrete trajectory rule in section3. One active transition plus latest pending destination; complete the active transition before starting the latest pending destination. While active, a desired mode matching the active destination clears pending work without restarting; a return to the old committed mode stays pending. Compare against committed mode only when idle. Intermediate echoes need not strictly alternate. No duplicated engines, state clearing or abrupt tail relocation. The interpolation of two matrices is an experiment candidate, not validated product behavior.

## 3. Timing, retargeting and event order

One linked L/R duration. Free time and Sync division are retained independently. Sync duration in seconds is 60*b/B, where b is quarter-note beats and B valid BPM; BPM updates do not overwrite another automatable control.

**Smooth:** two fixed reads share one history; a=(1-alpha)*a_old+alpha*a_new. Apply C once to the mixed read and feed back that same processed mixture, not two independently recirculating engines. Convex weights avoid correlated equal-power gain increase but phase cancellation and overlapping echo texture remain possible. No artifact-free/pitch-perfect claim.

Common discrete rule for Smooth, Repitch and routing: N=max(1,floor(T*fs+.5)), positive half ties upward; j=0..N inclusive; alpha=j/N. At start n0, j=0 uses the start value; endpoint n0+N uses the destination. Smooth5 at44100 gives N=221; Smooth20 gives N=882. Smooth mixes fixed reads; Repitch uses D(j)=(1-alpha)*D_start+alpha*D_target; routing interpolates each matrix entry with the same alpha. Endpoint retirement commits the destination before current-sample arbitration. If queued work starts on that endpoint sample it begins at j=0, so the evaluated read/matrices stay at the just-reached endpoint. One active fade and one latest pending destination bound state. Finish the active fade before transitioning to the latest pending target; fast updates may lag/skip destinations. For duration-only updates with fixed style, final settling after updates stop is at most two fade durations.

**Repitch:** move one read duration linearly from its currently evaluated value to the new target over 20 ms. New targets replace the old destination from the current position, preserving position but allowing a slope change. Large moves can create strong pitch shifts or reverse read motion; do not silently suppress that consequence. Analytical observation: reading sin(2*pi*f*(t-D(t))) has local signed frequency f*(1-D'(t)), independent of the quality of an eventual interpolation implementation. [Primary time-varying-delay text](https://www.dsprelated.com/freebooks/pasp/Time_Varying_Delay_Effects.html).

Apply the chosen style equally to manual/text, host automation and tempo changes. VST3 documents sample-offset parameter queues, but actual framework/host delivery must be verified separately; fixtures below model declared sample-timestamped events, not observed FL Studio guarantees. [Official VST3 automation](https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical%2BDocumentation/Parameters%2BAutomation/Index.html).

Proposed sample-n processing order:

1. Evaluate active trajectories at n; retire endpoints reached now without yet launching pending work.
2. Collect events timestamped n. Last event for the same control in the declared fixture order wins. Build one snapshot; equality includes effective timing duration and timing style. Repeated desired values matching an active destination are no-ops, not trajectory restarts.
3. Compute one effective time target from the snapshot; apply the routing snapshot independently. While Smooth is active, compare desired timing duration/style with the ACTIVE DESTINATION: equal clears stale pending work without restarting; different replaces pending work, even if the desired duration equals the old committed duration. For active routing use the same rule on destination mode. When idle compare against committed duration/style or mode and start only a different destination. Repitch remains retargetable from its evaluated current position; matching its active destination/style does not restart. Host events arriving at an endpoint replace any stale pending snapshot before the next trajectory starts.
4. Start the eligible transition or retain/queue its latest destination. If a Smooth fade is still active, timing style/target changes wait together until that endpoint. Repitch→Smooth starts from the current moving position as its old fixed read. Routing uses its own active/pending state.
5. Read → character/split → route/feedback gain → injection/write → output.

Free/Sync switches use the retained respective value and same timing policy. A completed Smooth fade considers all current-sample events before launching pending work. Exact host/controller concurrency and arbitration remain outside this sample-fixture model.

Invalid/missing BPM: hold last valid effective Sync target and visibly indicate unavailable tempo; use 120 BPM only before any valid tempo exists. Reject nonfinite duration requests; clamp finite out-of-range requests to proposed bounds. Reset/startup/restore semantics for retained tempo, transport stop/seek, bypass, latency and tails remain unresolved lifecycle work, not inferred from this proposal.

## 4. Semantic controls and provisional limits

| Control | Proposed meaning / rationale; all numeric values unaccepted |
| --- | --- |
| Free/Sync | Linked timing; no independent L/R durations in this candidate. |
| Free time | 10–2000 ms: audible short repeats to long echoes, excluding zero-delay algebraic loops. This excludes shorter comb/flanging use cases. |
| Sync division | Candidate straight b={1/8,1/4,1/2,1,2,4} quarter-note beats. PLAN-001 also proposes dotted/triplet choices; compact final representation/set remains an owner scope decision, not silently removed here. |
| Effective Sync duration | Same 10–2000 ms bounds, with visible limiting status; extreme BPM can break the selected beat relationship. |
| Feedback | Semantic persistence; experiment g=0/.5/.9. Candidate released maximum 90% remains conditional on complete-loop evidence; no self-oscillation promise. |
| Stereo/Ping-Pong | Explicit injection/routing alternatives in section 2. |
| Smooth/Repitch | Explicit sound choice; leading experimental transition duration 20 ms, not an accepted coefficient. |
| Wet/Dry | Candidate complementary linear gains (1-mu,mu), mu=0..1, including wet-only; phase relationships prevent constant-loudness promises. |

Tone/drive/motion/ducking retain approved PLAN-001 direction/conditional status. Numeric tone ranges/defaults, parameter mapping/IDs/automation eligibility/state compatibility remain unresolved. No nonfunctional knobs. Two-channel float storage at 96 kHz for 2 seconds is approximately 1.536 MB before guards/additional state: an arithmetic estimate, not a measured resource budget. JUCE supports fractional/samplewise reads and warns maximum-delay resizing may allocate; no library/version choice follows. [Official DelayLine](https://docs.juce.com/master/classjuce_1_1dsp_1_1DelayLine.html).

## 5. EXP-001 — one timing/routing comparison protocol

Question: can candidate injection, timing styles and interrupted transitions match the declared semantics, and what audible differences justify the proposed default? **Design only; no execution authorized.** A later explicit task may implement one disposable standalone harness, without plugin/host adapter, nonlinear character/ducking, dependency installation or production promotion by implication.

### Controlled scope and matrix

- A: convex fixed-read Smooth, 20 ms; B: same Smooth, 5 ms; C: single moving read Repitch, 20 ms. A/B use their fade duration for timing only; routing duration is 20 ms in all candidates.
- Each tested in Stereo and mono-summed left-first Ping-Pong: six candidate configurations. Include the dedicated routing-transition fixture, starting Stereo.
- Rates fs={44100,48000,96000}; partition patterns {1}, {64}, {512}, repeated {17,113,29,251}, truncating final block. Identical absolute events across partitions.
- Use the exact mandatory panels below, not a Cartesian product of every fixture/schedule/gain. Every panel is wet-only with zero initial history and C=I unless explicitly stated. Static pre/post uses g=.5, C=.5I, D=250 ms. Memoryless proxies only; no filter/nonlinear claim.
- Read interpolation is explicitly mathematical linear interpolation for this harness, including C; this is a controlled experiment assumption, not production interpolation selection. Candidate source and oracle must separately document indexing/guard conventions.

### Fixtures and schedules

Each render is exactly round(20*fs) samples. Events in seconds map to round(t*fs), with positive ties rounded upward; same-sample collisions preserve the order listed. Time requests remain exact seconds converted to fractional samples. Synthetic fixtures use absolute n/fs and zero outside the stated excitation interval; each source is a separate run.

| Fixture | Exact source |
| --- | --- |
| Impulses | At n=0: (.125,.125), (.125,0), (0,.125), (.125,-.0625), (.125,-.125); zero elsewhere. |
| Step | Centered .125 for 0<=t<2 seconds, then zero. |
| Sine | Centered .125*sin(2*pi*1000*n/fs) for 0<=t<2 seconds. |
| Pluck | Two centered events at 0 and 1 seconds. For each event tau=t-event_time>=0 and <1: .04*exp(-8*tau)*(sin(2*pi*220*tau)+sin(2*pi*330*tau)+sin(2*pi*440*tau)); zero outside each event interval. |

Source/schedule combinations are limited to the mandatory panels below; no unstated random seed/material or blanket Cartesian obligation:

| Schedule | Initial state / ordered events / final desired state |
| --- | --- |
| Static | Free 250 ms; retained Sync b=1/B=120; no events. Final timing unchanged. |
| Retarget | Free 250 ms; at 1 s request 375 ms; 1.005 s request 125 ms; 1.009 s request 300 ms. Final destination Free 300 ms. |
| Mode/collision | Free 250 ms; retained Sync b=1, BPM120. At 1 s select Sync b=1/BPM120; 1.005 s BPM90; 1.009 s invalid BPM then b=.5 then b=1; 1.02 s set Free=250 ms, select Free, toggle style (A/B→Repitch; C→Smooth20). Invalid event manifest payload is the literal string `INVALID_TEMPO_NONFINITE`, interpreted as quiet NaN by each evaluator, never a numeric zero or JSON NaN. Last valid Sync target remains 60/90 seconds until selecting Free. Final destination Free250 with toggled style. |
| Routing | Timing fixed Free250; start Stereo; at 1 s Ping-Pong, 1.005 s Stereo, 1.009 s Ping-Pong. Final routing Ping-Pong; timing unchanged. |
| Timing return-old | Free250, candidate style; at1 s request375 ms; at1.002 s request250 ms, no further events. Final Free250. A/B must finish375 then return250, exposing dropped pending work; C retargets from evaluated current duration to250. |
| Timing repeat/no-restart | Free250, candidate style; at1 s request375 ms; at1.002 s repeat375 ms, no further events. Final375 at the original endpoint, not a restarted endpoint; pending empty. |
| Routing return-old | Timing Free250, start Stereo; at1 s Ping-Pong; at1.002 s Stereo, no later events. Must complete Ping-Pong then return Stereo, exposing dropped pending work. |
| Routing repeat/no-restart | Timing Free250, start Stereo; at1 s Ping-Pong; at1.002 s repeat Ping-Pong. Final Ping-Pong at original20 ms endpoint; pending empty. |
| Endpoint collision | Free250, start Stereo; at1 s request375 ms and Ping-Pong. At timing endpoint n0+N_timing request300 ms; at routing endpoint n0+N_routing requestStereo. If endpoints coincide, declared order is timing event then routing event. New trajectories begin at endpoint j=0 with no state jump; A/B new fade300, C new ramp300, routing returnsStereo. |
| Read-motion diagnostic | Sine, g=0; directly prescribed read duration250 ms until1 s, linear250→275 ms from1 to1.5 s, then hold275. Bypasses candidate transition controller solely to characterize interpolation/read motion. The IDEAL continuous-time signed frequency is950 Hz inside the ramp away from edges. Actual sampled linear interpolation can exhibit phase/frequency ripple; compare waveforms against the independent sampled reference and report deviations without an invented frequency tolerance. This is not a product automation conformance test. |

Initial timing style follows A/B/C; other runs do not inherit state. At t=0, startup uses declared timing without fade. No transport/reset/preset event is modeled. Render continues through silence; retain all outputs, including no-energy impulse transition cases. Listening primarily uses sine/step/pluck segments, not a lone impulse already gone before a retarget. Endpoint-collision events are specified as absolute sample indices derived from n0 and the common N rule, without conversion back through seconds.

Paper trace at44100 (not executed evidence): n0=44100; return/repeat event round(1.002*fs)=44188. A endpoint44982, queued return-old endpoint45864; B endpoint44321, queued return-old endpoint44542; C return-to250 endpoint45070 from the retarget sample, while a repeated375 target keeps original endpoint44982. Routing first endpoint44982 and return-old endpoint45864. On endpoint-collision A/C300 transitions finish45864; B300 finishes44542; routing return finishes45864. These precomputed endpoints must be checked by the independent oracle author/reviewer before candidate outputs. A wrong discarded pending value, restarted identical destination or endpoint arbitration must fail the trace comparison.

### Mandatory panels and bounded workload

Panel choices are declared before results. A/B/C means each candidate's stated timing style; routes are the two fixed initial modes unless the schedule explicitly starts Stereo. Irregular means repeating {17,113,29,251}. All renders remain20 seconds. Distinct rows do not imply unlisted source/gain products.

| Panel | Exact mandatory combinations | Renders |
| --- | --- | --- |
| P1 static tap/routing | Five impulse vectors × two audible taps × two routes × three rates; Static schedule, A, g=.5, C=.5I, partition64. | 60 |
| P2 controller edges | Sine × {Retarget, Mode/collision, Timing return-old, Timing repeat/no-restart} × three styles × two routes; fs48000, irregular, g=.5. | 24 |
| P3 endpoint edges | Sine × Endpoint collision × three styles; declared startStereo; fs48000, irregular, g=.5. | 3 |
| P4 routing edges | Step × {Routing, Routing return-old, Routing repeat/no-restart}; A, declared startStereo, fs48000, irregular, g=.5. | 3 |
| P5 timing rate/partition stress | Sine × Retarget × three styles × two routes × three rates × four partition patterns; g=.9. | 72 |
| P6 routing rate/partition stress | Step × Routing × three rates × four partition patterns; A, declared startStereo, g=.9. | 12 |
| P7 zero-feedback timing | Sine × Retarget × three styles × two routes; fs48000, irregular, g=0. | 6 |
| P8 feedback baseline | Centered impulse × two routes × g={0,.5,.9}; Static, A, C=I, fs48000, partition64. | 6 |
| P9 prescribed read motion | Sine × Read-motion diagnostic × three rates × four partition patterns; g=0, Stereo, prescribed trajectory (no controller style). | 12 |
| P10 pluck listening | Pluck × Retarget × three styles × two routes; fs48000, irregular, g=.5. | 6 |
| Total | Mandatory primary candidate renders, excluding failure reruns/reference/negative-control artifacts. | **204** |

Raw stereo float32 primary output storage is precomputable:8 bytes*20 seconds*sum(fs over204 runs)=**1,933,632,000 bytes**, approximately1.93 GB (1.80 GiB), excluding headers, state traces, reference double outputs and reruns. This is arithmetic, not measured memory/runtime. Streaming raw outputs and compact scalar/state summaries avoids requiring all audio in memory. Named environment/resource feasibility and raw-output format are execution-task prerequisites; do not infer performance.

Every policy edge is exercised at48 kHz/irregular blocks; representative high-feedback timing/routing and read motion span all rates/partitions. All five source vectors/taps/routes span rates in static diagnostics. This does not cover every edge/source/gain at every rate/partition; nonlinear character, actual filters, host scheduling, long-release behavior and exhaustive rate/edge interactions remain untested. Further combinations require an explicitly bounded extension selected before execution; do not add/drop panels after observing outcomes to force a winner.

Negative controls, separately manifested and excluded from204: one representative P1 centered/post/Ping-Pong/48k case with wrong first side and one with a one-sample delay error, plus one P2 A/Stereo/Timing return-old case with dropped pending work and one P2 A/Stereo/Timing repeat case with an unwanted restart. They must fail oracle comparison; retain altered output and failure records. Reference outputs and failed/rerun histories are additional custody artifacts, not a blanket Cartesian panel.

### Independent oracle and predeclared criteria

Before viewing candidate outputs, construct handwritten static impulse arrival/amplitude tables; independent double-precision direct-history evaluation with absolute indices, floor/fraction lookup, explicit J/R matrices and event schedules; and channel/fold-down matrix calculations. Do not share candidate ring indexing, transition-state code or output-derived constants. A non-authoring technical reviewer checks derivation. Deliberately wrong first side, one-sample delay error and ignored pending target must fail the comparison; retain those negative controls.

For memoryless C=.5I, g=.5, D=250 ms, centered (.125,.125), expected Stereo post-tap echoes: (.0625,.0625), (.015625,.015625), (.00390625,.00390625); Ping-Pong: (.0625,0), (0,.015625), (.00390625,0). Pre-tap Stereo echoes: (.125,.125), (.03125,.03125), (.0078125,.0078125); Ping-Pong: (.125,0), (0,.03125), (.0078125,0). These are fixture arithmetic, not executed observations.

Proposed **predeclared experiment fidelity**: max absolute candidate/reference error<=1e-6; RMS<=2e-7; static integer impulse arrival exactly the declared sample. Require finite outputs/state and partition consistency within the same tolerances. Float-versus-double feasibility is unmeasured: if tolerance proves unsuitable, retain failure and justify a labeled protocol revision rather than silently relaxing it. No release quality threshold follows.

For |input channel|<=.125, C=I, convex interpolation/reads, proposed J/R with infinity norm<=1 and g<=.9, the analytical infinity-norm history bound is1.25. Require maximum absolute stored sample<=1.25001. Interpolated routing matrices retain that norm bound; this result does not establish nonlinear/variable-gain release stability. The pluck's analytic amplitude bound is .12, inside the envelope. Instrument stored state as well as output, and report any separate arithmetic overshoot.

Record transition waveforms, channel energies, diagnostic mono fold-down, committed/pending targets and settling, phase/frequency, peak/internal-state envelopes. No invented production thresholds for cancellation, transient metrics or subjective artifacts. Listening uses the same retained gain, fixed excerpts [.95,1.2] and [.95,1.75] seconds for transition/read-motion cases, randomized opaque A/B/C labels and saved reveal order. Match comparison level where practical without hiding native gain differences; save any normalization offsets. Owner preferences/dislikes are evidence, not technical conformance.

Selection: fidelity failure disqualifies a candidate until corrected under the same protocol. Provisionally prefer A for Smooth; B only if the owner finds its transitions acceptable and prefers faster settling. C is the explicit Repitch alternative. Inconclusive listening preserves provisional advice and limitations; objection yields REVISE, not a forced winner. No experiment result alone accepts a DSP contract or authorizes production reuse.

### Custody, failures and stop

Retain protocol/oracle hashes, independent author/reviewer identity, candidate revision, named compiler/toolchain/hardware, exact commands, source/fixture/event manifests, raw float outputs, summaries, block schedules and listening order. Hash all raw artifacts after final encoding; do not replace them with plots. Preserve failed runs and all negative/inconclusive outcomes.

Stop an affected run on nonfinite output, bound violation, oracle disagreement, uncontrolled event timestamps or unexplained partition dependence; retain diagnostics and report blocker. Do not reclassify protocol errors as successful candidate results. A changed criterion/protocol gets a new explicit revision; material scope/behavior changes require actual owner authorization. No benchmark or host result is claimed by the design.

## 6. Requirements trace, prerequisites and owner decisions

| Source / design output | Verification and remaining limitation |
| --- | --- |
| REQ-01/05; small core | Sections1–4 plus exact diagnostics: independent document review now; production-quality and complete-loop evidence later. |
| REQ-02; Windows/VST3/FL Studio | Section5 is host-independent model only; bus layouts/sample-offset delivery and actual FL Studio behavior remain F-003 prerequisites. |
| REQ-03 and repeat evolution | Post/pre tap choice makes evolution explicit; C proxy does not establish musical tone, saturation or genre success. Owner listening later. |
| REQ-04/06; considered categories/originality | PLAN-001 deferred candidates retained; original routing/policy advice and primary references, no competitor code/assets/presets. |
| REQ-07 | No contract freeze; EXP-001 protocol, behavior decisions and evidence required before dependent production. |
| REQ-08/09 | TASK-002/TODO/review/readiness/current-state trace, owner acceptance and checkpoint; no successor authority. |

F-002 remains open: M1 supplies decision-ready options, not accepted behavior or experiment results. Separate prerequisites: actual filters/order/coefficients and loop gain; nonlinear/anti-aliasing/timing/CPU analysis; host parameter IDs/ranges/defaults/state/tempo delivery; latency/tail/bypass/stop/reset/restore; pinned toolchain/dependency obligations; supported sample-rate/block/hardware/performance budgets; final dotted/triplet/control/preset/UI scope. F-003/F-005 retain build/provenance limitations.

Product Owner choices after review:

1. First repeat colored immediately (recommended post tap), or clean first repeat (pre tap).
2. Obvious centered-source left/right alternation with mono wet injection and disclosed cancellation (recommended), or stereo-preserving cross feedback with centered input remaining centered.
3. Smooth default plus explicit Repitch alternative (recommended), or another stated timing policy after comparisons. Experimental20 ms is not yet a product coefficient.

M1 acceptance and authority to execute EXP-001 are separate actual owner actions. Complete independent technical review/correction then fresh non-authoring readiness of the identified document. **STOP: M1_AWAITING_PRODUCT_OWNER_ACCEPTANCE.**
