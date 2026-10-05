# CHROMAVE — Application Definition & Product Brief

**Working product name:** CHROMAVE  
**Product descriptor:** Character Delay  
**Document revision:** 1 — preparation draft  
**Intended companion:** `CLEAN_TEMPLATE_EXPORT.md` from the Application Building Template project  
**Document purpose:** Self-contained application intent for project-specific planning and controlled adaptation  
**Authority:** Product-owner requirements are attributed below; recommendations remain proposals. This document is not an accepted DSP specification, implementation authorization, release approval, or replacement for an existing repository.

> Build an original, production-quality stereo character-delay VST3 for Windows 11 and FL Studio. Give producers musically useful synthwave-oriented echoes, an efficient interface, and a carefully engineered path toward repeats that evolve as they circulate.

---

## 1. How to use this document with the template

`CLEAN_TEMPLATE_EXPORT.md` supplies the reusable development process. This document supplies **what CHROMAVE should become, why it should exist, what has been discussed, and what still needs resolution**. Neither document alone establishes permission to implement the application.

The requested application is an audio plugin with an actual usable interface inside a DAW. It is not the Application Building Template itself, a project-management dashboard, a website, a documentation generator, or a self-improving AI system. Do not implement CHROMAVE features in the template-development repository.

### 1.1 Existing-project protection

CHROMAVE has prior product/research discussions and an approved historical documentation-initialization checkpoint. Do not assume that it is now a completely empty project or that it must restart Stage 0. Equally, do not assume that the approved initialization task was executed or that subsequent experiments passed.

At adaptation time, inspect the actual CHROMAVE repository in this order:

1. `AGENTS.md`.
2. `PROJECT_STATE.md`.
3. Authoritative product, architecture, DSP, and testing documents referenced there.
4. Relevant roadmap, decisions, and findings.
5. Relevant experimental evidence, implementation, and tests.
6. Actual Git/PR state.

Use the smallest relevant read set after startup. Existing accepted repository records govern project state. If sources conflict, stop the affected planning or mutation, identify the exact conflict, and obtain a documented resolution. Do not overwrite existing instructions with the template's empty starter state.

**Preparation limitation:** Connected GitHub searches and the accessible repository listing did not locate CHROMAVE during preparation of this brief. Its current branch, accepted commit, implementation status, and completed gates were therefore not verified. An unavailable repository is not evidence that no repository exists. Historical discussion is preserved below as context, not asserted as current repository truth.

### 1.2 Template identity and acceptance context

The Application Building Template's retrieved repository state identifies the following accepted reusable v1.0 basis:

| Field | Identified value |
| --- | --- |
| Export identifier | `TEMPLATE-EXPORT-SOURCE-BUNDLE-001` |
| Source content revision | `6a15bc12c2721b9bf39bf4bd725c35f1887edc2e` |
| Export path in template project | `records/evidence/task-025/CLEAN_TEMPLATE_EXPORT.md` |
| Recorded export SHA-256 | `7AA754C1DBA8DC454BFC022F20E4D8A7CBE5F4A39CC43B051F8B224D90DDAB76` |
| Recorded export size | 22,581 bytes |
| Acceptance record | D-047: exact unchanged Candidate 2 source/export accepted as the bounded reusable v1.0 basis |

The export's historical header still describes Candidate 2 and release status `NONE`; the later acceptance record explicitly preserves those original bytes. Do not rewrite the export merely to update that header, and do not treat its neutral startup fields as a declaration that CHROMAVE has no existing work. Verify the actual companion file's identity when it is supplied. A different hash requires version reconciliation, not an automatic assertion of equivalence. [P4]

Keep template acceptance separate from CHROMAVE acceptance. No Application Building Template tasks, findings, permissions, or product-release claims transfer into CHROMAVE.

### 1.3 Roles and process boundaries

Will is the product owner. The established CHROMAVE arrangement has ChatGPT advising on research, architecture, requirements, experimental design, implementation review, and milestone readiness; Codex implements authorized documentation, experiments, tests, and production work.

The inspected export also routes substantive planning to ChatGPT. Do not silently replace that arrangement with autonomous Codex planning, invented review agents, or a different approval model. Any later owner-approved process adaptation must be reconciled explicitly with the selected export and existing CHROMAVE instructions. Use real available contributors when valuable; do not claim delegation, isolation, review, or model changes that were not performed.

Before substantial research or consequential review, state the recommended model and effort using options actually available at that time. Keep ChatGPT and Codex recommendations separate. Historical model names are not technical dependencies and are intentionally not hard-coded here.

---

## 2. Confidence and authority vocabulary

| Label | Meaning in this brief |
| --- | --- |
| **PRODUCT-OWNER REQUIREMENT** | Explicit user intent or constraint supported by the supplied project discussions. Approval of an implementation is separate. |
| **FACT** | A source-backed technical statement or directly observed record. A framework capability is not proof of CHROMAVE behavior. |
| **FROZEN CONTRACT** | An engineering choice explicitly accepted in the governing repository, with scope and provenance. This brief creates none. |
| **PROVISIONAL ENGINEERING DIRECTION** | A recommended approach that may change after research, testing, or owner review. |
| **ASSUMPTION REQUIRING EXPERIMENT** | A hypothesis whose suitability must be demonstrated. |
| **UNRESOLVED** | A decision, requirement detail, or evidence gap not settled by the available material. |

Unless expressly attributed as a product-owner requirement or supported fact, feature behavior, UX refinements, release criteria, and sequencing below are **proposals for review**. “Should” expresses a recommendation; it does not create a frozen contract. Requirement labels in this brief are local traceability labels, not parameter IDs, existing issue IDs, or authorization records.

---

## 3. Product objective and requirements

### 3.1 Product thesis

**PROVISIONAL ENGINEERING DIRECTION**

