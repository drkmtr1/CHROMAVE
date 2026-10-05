# PLAN-001 — Proposed CHROMAVE application plan

Candidate: revision 1, 2026-10-05 (Pacific/Honolulu), prepared under TASK-001. **PROPOSAL — NOT ACCEPTED.**

Planning author: real bounded read-only in-Codex contributor `/root/planning_readiness`; coordinator integrates records and verifies scope/attribution. Advisory result: **PASS for presentation to the Product Owner; implementation readiness BLOCKED** by unaccepted scope/contracts and missing empirical/build/host evidence. This is planning-author advice, not independent technical review, fresh post-implementation readiness, milestone acceptance or permission to implement.

**STOP: `PLAN_AWAITING_PRODUCT_OWNER_AUTHORIZATION`.**

## 1. Authority, source and record mapping

Current actual Product Owner instructions (D-001): new neutral project; supplied accepted template v1.2 instructions; supplied definition as intent; one bounded in-Codex planning assignment; no application code or tests; explicit approval required before implementation. No architecture, V1 cut, experiment, application baseline, milestone or release has been accepted.

The actual source is `CHROMAVE_APPLICATION_DEFINITION.md`, read in full; `APPLICATION_DEFINITION.md` is absent. Historical existing-project initialization, external-ChatGPT routing and v1.0 acceptance references in the brief are preserved context, not inherited authority. Current instructions and the inspected neutral local state govern. No historical conversation, other repository or template-development approval was imported.

Owner-supplied v1.2 identity is accepted for this task's process selection. Local input hashes are in TASK-001; independent reproducible v1.2 source/export identity is unavailable (F-005). The folder is not a Git repository, so there is no commit, tracking ref, remote checkpoint or remote equality (F-004). Neither limitation prevents the authorized proposal; neither is a claim that an outside repository does not exist.

Single record responsibilities: `MASTER_SPEC.md` section 9 owns attributed USER REQUIREMENTS; this plan owns advice/options/assumptions/questions; `DECISIONS.md` owns actual owner dispositions; `TODO.md` owns findings; TASK-001 owns execution evidence; `PROJECT_STATE.md` owns current gate and next action. Preserve the brief as provenance. No second product-spec or architecture hierarchy is created now.

## 2. USER REQUIREMENTS versus proposed outcomes

Source: brief section 3.2; authoritative transcription: MASTER_SPEC section 9. REQ-01–09 require original production-quality stereo character delay; Windows 11/64-bit/VST3/FL Studio; meaningful synthwave and related genre usefulness; consideration of useful effect categories; fewer excellent modules; independent work informed by public Comeback Kid references; resolved consequential DSP contracts before dependent production; incremental knowledge preservation; bounded tasks and explicit testing/review/acceptance gates.

Additional owner directions: expected modern C++/JUCE/CMake/VST3/Git/GitHub foundation; echoes that evolve as they repeat; original cyberpunk appearance with detailed design deferred. Versions/licenses, exact V1 repeat evolution and visual/control contracts are not selected. The underlying conversations cited by the brief were not independently inspected.

**Recommended compact V1 envelope, not an approved requirement or release promise:** a producer establishes echo rhythm, shapes successive repeats, keeps the source intelligible, saves settings and returns to a useful sound in FL Studio.

| Proposed capability | Proposed purpose / boundary |
| --- | --- |
| Free and host-synchronized timing | Compact accepted straight/dotted/triplet choices; limits, tempo fallback and transitions need contracts. |
| Feedback, wet/dry and wet-only | Predictable persistence and insert/send use; mix/gain/decay laws remain open. |
| Stereo preservation and defined ping-pong | Deliberate routing including centered sources; not a swap-only assumption. |
| Recursive HP/LP tone | Demonstrable successive bandwidth change as the first repeat-evolution baseline; not automatic final character-product acceptance. |
| Input-driven audible-wet ducking | Preserve clarity while keeping the proposed recursive tail independent. |
| Automation and host-project recall | Stable accepted parameters/state behavior; no promise to serialize audio tails. |
| Original readable cyberpunk editor and a small original sound set | Final design follows control contracts. User-preset workflow/count/format remain scope choices. |
| Saturation and restrained delay modulation | Separate conditional candidates, included only after useful sound, artifacts, loop behavior, timing and performance evidence. |

If conditional character candidates fail or are deferred, the owner chooses further bounded work or an explicitly reduced release definition. A clean/filter/ducking core is a developmental outcome, not automatically fulfillment of the final musical character objective.

