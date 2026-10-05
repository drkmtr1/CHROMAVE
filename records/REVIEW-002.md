# REVIEW-002 — Independent technical review of M1

Reviewer: real non-authoring `/root/m1_technical_review`, distinct from the design author/coordinator and subsequent readiness. Read-only assignment; no edits, recursive delegation, executable DSP tests or experiment execution.

## Revision 1 — REVISE

Actual candidate SHA-256 verified before/after review: `F390424ECC5F86889572D90134287FFB1165F086F0DF817AFE4332DDB372EB2D`. Preserved at `records/evidence/task-002/DESIGN-001-revision-1.md`. Full relevant candidate, TASK-002/PLAN-001 criteria, D-002 authority, USER REQUIREMENTS, TODO and governing process inspected.

| Ledger ID | Finding / original candidate lines | Required correction |
| --- | --- | --- |
| F-006, P1 material | DESIGN revision1 lines53,61–64: clearing pending work against old committed endpoint during an active transition can lose a return-to-old request; routing shares ambiguity. | Compare active desired destination while active, committed only when idle; retain return-old and avoid identical-target restarts. |
| F-007, P2 material | Revision1 lines45,53,55,92,100: unspecified round(T*fs), especially5 ms at44100=220.5; routing/Repitch endpoint rules incomplete. | Common positive-half-up N and inclusive endpoints, consistent retirement/arbitration for all families. |
| F-008, P2 material | Revision1 lines109–119,123: no isolated return-old/repeat-target schedules and invalid-BPM payload unspecified. | Exact timing/routing schedules, final destinations, semantic invalid marker and independent paper traces. |
| F-009, P3 minor | Revision1 lines55,96,117,131: ideal950 Hz derivative could be read as exact linear-interpolator behavior. | Distinguish ideal analytical frequency from observed sampled/interpolated reference and ripple. |

Checks found recurrence/echo arithmetic correct under declared assumptions; mono-sum/channel/fold-down consequences correct; restricted stored-state bound .125/(1-.9)=1.25 correct with causal convex reads and bounded J/R; signed-frequency derivative correct. Shared-history Smooth topology, explicit style policy and independent oracle/custody design appropriate. Existing runtime/dependency/provenance gaps F-002/F-003/F-005 remain honestly deferred, not documentation failures. M1 selection/listening keeps owner decision separate from fidelity. Authority is documentation-only and consistent; checkpoint work is coordinator responsibility.

Primary technical references independently checked: the time-varying-delay textbook, official VST3 automation and JUCE DelayLine links in DESIGN-001. No reference supplies CHROMAVE runtime evidence. REVISE history is retained rather than replaced by a later PASS.

## Revision 2 — corrected F-006–F-009; REVISE for F-010

Coordinator integrated bounded document corrections: active-versus-idle matching, common discrete endpoints, exact invalid-tempo marker, return-old/repeat/collision schedules with paper endpoints, ideal-versus-interpolated frequency qualification. No behavior is frozen or experiment executed.

Candidate SHA-256: `B523BBB7119CEC98E5EEA8B428EF4FA04984237A1AFE85590DE3AD618A285FC6`. Existing reviewer receives affected follow-up covering corrected rules/schedules and their combined interactions; unchanged checks remain applicable. Finding closure and technical PASS require actual follow-up, not coordinator assertion.

Actual follow-up verified the revision2 hash and revision1 preservation. F-006–F-009 resolved at document level: active/idle equality and routing return behavior; common N and endpoints; invalid-tempo representation/isolated schedules; ideal frequency qualification. Independent paper endpoints at44100 agree: start44100, retarget44188, A first44982/return45864; B first44321/return44542; C retargeted return45070/repeated target44982; routing44982/45864; endpoint-collision A/C45864, B44542. Runtime effectiveness remains UNKNOWN.

New F-010 (P2 material): blanket full-grid/every-source/every-schedule language implied about15,000–17,000 twenty-second renders, approximately150–170 GB raw candidate float audio before reference/diagnostics. This was an estimated workload, not an executed failure; it was disproportionate to the smallest useful experiment. Required explicit selected mandatory panels, counts/storage arithmetic, edge/rate/partition coverage and retained limitations, with no result-driven omission. Therefore revision2 remained REVISE. Exact revision2 is preserved under `records/evidence/task-002/DESIGN-001-revision-2.md`.

## Revision 3 — PASS, M1 documentation technical scope

Candidate SHA-256 `0A29614548A4868915FCF0E13FDDD5BB9510615C3CAA5854E79144E624185769`. Coordinator replaced Cartesian obligation with10 panels/204 primary renders. All policy edges are covered on a declared primary environment, static routing/taps span rates, representative high-feedback timing/routing and prescribed motion span every rate/partition. Four negative controls remain manifested separately. Primary raw stereo float32 storage is1,933,632,000 bytes; reference traces/reruns are additional. Arithmetic was checked, no render executed. Reviewer must verify coverage/counts/limitations before closure.

Actual final affected follow-up: **PASS**; F-010 resolved at document level, no additional findings. Reviewer verified actual revision3 hash, all10 counts (60+24+3+3+72+12+6+6+12+6=204), endpoint-collision initial-mode applicability, independent summed rates12,085,200 and8*20*12,085,200=1,933,632,000 bytes. All controller edges, rate/partition stress, input/tap/route static diagnostics, bounded pluck listening, four negative controls and explicit coverage/resource limitations are consistent. Sections1–4 and final authority boundary were reread; unchanged previous mathematical/authority checks remain applicable. No runtime/host/listening/performance evidence was supplied or claimed.

This technical PASS permits fresh readiness, not Product Owner M1 acceptance, contract freezing, experiment execution or implementation. Both earlier REVISE outcomes remain part of the checkpoint evidence.