CHROMAVE should make it easy to create musical echoes that range from clean and rhythmically precise to dark, saturated, gently unstable, and atmospheric. Its distinguishing emphasis should be **controlled repeat evolution**, not the largest possible number of effects.

The plugin should perform three jobs well: establish the rhythm of the echoes, shape their character, and place them behind or around the source without making the mix unnecessarily muddy or difficult to manage.

### 3.2 Explicit product-owner requirements

| ID | Requirement | Scope qualification |
| --- | --- | --- |
| REQ-01 | Create an original, production-quality **stereo character-delay effect** named CHROMAVE. | Working identity; no trademark-clearance claim is made. |
| REQ-02 | Initial target: **Windows 11, 64-bit, VST3, FL Studio**. | Exact supported host builds, CPU architectures, and test matrix remain to be specified. |
| REQ-03 | Make the effect particularly useful for **synthwave, dark synthwave, retrowave, and cyberpunk** production while retaining general-purpose usefulness. | Genre relevance is a product outcome, not merely a visual theme. |
| REQ-04 | Consider the useful, familiar effect categories that support that music. | This does not approve every effect for V1 or require Comeback Kid feature parity. |
| REQ-05 | Prefer **fewer excellent DSP modules** over a large collection of mediocre features. | A narrow release must still be musically useful, not merely a technical demonstration. |
| REQ-06 | Study Comeback Kid as a public behavioral/product-design reference, but implement CHROMAVE independently. | No proprietary code, decompilation, presets, assets, branding, distinctive interface copying, or proprietary resources. |
| REQ-07 | Resolve consequential DSP contracts before dependent production implementation. | Research and separately authorized experiments may precede production code. |
| REQ-08 | Preserve project knowledge incrementally in repository documentation. | Conversation alone must not hold accepted architecture or current project state. |
| REQ-09 | Use reviewable, bounded tasks with testing and explicit review/acceptance gates. | No blanket authorization for all milestones. |

**Owner-provided technical expectation:** modern C++, JUCE, CMake, VST3, Git, and GitHub. The expectation is not a selected dependency version, a licensing conclusion, or permission to scaffold production code. [P1]

**Owner-provided sonic direction:** “the echoes evolve as they repeat.” This is the leading long-term identity; its precise V1 commitment still needs explicit scope acceptance. [P1]

**Owner-provided visual direction:** an original cyberpunk-themed interface. Detailed layout and reference-image work were intentionally deferred until the capability/control surface becomes clearer. The theme should guide later design, not determine the DSP or add unapproved controls. [P3]

### 3.3 What success should feel like

A producer inserts CHROMAVE, selects a timing relationship, sets repeat length and tone, and gets a useful musical result without assembling a complicated external chain. Deeper settings provide purposeful transformation rather than unexplained loudness changes or fragile behavior. Saving the DAW project preserves the intended settings, and returning to the song does not require rebuilding the sound.

These are proposed experience goals to turn into demonstrable acceptance scenarios, not measured claims about an existing build.

---

## 4. Users and musical use cases

The primary user is a producer or sound designer working in FL Studio with synth leads, arpeggios, plucks, pads, vocals, guitars, drums, and atmospheric source material. The product should be approachable without requiring knowledge of interpolation, feedback matrices, or oversampling.

| Scenario | Desired result | Relevant candidate capabilities | Initial scope position |
| --- | --- | --- | --- |
| Synth lead behind the melody | Repeats fill the spaces without masking new notes. | Tempo sync, filtering, feedback, ducking. | First-release target. |
| Rhythmic arpeggio or pluck | Echoes create a deliberate interlocking rhythm. | Straight/dotted/triplet timing, stereo or ping-pong. | First-release target. |
| Dark cyberpunk echo | Repeats grow more restricted in bandwidth and deliberately colored. | Recursive filtering and validated saturation. | Character target; saturation is evidence-dependent. |
| Vocal or guitar space | A useful slapback or longer trail remains controlled in the mix. | Free timing, mix control, filtering, ducking. | First-release target. |
| Atmospheric synth tail | A sustained source develops gentle motion and depth. | Modulated delay reads, stereo behavior; later diffusion or drift. | Basic motion first; extended texture later. |
| Drum accents or percussion | Selected hits gain rhythmic repeats without uncontrolled low-end buildup. | Timing, feedback filtering, wet/dry; later transient shaping. | Core behavior first. |
| Retro degraded repeats | Echoes acquire a deliberately worn digital texture. | Future bit/sample-rate degradation and controlled drift. | Extension candidate, not V1 promise. |
| Mix send/return | A fully wet return can be blended using the DAW mixer. | Reliable wet-only output, level management, defined tail behavior. | Recommended workflow for V1 review. |

These scenarios specify desired outcomes. They do not assert market-share rankings for “popular” effects or guarantee a match to any named recording. Sonic references should later be translated into observable qualities rather than copied presets.

---

## 5. Relationship to BABY Audio Comeback Kid

**FACT:** BABY Audio publicly lists free and synchronized delay timing, ping-pong, ducking, low/high cuts, transient shaping, tape-style saturation, vintage-digital coloration, phasing, diffusion/reverb, timing-based width, pitch-based richness, panning, mono output, and subtle randomization. [T1]

The useful lesson is that producers benefit from shaping their echoes within the delay instrument itself. CHROMAVE may cover overlapping functional categories through original implementations.

Do not describe the goal as “rebuild Comeback Kid now and add every remaining control later.” Evaluate each capability on its musical value, interaction with the existing delay, engineering risk, interface cost, and testability.

Do not claim that recursive coloration is unique to CHROMAVE, or infer that Comeback Kid lacks it. A public feature list does not establish a competitor's complete internal routing. CHROMAVE's differentiation should be its chosen sound, repeat-evolution behavior, usability, and implementation quality—not an unsupported exclusivity claim.

---

## 6. Recommended first-release scope