Retain drift/wow/flutter, dedicated chorus, width/spatial motion, degradation, diffusion, transient shaping, pitch shifting, randomness, self-oscillation and multi-tap as unpromised future candidates (brief section 7). No version/date commitments or competitor parity.

## 3. Architecture recommendation and tradeoffs

Leading recommendation: native C++/JUCE/CMake VST3, with a small testable DSP core separated from host adaptation, parameter/state handoff and editor responsibilities. No generic DSP framework or suite. JUCE provides VST3 plugin targets in its [official CMake API](https://github.com/juce-framework/JUCE/blob/master/docs/CMake%20API.md); this establishes capability, not a working CHROMAVE build.

Candidate routing: input preservation to dry branch; input mapping plus feedback into delay storage/reads; recursive character and stereo routing in the round trip; an explicitly placed audible wet tap; source detector controlling audible wet gain after the feedback split; wet/dry output mix. Tap placement, character order and channel injection are unresolved. No diagram is a frozen contract.

| Decision area | Alternatives / leading advice | Tradeoff and required evidence |
| --- | --- | --- |
| Foundation | JUCE infrastructure/original DSP versus direct VST3 SDK/custom host/UI infrastructure. Investigate JUCE first. | Lower custom integration burden is engineering inference, not measured evidence; review versions, framework constraints and applicable dependency obligations before selection/install. |
| Storage | JUCE DelayLine versus small custom circular buffer. Prefer framework if it meets accepted behavior. | Define indexing, fractional positions, guard samples, limits and allocation lifecycle. Custom code only for an evidenced gap. JUCE documents fractional/sample-wise reads and warns maximum-delay resizing may allocate in the callback. [DelayLine](https://docs.juce.com/master/classjuce_1_1dsp_1_1DelayLine.html) |
| Interpolation | Compare linear and third-order Lagrange; consider Thiran only if its state/phase behavior suits movement. Select none now. | JUCE describes cost/coloration tradeoffs and stateful Thiran limitations under fast modulation. Actual response, circulating-loop coloration and CPU need experiments. [Linear](https://docs.juce.com/master/structjuce_1_1dsp_1_1DelayLineInterpolationTypes_1_1Linear.html), [Lagrange](https://docs.juce.com/master/structjuce_1_1dsp_1_1DelayLineInterpolationTypes_1_1Lagrange3rd.html), [Thiran](https://docs.juce.com/master/structjuce_1_1dsp_1_1DelayLineInterpolationTypes_1_1Thiran.html) |
| Time changes | Moving reads versus dual-read transitions, with a declared manual/automation/tempo policy. | Pitch movement, overlap gain and temporal texture differ. Specify retarget interruption and event ordering; numeric update shape alone cannot reveal producer intent. Test changes under feedback. |
| First echo / recursive tone | Post-character audible tap colors the first repeat; pre-character tap can leave it cleaner. Investigate recursive HP/LP rather than only output tone. | Specify first three echoes, full round-trip order, bypass, smoothing and loop gain. Filtered-feedback theory supports frequency-dependent decay, not proof of nonlinear/time-varying loop stability. [Filtered-feedback model](https://www.dsprelated.com/freebooks/pasp/Filtered_Feedback_Comb_Filters.html) |
| Stereo / ping-pong | Stereo preservation versus deliberate alternating echo injection. | Swapping identical channels leaves them identical. Define injection/downmix, first side, mono input, L/R-only input, mode changes and fold-down before accepting routing. |
| Saturation / anti-aliasing | Recursive or output-only nonlinear color; with/without suitable anti-aliasing. | Different sounds, gain, aliasing, timing and CPU risks. No nonlinear law, ordering or oversampling factor chosen. [JUCE Oversampling](https://docs.juce.com/master/classjuce_1_1dsp_1_1Oversampling.html) documents filter/phase/latency tradeoffs. |
| Ducking | Audible wet gain after split versus gain in loop. Investigate outside-loop internal detector first. | Specify stereo linking, envelope/law/smoothing and control count; test unchanged recursive history. External sidechain is excluded from this proposal. |
| Parameters/state | Framework facilities with explicit real-time processor handoff versus custom state system. | Define IDs/ranges/defaults/schema, invalid state and tail/reset/preset policy. JUCE state copy/replace uses locks and is unsuitable in audio processing. [APVTS](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState.html) |

Recommended real-time obligation: bounded callback work; preallocation at safe lifecycle boundaries; no callback allocation, blocking locks, file/network/UI work or unbounded operations. This needs accepted scope and actual verification; using a framework does not establish real-time safety.

Recommended operational boundary: local audio processing; no accounts, telemetry, uploads, cloud licensing/update agents or embedded AI without a separate decision. No database, web frontend, GPU, generic plugin suite, repository move or changes to other products.

## 4. Smallest useful first milestone

**M1 proposal: decision-ready core behavior and one bounded experiment design.** Outcome: the owner understands the first echoes, channel movement and time-change behavior, and an implementer knows the precise unresolved question and evidence needed. M1 contains documentation/design only, not a playable plugin.

**Only next proposed assignment, not authorized:** create a bounded documentation/design task and `records/DESIGN-001.md`; reconcile MASTER_SPEC/DECISIONS/TODO/PROJECT_STATE without changing governing workflow or the brief. One coordinator owns records. Scope:

1. Explain pre/post-character tap and stereo/ping-pong injection with first-three-echo examples for centered, L/R-only and stereo input.
2. Propose explicit timing-change policies for manual edits, host automation, tempo changes and interruption, with sonic/failure tradeoffs.
3. Propose compact timing/feedback/routing/mix semantics and limit rationale without freezing algorithms, serialized parameter IDs or compatibility promises.
4. Draft one timing/routing experiment contract with controlled fixtures, independent expected observables, candidate-selection criteria, evidence custody and stop conditions. Do not execute it.
5. Identify remaining separate prerequisites: nonlinear characterization, host/state/latency/bypass contracts, toolchain/dependency selection and release-quality budgets. Do not automatically begin them.

| Proposed M1 acceptance criterion | Planned verification / evidence |
| --- | --- |
| Every requirement/direction has attributable source; advice remains labeled. | Source-to-contract trace and document authority check. |
| First-repeat/routing/time-change alternatives make sonic differences and failure modes visible. | Technical reasoning review of diagrams and independent first-echo oracles; no framework-default semantics. |
| Experiment design identifies controlled inputs/envelope, block partitions, observables, independent oracle, predeclared criteria and negative/inconclusive handling. | Reproducibility and test-design review; no result-derived threshold disguised as predeclared. |
| Every open contract names blocked dependent work and minimum resolving evidence/owner choice. | Finding/decision/prerequisite trace in the single TODO ledger. |
| Identifiable combined documents are consistent, originals preserved and applicable review complete. | Coordinator checks; real non-authoring technical review; then fresh non-authoring readiness advice distinct from technical reviewer; separate owner acceptance. |

Runtime tests are not applicable to M1. No empirical PASS is possible from document review alone. Approval of this plan does not accept the future milestone or authorize all its successors; record the exact bounded task authorized by the owner.

**First audible milestone, conditional and separately authorized:** after accepted prerequisite behavior, necessary bounded experiments and build authorization, demonstrate a reproducible FL Studio VST3 with a temporary functional editor, defined clean stereo delay, feedback/wet-dry, evidenced timing and basic state recall. Only accepted semantics are included. This internal milestone is not a character-delay release or final UI acceptance.

Indicative later outcomes, not scheduled/authorized tasks: validated core and host contracts → playable core → repeat tone/ducking → separately validated optional character/motion → complete automation/state/original UI/sounds → full release candidate evidence and owner disposition. Each needs its own bounded authority; a failed experiment may change the sequence only through an actual decision.

## 5. Planned acceptance/tests and requirement trace

| Intent | Proposed later acceptance evidence |
| --- | --- |
| REQ-01 / REQ-05 | Accepted compact feature envelope; deterministic signal/routing/decay tests, lifecycle and real-time evidence, complete technical review. A narrow core pass does not establish production quality. |
| REQ-02 | Named Windows/CPU/FL Studio/toolchain matrix; VST3 validation plus actual scan/instantiate, insert/send, playback/offline render, automation, bypass, transport, editor reopen, project reopen and multiple-instance evidence. [Image-Line manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/basics_externalplugins.htm) documents VST3 hosting; actual CHROMAVE integration is untested. |
| REQ-03 / sonic direction | Owner listening review of rhythmic pluck, lead darkening tail, vocal clarity and pad movement if included; permitted fixtures, matched levels, settings/session provenance and unfavorable results retained. |
| REQ-04 | Documented capability/value/risk decisions and deferrals; no feature-parity test. |
| REQ-06 | Public reference notes and original implementation/design/assets/presets provenance. [BABY Audio public page](https://babyaud.io/comeback-kid-delay-plugin) supplies functional categories; infer no proprietary routing or exclusivity. |
| REQ-07 | Accepted contracts before dependent production; experimental artifacts distinguished from production and reviewed before reuse. |
| REQ-08 / REQ-09 | Requirements/decision/task/finding/evidence trace, qualified limitations, distinct reviewer/readiness roles and owner decisions; real checkpoint evidence when Git exists. |
| Stack direction | Reviewed pinned toolchain/dependencies and repeatable build, without current version/license selection. |
| Visual direction | Original readable cyberpunk editor at agreed scaling/input/accessibility scope; visual reference images do not prove DSP/automation/recall. |

Later planned tests: impulse and fractional magnitude/phase response; repeated circulation and spectral decay; abrupt/interrupted time changes and high-feedback interaction; mono/centered/stereo/L/R-only routing and fold-down; finite output/internal state, extreme permitted settings, silence-after-excitation and repeated reset; malformed state/schema compatibility; sample-rate and block-partition comparisons; allocation/locking audit and named-hardware performance; independent plugin-format validation, FL Studio integration and controlled listening.

Exploratory 44.1/48/96 kHz and small/large/irregular blocks are recommended candidate conditions, not a supported-configuration promise. Numeric tolerances, input envelope, CPU/memory/multi-instance budgets, automation granularity, latency/tail/bypass/tempo/reset behavior and listening criteria remain unset. Declare criteria before measurements where feasible; exploratory/post-result criteria must be labeled. No tests, measurements, benchmarks or listening sessions were performed here.

## 6. Assumptions, risks and unresolved owner choices

**Assumptions requiring verification:** suitable Windows compiler/SDK and FL Studio access; JUCE suits accepted behavior; compact controls achieve genre usefulness; optional saturation/motion justifies its cost; agreed multi-instance budget can be met. None is an established application fact.

| Risk / uncertainty | Proposed mitigation and retained limitation |
| --- | --- |
| Nonlinear/time-varying feedback and time-change transient gain | Define full round trip and envelope; independently characterize long renders/retargets. Feedback below 100% or output clamping alone is not proof of intended decay. |
| First echo / centered ping-pong ambiguity | Explicit first-three-echo oracles and user-visible policies before dependent code. |
| State/automation incompatibility and real-time handoff | Accepted parameter/schema/lifecycle contracts; malformed-state/recall/thread-path review and host evidence. |
| Aliasing/latency/performance cost | Conditional inclusion and measured tradeoffs on named builds/hardware. |
| Loudness bias or weak genre identity | Matched-level permitted listening material and separate owner musical acceptance. |
| Feature expansion or unreadable aesthetics | Compact scope, conditional modules and usability criteria before art/presets. |
| Unsupported host/build/dependency obligations | Exact environment/version decisions and applicable due diligence; no legal conclusion or universal-host claim. |
| Missing checkpoint/template provenance | F-004/F-005 preserve limitations; no fabricated Git equality or upstream identity. |

Actionable follow-ups and closure evidence live in TODO F-002/F-003, with F-004/F-005 handling checkpoint/provenance. Writing options does not close any unresolved contract or demonstrate corrective effectiveness.

**Decisions needed from the Product Owner (all unresolved):**

- Whether this compact V1 direction and recursive tone as the initial repeat-evolution baseline fit the intended product, with saturation/motion conditional and no silent reduced-release acceptance.
- Whether M1 documentation/design, with the exact scope/exclusions in section 4, is the next authorized task. Implementation and experiment execution remain excluded.
- Within that task, preferred first-repeat coloration, centered-source ping-pong behavior and time-change feel after understandable alternatives are presented.
- Later, exact support/performance commitments and final UI/preset/release envelope. These are not prerequisites to presenting or approving the current proposal.

Engineering research should establish feasibility/facts rather than ask the owner to select interpolation from memory. No answer is inferred from silence or a technical PASS.

## 7. Contributor strategy and stop

Current: one coordinator/shared-record writer and one real read-only Planning & Readiness author; no recursive delegation or concurrent source writers. This planning proposal is not an implementation milestone and has not received independent technical review or fresh post-implementation readiness.

For a later authorized M1: coordinator/document author, bounded read-only technical reviewer, then a fresh non-authoring readiness contributor distinct from that reviewer. For code: one writer until separate workspaces/ownership and controlled integration are actually verified. Add DSP/QA expertise only for bounded risks; account for partial/failed outputs and ensure no active contributor remains at completion. No fixed permanent roster.

No successor task, scaffold, dependency install, experiment, application code/test, acceptance, GitHub creation, release or publication is authorized by this proposal.

**Only next action now: Product Owner disposition of PLAN-001 and explicit authorization of any next bounded work. State: `PLAN_AWAITING_PRODUCT_OWNER_AUTHORIZATION`.**