**Status: PROVISIONAL ENGINEERING DIRECTION.** This is a V1 proposal for review, not an approved feature freeze. Build the reliable core first; do not advertise a complete character-delay release until its accepted musical outcomes and quality gates are met.

| Capability | Intended behavior | Important unresolved detail |
| --- | --- | --- |
| Free timing | Choose delay time directly using a meaningful time display. | Minimum/maximum time, mapping, precision, transition behavior. |
| Host tempo synchronization | Select musical note relationships rather than calculating milliseconds. | Tempo fallback, supported divisions, out-of-range policy. |
| Straight/dotted/triplet timing | Provide useful rhythmic alternatives. | Exact division set and representation. |
| Feedback | Control repeat persistence predictably. | Maximum gain, nonlinear interactions, near-unity policy. |
| Wet/dry mix | Blend the original signal with processed repeats; support a clear wet-only setting. | Mix law, gain staging, dry-path latency policy. |
| Stereo operation | Process stereo source material without accidental collapse or channel loss. | Linked timing, mono input support, channel behavior. |
| Ping-pong | Produce a defined alternating stereo echo behavior. | Input injection, first echo side, routing and mode transitions. |
| Feedback HP/LP filtering | Shape low- and high-frequency content as repeats circulate. | Topology, cutoff range, bypass, order, smoothing. |
| Ducking | Reduce audible echoes during source activity and recover afterward. | Detector linking, law, attack/release, exposed controls. |
| Character saturation | Add a musically useful nonlinear color to repeats. | Candidate only until aliasing, loop behavior, CPU, and latency are acceptable. |
| Controlled modulation | Introduce restrained pitch/timing movement through the delay. | Candidate only until depth/rate limits, interpolation, and stereo behavior are validated. |
| State recall | Restore accepted settings reliably in saved host projects. | Parameter model, schema, migration, reset and tail policy. |
| Usable native plugin interface | Provide clear controls and status, ultimately with the original cyberpunk visual direction. | Exact control surface, dimensions, scaling and interaction specification. |
| Original presets | Demonstrate the accepted sound palette and provide practical starting points. | Recommended for release; count, file format, browser scope and user-preset workflow remain open. |

A clean delay with filters and ducking is a valuable developmental milestone. It is not automatically sufficient to satisfy the final character/synthwave product objective. Conversely, an experimental saturation or modulation module should not be included merely to make the feature list look complete.

At the V1 gate, the owner should choose among a validated compact character release, an explicitly reduced release definition, or additional bounded experimentation. A feature removal that materially weakens the product thesis requires an explicit decision.

---

## 7. Extended synthwave capability backlog

**Status: future candidates only.** Preserve these ideas without assigning release dates, guaranteed version numbers, or implementation authorization. “Deferred” means retained for reevaluation, not promised.

| Candidate | Musical objective | Main design question | Revisit condition |
| --- | --- | --- | --- |
| Wow/flutter or controlled drift | Gently unstable, worn echoes. | Random/deterministic behavior, rates, depth bounds, interaction with sync. | Basic modulation is proven and additional instability has clear value. |
| Dedicated chorus/detuned repeats | Richer stereo movement than simple read modulation alone. | Topology, mono behavior, level, extra delay state. | A concrete use case cannot be served adequately by the existing core. |
| Stereo width/spatial motion | Place repeats more widely or move them deliberately. | Post-loop versus recursive placement, mono loss, gain behavior. | Baseline stereo/ping-pong is accepted and limitations are demonstrated. |
| Lo-fi/vintage-digital degradation | Crunchy or progressively eroded echoes. | Quantization, resampling, noise, loop persistence and controllability. | Separate controlled experiments establish a useful, stable sound. |
| Diffusion/space | Smear distinct repeats toward a denser atmospheric tail. | Density, metallic artifacts, memory/CPU, loop placement. | The delay is mature enough for a separate diffusion substage. |
| Transient shaping | Soften attacks or emphasize sustain in rhythmic repeats. | Detection, pumping, relationship to ducking and feedback. | Listening tests demonstrate a gap in the current shaping tools. |
| Pitch-shifted repeats | Controlled harmonic movement through successive echoes. | Pitch algorithm, latency, feedback behavior, clarity and CPU. | A specific musical objective justifies a substantial new subsystem. |
| Humanization/random timing | Less mechanically identical repetitions. | Reproducibility, bounded variation and rhythmic predictability. | Drift/modulation foundations and determinism policy are established. |
| Expressive self-oscillation | Intentional sustained feedback performance behavior. | Excitation, output management, stopping behavior and usable bounds. | Product owner explicitly requests it and dedicated safety/behavior tests pass. |
| Multi-tap architecture | Multiple independently shaped rhythmic echoes. | Interface complexity and departure from the compact product. | Explicit product expansion, not generic future-proofing. |

Saturation does not automatically constitute a full tape-machine model. Basic delay modulation is not automatically a dedicated chorus. Diffusion is not automatically a full reverb. State these distinctions honestly in the eventual product documentation.

---

## 8. Sound identity and listening targets

**PROVISIONAL ENGINEERING DIRECTION**

The desired palette includes precise rhythmic repeats, progressively darker echoes, restrained analog-like color, subtle pitch motion, useful stereo movement, and tails that remain manageable behind the original source.

Repeat evolution is a behavioral concept: selected processing is encountered again as audio circulates. It does not require every repeat to become monotonically more distorted, wider, louder, or less stable. Those outcomes depend on levels, routing, modulation, and processing choices and require evaluation.

Illustrative listening targets—not final preset names or parameter settings—are:

| Target | Description | Scope |
| --- | --- | --- |
| Clean rhythmic echo | Precise repetitions with deliberate stereo behavior and minimal added color. | Core baseline. |
| Darkening trail | A lead or pluck loses excess low/high content progressively without becoming unusably thin too quickly. | Feedback-filter evaluation. |
| Colored lead tail | Repeats gain audible character while the original remains intelligible. | Saturation-dependent. |
| Moving pad echo | Gentle modulation produces depth without involuntary extreme pitch sweeps. | Modulation-dependent. |
| Ducking vocal repeat | A phrase remains forward; its trail becomes audible in the gaps. | Ducker evaluation. |
| Worn digital atmosphere | Degraded, unstable, potentially diffuse echoes. | Later extension; not required of the initial core. |

Listening should compare alternatives at matched perceived level where practical. A louder setting is not automatically a better character model. Use original, licensed, or otherwise permitted test material and record enough session detail to repeat a comparison.

---

## 9. Candidate control surface

The following are **semantic controls**, not approved parameter IDs or final knob counts.

| Group | Candidate controls | Design aim |
| --- | --- | --- |
| Time | Free/Sync, Time or Division, rhythmic modifier | Make the timing relationship visible and predictable. |
| Repeats | Feedback | Make persistence easy to hear and understand. |
| Routing | Stereo/Ping-Pong | Make channel behavior explicit. |
| Tone | Low Cut, High Cut | Shape repeat bandwidth without hiding the loop behavior. |
| Character | Drive/Character, only if accepted | Add useful coloration without a misleading tape-emulation claim. |
| Motion | Rate and Depth, only if accepted | Provide controlled movement with useful ranges. |
| Clarity | Duck amount; additional envelope controls only if justified | Keep the original forward without overloading the interface. |
| Mix | Wet/Dry; output trim if justified | Support inserts, returns, and level comparison. |
| Presets | Selection, initialization, user save/load if approved | Make sounds reusable without building a large content platform. |

Do not derive serialized IDs directly from these display labels without a reviewed parameter contract. Do not add nonfunctional knobs for deferred features. Decide reset values, units, normalization, discrete transitions, automation eligibility, and preset behavior before committing the control surface to released sessions.

---

## 10. Interface and interaction direction

**Owner-provided direction:** original cyberpunk theme. **Implementation and usability recommendations:** subject to review.

The finished plugin should look like a professional audio tool rather than a game interface or a miniature web dashboard. A dark surface, restrained luminous accents, crisp labels, readable values, and clearly grouped controls are plausible interpretations. Color choices, illustrations, materials, typography, and animation remain unfrozen.

Timing, feedback, and mix deserve visual priority. Character, tone, motion, and ducking should be discoverable without overwhelming the main workflow. The visible distinction between core timing and optional coloration should help explain what a control does.

Recommended interactions include fine adjustment, direct value entry where useful, reset-to-default, clear selected modes, meaningful units, tooltips, and an evident modified-preset state. UI scaling and keyboard/accessibility behavior need an explicit test scope. Do not claim those affordances are already implemented.

### 10.1 Early usability without premature art direction

After the relevant production foundation is authorized, build the earliest useful **functional** control surface for listening and host testing. A plain or temporary editor is acceptable for that internal milestone. It is not the final visual deliverable.

Create detailed reference images and final design assets only after the meaningful controls and interaction states are understood. Reference images guide appearance; they cannot establish that DSP, automation, or state recall works. No image generation or GUI implementation is authorized by this brief.

### 10.2 Scope boundary

Do not add a waveform dashboard, animated cityscape, account screen, online store, preset marketplace, or multi-window rack merely because it matches the aesthetic. Add visualization only when it answers a concrete user question and fits the processing/UI budget.

---

## 11. Provisional DSP architecture

**Status: PROVISIONAL ENGINEERING DIRECTION reconstructed from the supplied proposal, not a verified current repository contract.**

The leading concept separates source preservation, recursive character, and output mix management. A candidate signal flow is:

```text
Original input ----------------------------------> dry gain ---------+
       |                                                             |
       +--> detector -------------------+                            |
       |                                |                            v
       v                                v                          mix --> output
input mapping --> SUM --> delay reads --> character --> wet ducker --> wet gain
                   ^                         |
                   |                         v
                   +---- feedback gain <-- stereo feedback routing
```

“Character” represents candidate HP/LP filtering and, only if validated, saturation. Their exact order remains unresolved. Modulation would primarily control the delay reads rather than necessarily add a separate chorus processor. The detector reads the source; its gain acts on the audible wet branch, not on the candidate recursive state.

### 11.1 Delay storage and reads

Preallocated circular storage with fractional read capability is the leading direction. JUCE exposes fractional, sample-by-sample and multi-tap-oriented delay operations, and warns that resizing its maximum delay storage may allocate and must not occur on the audio thread. This supports evaluating its infrastructure; it does not select it automatically. [T2]

Linear and third-order Lagrange are useful comparison candidates. JUCE documents a low-pass effect for linear interpolation, reduced coloration with Lagrange at increased cost, and state-related limitations for rapidly modulated first-order Thiran interpolation. Lagrange was previously favored, not validated as CHROMAVE's final choice. [T3] [T4] [T5]

### 11.2 Timing transitions

The earlier design proposal distinguishes intentional continuous delay movement from selecting a different delay target. Moving reads and dual-read crossfades should remain alternatives or components of an explicitly designed transition system, not automatically selected based on the apparent shape of automation.

**Important unresolved point:** a sequence of numeric host updates does not by itself establish whether the producer intended a discrete edit or continuous modulation. Define the product policy, event handling, interrupted-transition behavior, and same-sample ordering. Do not rely on an undocumented heuristic to guess intent.

### 11.3 Feedback character and first-repeat placement

Filtered feedback can produce frequency-dependent decay. Established filtered-feedback models also make clear why the complete round-trip path matters, not only the feedback knob. [T6]

The sketch above taps the audible signal **after** the character chain. Under that candidate topology, the first audible repeat encounters the chain once and subsequent circulations encounter it again. Earlier discussion also considered a pre-character output tap. These are different behaviors; the exact wet-tap position, input injection, and character ordering must be reconciled and accepted before implementation depends on them.

Do not treat a scalar feedback setting below 100% as a complete proof for a nonlinear, time-varying stereo loop. Character gain, interpolation, routing, transitions, and modulation all belong in the analysis and tests. Output clamping alone is not an acceptable demonstration of intended decay or musical stability.

### 11.4 Saturation and anti-aliasing

Recursive saturation is an experiment-dependent candidate. Select it for its sound and controllability, not as a substitute for understanding feedback behavior. JUCE's oversampling documentation describes nonlinear aliasing mitigation together with filter, phase, and latency tradeoffs. No oversampling factor is selected here. [T7]

Measure both audible artifacts and internal timing implications. Distinguish algorithmic processing latency from the deliberate musical echo time. A zero-latency marketing promise or a blanket oversampling choice would be premature.

### 11.5 Stereo and ping-pong

A channel-swap feedback matrix is a candidate routing component, not a complete ping-pong specification. Define source injection, channel linking, the first audible side, and behavior for centered/identical-channel material. Simply swapping equal left/right signals does not create audible alternation; this follows directly from swapping two equal values.

Test mono source, stereo source, left-only/right-only input, identical channels, and mono fold-down. A stereo-width control, if later added, must separately specify whether it changes the recursive state or only the output.

### 11.6 Ducking

The current proposal places conventional ducking after the feedback split so it changes the audibility of the wet signal rather than directly changing the stored tail. A stereo-linked detector is a candidate, not a frozen choice. Detector law, envelope timing, gain smoothing, and sidechain scope require review.

An external sidechain is not part of the current approved scope. Internal input-driven ducking is the simpler candidate to evaluate first.

---

## 12. Architectural decisions that remain open

Do not resolve these by silently copying a framework default or a competitor's visible range.

| Decision area | What must be specified | Evidence or review needed |
| --- | --- | --- |
| Delay limits | Minimum/maximum time, guard samples, behavior at limits. | Product needs, memory calculation, boundary tests. |
| Fractional delay | Algorithm, indexing, supported fractional positions and modulation range. | Response, timing, modulation and CPU measurements. |
| Time changes | Free/sync transitions, repitch/crossfade policy, retargeting. | Stress signals, repeated edits, listening under feedback. |
| Tempo behavior | Missing/invalid tempo, changing BPM, transport discontinuities, out-of-range durations. | Current host/framework research and FL Studio tests. |
| Feedback | Gain law, maximum, decay semantics, boundedness and self-oscillation policy. | Linear analysis, nonlinear renders, product decision. |
| Character chain | Wet tap, filter order, saturation position, bypass and gain staging. | Controlled comparisons and loop interaction tests. |
| Stereo | Input/output layouts, injection, ping-pong, channel linkage and mono behavior. | Routing oracles and host layout validation. |
| Parameters | IDs, ranges, defaults, units, smoothing, discrete transition rules and event timing. | Contract review before automation/preset compatibility commitments. |
| State | Schema, compatibility, invalid input, thread handoff and tail restoration. | Serialization and host recall tests. |
| Latency/tails/bypass | What latency is reported; what bypass, stop, reset and offline rendering do. | Signal timing and actual host behavior. |
| Randomness | Whether randomness exists; seed, reset and repeatability policy. | Only required if an accepted feature uses randomness. |
| Dependencies | Framework/toolchain versions, licenses, updates and build reproducibility. | Version-specific due diligence and repeatable build evidence. |
| Performance | Reference hardware, sample rates, block sizes and multi-instance budget. | Measured release-build results; no invented benchmark. |

A downstream milestone may begin only when the contracts it relies on are sufficiently resolved. Independent research can be sequenced sensibly, but it must not accumulate across multiple major substages without a documentation checkpoint.

---

## 13. Quality, host integration, and real-time requirements

These are proposed engineering acceptance obligations implementing the owner's production-quality objective. They still require an accepted test scope and, where applicable, numeric thresholds.

### 13.1 Real-time processing

Audio processing should perform bounded work without dynamic allocation/deallocation, blocking locks, file/network access, UI work, or unbounded operations on the processing path. Preallocate required storage at a safe lifecycle boundary. Define how control/state updates reach the processor without making the callback wait.

“Thread-safe” is not equivalent to “real-time-safe.” For example, JUCE documents `AudioProcessorValueTreeState::copyState()` and `replaceState()` as using locks and not suitable for the audio-processing code. The framework is a candidate; using it does not automatically solve the project's state handoff. [T8]

Test finite samples and bounded internal behavior over the supported operating envelope, including silence after excitation, very low levels, repeated resets, extreme permitted settings, and malformed state. Define the actual fault policy before using sanitization, clearing, or limiting as a recovery mechanism.

### 13.2 Host behavior

FL Studio is the primary acceptance host. Recommended scenarios include scanning and instantiation, insert and send use, playback and offline rendering, tempo automation, parameter automation, preset/state recall, bypass, transport changes, editor close/reopen, project reopen, and multiple instances.

Do not advertise universal DAW compatibility from one host test. Distinguish VST3-format validation from FL Studio integration and from listening acceptance. Identify the host version and environment in each report.

### 13.3 Performance and compatibility

A reasonable initial experimental matrix is 44.1, 48, and 96 kHz, with small, large, and irregular processing blocks. These are proposed test conditions, not the final support statement. Define release support after checking architecture, resources, and actual host behavior.

Native Windows x64 is a likely first deployment target, but the owner specified 64-bit rather than a complete CPU-architecture matrix. Do not infer Windows ARM, macOS, Linux, VST2, AU, AAX, standalone operation, or 32-bit support.

### 13.4 Operational trust

Proposed default: keep audio processing local and do not require a cloud service. Do not add audio uploads, telemetry, account creation, licensing servers, update agents, or embedded AI inference without a separate product decision. AI-assisted development does not imply AI inference inside the plugin.

---

## 14. State, presets, and persistence

**PROVISIONAL ENGINEERING DIRECTION**

The released plugin should restore its accepted parameter state predictably. Preserve parameter identity across updates, version the state format where necessary, and define fallback behavior for missing, unknown, malformed, or out-of-range state fields.

Host project state and user presets may share a representation, but that is not decided. Preset support should begin with the smallest useful local workflow, not a marketplace, cloud library, or tagging platform. Factory examples must be original and exercise only supported capabilities.

An initialization state should be safe and understandable. Switching or loading presets should have a defined treatment of smoothing, latency, modulation phase, and existing delay contents.

**UNRESOLVED:** whether saving state captures only controls/configuration or also any audio tail; whether a restored session resets or reconstructs modulation phase; how preset changes treat active feedback; whether user presets require version migration. Do not silently serialize large delay buffers or promise sample-identical recall of a tail without such a contract.

---

## 15. Verification and experiment strategy

No experiment is represented as executed or accepted in this brief. Earlier analytical descriptions and illustrative calculations are not benchmark results. In particular, the previous interpolation attenuation example must not be reused as a validated JUCE measurement without reproducible derivation and implementation-specific checking.

### 15.1 Evidence discipline

Each experiment should identify one question, competing candidates, controlled inputs, parameter values, sample rates, block partitioning, build/environment, expected observables, acceptance or selection criteria, commands, raw outputs, and limitations.

Define criteria before comparing outcomes where feasible. Exploratory results can inform later thresholds, but thresholds chosen after seeing a result must be labeled as such. Preserve negative and inconclusive results. A graph is supporting evidence, not architecture approval.

Experimental code must remain distinguishable from production code. Reusing it in the plugin requires an explicit production review; it must not become the engine by inertia.

### 15.2 Delay-core experiments — historical Stage 0B2 intent

| Experiment | Evidence sought |
| --- | --- |
| Fractional timing and impulse response | Correct indexing and characterized fractional behavior; do not infer fractional delay from peak position alone. |
| Frequency response across fractional offsets | Magnitude/phase behavior across the tested bandwidth. |
| Repeated-feedback circulation | Accumulated spectral change and decay under controlled settings. |
| Moving-delay characterization | Intentional modulation behavior versus unwanted artifacts. |
| Step/transition comparison | Discontinuity, short-term level changes, temporal smearing and listening results. |
| Interrupted transition/automation stress | Defined behavior when new targets arrive before a transition finishes. |
| High-feedback transition interaction | No unexamined transient gain or unstable state from tap mixing. |
| Sample-rate/block partition comparison | Equivalent intended behavior within accepted tolerances. |
| CPU and memory measurement | Costs on named hardware/builds, including active transitions and modulation. |

### 15.3 Feedback and character experiments — historical Stage 0C2 intent

| Experiment | Evidence sought |
| --- | --- |
| Impulse decay and spectral decay | Feedback behavior agrees with accepted routing and filtering. |
| Character ordering | Controlled comparison of filtering and saturation order. |
| Nonlinear aliasing/level sweep | Character quality across signal frequencies, levels and supported sample rates. |
| Anti-aliasing comparison | Quality, latency and CPU tradeoff rather than a predetermined oversampling factor. |
| Long renders and silence-after-excitation | Finite outputs, intended decay/persistence, no unexplained sustained state. |
| Stereo routing tests | Expected first and successive echo channels for representative inputs. |
| Mono fold-down | Documented and acceptable consequences of stereo processing. |
| Ducker independence | Output attenuation does not directly rewrite the intended feedback history. |
| Combined automation | Tone, feedback, time, character and routing changes interact acceptably. |

### 15.4 Production verification layers

Use unit tests for local contracts, deterministic signal tests for DSP behavior, invariants for forbidden states, regression tests for accepted behavior, plugin validation for format/lifecycle issues, performance measurement, controlled listening, and FL Studio integration.

Recommended host acceptance scenarios include a short lead phrase with a tail, a rhythmic pluck with timing changes, a centered mono-derived source in ping-pong, a stereo pad under modulation, a vocal with ducking, a project save/reopen, and a multi-instance render.

For each accepted feature, maintain a trace from requirement or decision to test/evidence and remaining limitation. A test pass does not replace subjective product acceptance, and a pleasing demo does not replace numerical or host evidence.

---

## 16. Development sequence and gates

This section is a **planning outline**, not an authorized roadmap or declaration of current progress. Preserve any newer accepted repository sequence.

### 16.1 Research organization

| Substage | Purpose |
| --- | --- |
| Stage 0A | Product definition, user outcomes, behavioral references and success criteria. |
| Stage 0B1 | Delay-core design alternatives and candidate direction. |
| Stage 0B2 | Bounded delay-core experiments, split further by question. |
| Stage 0C1 | Feedback and character-topology alternatives. |
| Stage 0C2 | Feedback/nonlinear/stereo interaction experiments. |
| Stage 0D | Host, parameter, state, bypass and latency contracts. |
| Stage 0E | System-wide real-time safety and verification architecture. |
| Stage 0F | Accepted V1 feature cut, dependencies and small implementation milestones. |
| Stage 0G | Cross-document reconciliation and explicit Stage 0 acceptance. |

Substage numbering does not imply all evidence is available or that experiments must precede the definitions needed to conduct them. Where a test depends on an unresolved contract, first resolve that narrow dependency under an authorized task.

Preserve the CHROMAVE research checkpoint sequence:

**RESEARCH SUBSTAGE → REVIEW → DOCUMENT → CODEX UPDATE → VALIDATE → CHATGPT REVIEW → PASS → NEXT SUBSTAGE**

Accepted findings must be documented before the next major research unit. PASS remains distinct from owner approval where that approval is required.

### 16.2 Outcome-based implementation increments

After production prerequisites are accepted, subdivide work around demonstrable outcomes rather than feature-count targets. Likely increments include the reproducible plugin/test foundation; a minimal playable delay with a temporary functional editor; fractional timing; timing transitions and sync; feedback/stereo routing; feedback tone; conditional character and motion modules; ducking/mix behavior; complete state/automation integration; original UI/presets; and release validation.

Host and parameter contracts must be designed before implementation depends on them. A functional editor can support early listening once authorized; final visual polish does not need to block core experiments. Conversely, UI development must not introduce unreviewed DSP or state semantics.

Treat saturation and modulation as separate reviewable increments. Further split a risky subsystem when one task would otherwise mix algorithm selection, implementation, host integration, and product acceptance.

### 16.3 First-release completion proposal

A release should require the accepted feature set to work in the declared environment; core musical scenarios to pass listening review; mandatory signal, lifecycle, state and plugin checks to be evidenced; performance to meet the agreed budget; original UI and presets to meet their approved scope; installation/build documentation to match the actual artifact; and all release-blocking findings to be closed or explicitly dispositioned.

Record known limitations and supported configurations. Owner acceptance and release/publication permission remain separate. Additional effects require new scoped work after the first release; they are not silently activated by completion.

---

## 17. Technology and dependency strategy

**Expected foundation:** modern C++, JUCE, CMake, VST3, Git, GitHub. **Selection status:** version-specific choices remain open.

Recommended approach: prefer maintained framework infrastructure when it meets the accepted behavior; write custom DSP where evidence shows a need; keep testable signal-processing responsibilities separable from the editor and host adapter without building a speculative general framework.

Pin accepted versions and record toolchain/build configuration when implementation begins. Check framework/SDK licensing, redistribution obligations, third-party notices, asset permissions, and packaging requirements before a release decision. This brief makes no legal conclusion or pricing assumption.

Do not add a database, web frontend, authentication, cloud infrastructure, agent runtime, generic plugin suite, shared DSP framework, or GPU requirement to deliver this delay. A small offline analysis harness may use additional tools when explicitly approved; that does not make them production dependencies.

A relationship to a future synthwave-effects suite must not force a repository move, rename, monorepo, shared engine, or changes to other products. Preserve CHROMAVE's independence until a separately justified integration decision exists. [P5]

---

## 18. Repository knowledge and documentation ownership

The app brief is an adaptation input, not a second live project-state system. Once approved, distribute its accepted content into the repository's existing authoritative documents and retain this source as provenance where useful.

The earlier CHROMAVE checkpoint proposed `AGENTS.md`, `PROJECT_STATE.md`, `docs/PRODUCT.md`, `docs/DSP_ARCHITECTURE.md`, and `docs/TEST_STRATEGY.md`. The reusable export has its own five-file process core, including `MASTER_SPEC.md`, `TODO.md`, and `DECISIONS.md`. **These layouts must be reconciled, not blindly combined or overwritten.** [P2] [P4]

| Information | Single responsibility to preserve |
| --- | --- |
| Startup and working rules | An unambiguous entrypoint and explicit process authority. |
| Current project state | A concise index of current stage, gate, authorized work, evidence pointers, and exact next action. |
| Product requirements | One authoritative home for accepted goals, scope, use cases and non-goals. |
| DSP/architecture | Exact accepted contracts, provisional alternatives, assumptions, and rationale. |
| Tests/experiments | Methodology, criteria, evidence location and result status. |
| Findings | One continuous ledger, with stable identities, disposition and closure evidence. |
| Decisions/permissions | Actual decisions, approval provenance, effective scope and limitations. |

For a fresh adaptation, preserve the selected export's record boundaries unless the owner approves a documented change. For an existing CHROMAVE repository, propose the smallest mapping that retains its accepted authorities. A `MASTER_SPEC.md` and `docs/PRODUCT.md` must not maintain conflicting copies of the same requirements.

`PROJECT_STATE.md` should index current stage/substage, completed work with evidence, active gate, authorized implementation, frozen contracts, provisional direction, unresolved blockers/experiments, latest accepted Git/PR observation, and one exact next action. It should link to detailed records rather than duplicate them.

Do not create an empty document for every future feature. Add focused records when there is durable content to own. Do not close findings because they were documented or because a task summary says “complete.” Follow the selected template's checkpoint, final Git verification, and authorization rules; no commit, push, or release is authorized by this brief.

---

## 19. Historical research checkpoint — not current status

The supplied CHROMAVE conversation contains product-definition work, a full Pass B analytical response, and a Pass C topology response. Pass B was not absent or skipped. However, the later checkpoint explicitly separated analytical research from empirical validation.

| Historical item | What the supplied material establishes | What it does not establish |
| --- | --- | --- |
| Product definition / early Stage 0A | Product objective, target platform, differentiation and research questions were discussed. | Completion of every original product/reference research deliverable. |
| Stage 0B1 / Pass B | Circular delay, interpolation alternatives, transition candidates and experiment areas were documented in chat. | Executed implementation-specific measurements or a final interpolation decision. |
| Stage 0C1 / Pass C | Recursive character, filtering, saturation, stereo/ping-pong, modulation and ducking proposals were discussed. | Validated nonlinear behavior, final processor order or frozen topology. |
| Stage 0B2 and 0C2 | Experiments were planned; no executed results appear in the supplied conversation. | Their present repository status or proof they remain undone today. |
| Documentation initialization | The owner approved a bounded documentation-only initialization task. | Proof that Codex executed it, files passed review, or Git state was accepted. |
| Synthwave clarification | The owner emphasized that CHROMAVE should contain useful synthwave-related effects. | Approval of all candidate modules or a complete V1 freeze. |

The historical checkpoint had no frozen DSP contracts. The present repository may contain later decisions; inspect it before asserting that none exist now. Do not restart Stage 0B2 automatically or carry forward an old “next task” after a newer accepted gate.

Potential ambiguities carried forward include first-repeat character placement, automation transition policy, and saturation ordering. This brief does not treat an assistant's confident wording as acceptance evidence.

---

## 20. What the next planning session should produce

When the product owner supplies this brief and the identified export, the first response should be a bounded adaptation/reconciliation proposal—not a giant implementation prompt.

It should identify the supplied template version and authority, reconstruct available CHROMAVE repository state, map explicit requirements versus recommendations, reconcile documentation/process ownership, propose a compact V1 outcome definition and retained extension backlog, identify architecture blockers and necessary experiments, and recommend only the next eligible bounded task.

For a genuinely new and explicitly selected workspace, propose a documentation-first baseline without inherited acceptance. For an existing project, preserve accepted work and propose only the required migration or reconciliation. Missing prerequisites should block dependent mutation, not cause invention or destruction of project state.

Ask only questions that genuinely require an owner decision. Research or inspect engineering facts rather than asking the owner to choose an interpolation filter from memory. Explain consequential choices using the question, rationale, mechanism, alternatives, tradeoffs, failure modes, and evidence required.

**This document does not authorize production DSP, a plugin scaffold, Stage 0D research, a repository rewrite, a template modification, automatic task succession, or public release.**

---

## 21. Sources and provenance

### Project sources

**[P1] CHROMAVE product initialization and subsequent supplied discussion.** User product initialization of September 2026: product identity, platform, expected stack, originality boundaries, staged workflow, candidate effects and repeat-evolution direction. Later user clarification: synthwave relevance is important. These supply product intent, not current Git state.

**[P2] Approved Stage 0 checkpoint in the supplied conversation.** The user requested incremental repository preservation and approved the documentation-only checkpoint. It distinguished analytical Pass B/Pass C material from missing empirical evidence and proposed an initial five-document foundation. Approval of that task is historical and does not prove execution.

**[P3] CHROMAVE UI-reference discussion in the supplied Project context.** The user requested cyberpunk-themed interface references, then deferred that work until capabilities were sufficiently settled. This supports aesthetic direction, not a final layout or GUI authorization.

**[P4] Application Building Template artifacts inspected during preparation.** Library copy of `CLEAN_TEMPLATE_EXPORT.md`, especially its separate-application-definition/adaptation provisions; later D-047 acceptance records; live connected repository `drkmtr1/application-building-template`, `AGENTS.md` and `PROJECT_STATE.md`. The latter confirms acceptance of the unchanged exact export as the bounded reusable v1.0 basis. No current local/remote equality was tested here. Identity values in section 1.2 are recorded acceptance values; independently hash the actual supplied companion before relying on byte identity.

**[P5] Synthwave FX Suite Blueprint v1.1, sections 4.3, 20.5 and Appendix A.1.** Retrieved library text preserves CHROMAVE's separate repository, history and accepted lifecycle. This brief imports only that non-interference boundary, not other plugins' scope or authorizations.

### Technical reference anchors

These primary product/framework documents and recognized DSP text support the limited factual statements above. They are not substitutes for version-pinned implementation review or CHROMAVE measurements. URLs are reference locations, not installation instructions.

- **[T1] BABY Audio — Comeback Kid official product page.** Publicly documented behavior and feature categories; no inference about proprietary internal routing.
- **[T2] JUCE — `dsp::DelayLine`.** Fractional/sample-wise/multi-tap capabilities and allocation warning.
- **[T3] JUCE — Linear delay interpolation.** Documented coloration and intended usage.
- **[T4] JUCE — Third-order Lagrange delay interpolation.** Documented quality/cost/modulation tradeoff.
- **[T5] JUCE — First-order Thiran delay interpolation.** Stateful behavior and modulation caveat.
- **[T6] Julius O. Smith — Physical Audio Signal Processing, Filtered-Feedback Comb Filters.** Recursive filtering and loop behavior.
- **[T7] JUCE — `dsp::Oversampling`.** Nonlinear aliasing mitigation, filter tradeoffs and latency.
- **[T8] JUCE — `AudioProcessorValueTreeState`.** Parameter/state facilities and explicit real-time limitations of state copy/replacement.

[T1]: https://babyaud.io/comeback-kid-delay-plugin
[T2]: https://docs.juce.com/master/classjuce_1_1dsp_1_1DelayLine.html
[T3]: https://docs.juce.com/master/structjuce_1_1dsp_1_1DelayLineInterpolationTypes_1_1Linear.html
[T4]: https://docs.juce.com/master/structjuce_1_1dsp_1_1DelayLineInterpolationTypes_1_1Lagrange3rd.html
[T5]: https://docs.juce.com/master/structjuce_1_1dsp_1_1DelayLineInterpolationTypes_1_1Thiran.html
[T6]: https://www.dsprelated.com/freebooks/pasp/Filtered_Feedback_Comb_Filters.html
[T7]: https://docs.juce.com/master/classjuce_1_1dsp_1_1Oversampling.html
[T8]: https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState.html

---

## 22. Compact handoff statement

> CHROMAVE is an original stereo Character Delay for Windows 11, 64-bit VST3 and FL Studio, with meaningful synthwave/cyberpunk production relevance. Build a small, high-quality first release around reliable musical delay behavior and validated character tools; retain further modulation, drift, degradation, spatial and transient effects as evaluated extension candidates rather than guaranteed parity with Comeback Kid. Treat repeat evolution as the leading sonic direction, not a license to skip DSP experiments. Use the supplied Application Building Template for process, preserve existing CHROMAVE repository truth, reconcile authority before mutation, and propose only the next bounded authorized step.

**Document disposition:** Prepared for product-owner review and template adaptation. No implementation or research gate is passed by creation of this file.
