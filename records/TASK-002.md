# TASK-002 — M1 core behavior and experiment design

## Authority and scope

Will's direct 2026-10-05 approval, “I approve and authorize this,” accepts PLAN-001 revision 1's proposed direction and authorizes its section 4 next bounded M1 documentation/design assignment. Supplied repository: https://github.com/drkmtr1/CHROMAVE. D-002 records the actual disposition separately from design advice.

Deliver: `records/DESIGN-001.md` covering first-three-echo tap/routing alternatives, manual/automation/tempo transition policies and interruption, compact semantic controls/limit rationale, one timing/routing experiment protocol and remaining prerequisites. Complete non-authoring technical review/corrections, then fresh non-authoring readiness, and stop for Product Owner M1 acceptance. No experiment execution, application code/tests, scaffold, dependency install, algorithm freeze, serialized parameter IDs, future milestone, release or product publication.

Read set: AGENTS; PROJECT_STATE; MASTER_SPEC sections 2–9; DECISIONS; relevant TODO F-002–F-005; TASK-001; PLAN-001; brief sections 3, 9, 11–15; this task, DESIGN-001 and its review evidence. Official technical sources may support recommendations. Targeted Git repository metadata/refs and exact documentation diff/integrity checks are allowed; no other projects, unrelated user files or credentials content.

Coordinator write set: TASK-002, DESIGN-001, `records/REVIEW-002.md`, `records/READINESS-002.md`, task-owned preserved review evidence `records/evidence/task-002/DESIGN-001-revision-1.md` and `DESIGN-001-revision-2.md`, PROJECT_STATE, DECISIONS, TODO, MASTER_SPEC section 9's current disposition pointer. Historical snapshots preserve failed material review without another live contract/ledger. AGENTS, product brief, PLAN-001 and TASK-001 remain unchanged. Local Git initialization, origin connection, documentation commit and ordinary checkpoint push to the supplied repository are normal checkpoint operations; no remote creation or release. Before push, inspect only these named documentation files plus preserved initial documents for unintended sensitive content and whitespace; never stage unknown files or force push.

## Baseline / repository reconciliation

Local initial source integrity: AGENTS SHA-256 `854D738668D2F14A70F145F14731237AA7822E3D1BB80147BCF259B9B26A9A2D`; brief `6559A9164A76DE9DA13943C9C3C86522CC401B2318200A58F840ECA67587640D`; approved PLAN-001 `A0AC2DEEE773F38892243DD11A9EB2F50449FD1DAA3737EE87247F07EF8BF3AB`.

Workspace remains documentation-only and initially has no .git. Git 2.55.0.windows.1 and gh 2.96.0 are available. Initial sandboxed network read failed DNS; approved elevated targeted inspection succeeded. GitHub metadata reports `drkmtr1/CHROMAVE`, public, empty defaultBranchRef; `git ls-remote --symref ... HEAD refs/heads/main refs/heads/master` succeeded with no refs. No existing remote application history or candidate was found; do not infer history from the brief. Recheck refs before first push and stop/reconcile if another writer establishes a branch.

## Assignment ownership and verification

Supported native collaboration; one coordinator writer. Planning author returns read-only design advice; separate fresh technical reviewer reads the actual integrated document/authority/findings; after correction a fresh readiness contributor distinct from author/reviewer assesses the candidate. No recursive delegation or simultaneous source writers. Instructions establish read-only ownership, not technically enforced hidden-context/workspace isolation.

Material outputs: behavior/routing tables, transition policies, experiment fixtures/oracles/criteria, coordinator integration and owner-decision mapping. Verification: independent technical document/DSP reasoning and experiment-design review; source/authority/trace checks; fresh product-alignment readiness. Runtime DSP/plugin/host/performance/listening evidence is not applicable to this milestone and must remain absent/unclaimed. Review gaps or failed attempts stay in TODO with stable IDs.

## Acceptance criteria

1. Attributed requirements and accepted plan direction stay separate from unaccepted DSP/behavior proposals.
2. First-repeat and channel examples are mathematically consistent for centered, L-only, R-only and stereo input, with exact injection/tap/round-trip ordering.
3. Manual edits, host automation, tempo changes, interrupted retargets and ordering have explicit candidate policies, tradeoffs and unresolved prerequisites.
4. One bounded experiment protocol identifies controlled inputs/envelope, sample rates/block partitions, independent expected observables, predeclared selection criteria, custody, negative/inconclusive handling and stop conditions without executing tests.
5. Open choices name blocked dependent work, resolving evidence and actual owner action; future nonlinear/host/dependency/performance tasks stay separate.
6. Integrated candidate passes appropriate technical review/corrections and fresh readiness; records, original integrity, assignments and checkpoint are reconciled. PASS remains advice; owner milestone acceptance required.

## Rollback and stop

Preserve all initial documents and approval history. If rejected, supersede the proposed design through a recorded owner disposition; Git revert only task-owned documentation if needed, never reset unrelated work. A correction outside the bounded contract stops affected work for an actual decision.

Terminal gate: `M1_AWAITING_PRODUCT_OWNER_ACCEPTANCE`. No successor starts automatically. Final local/tracking/live equality is verified only after every planned tracked mutation and checkpoint; no tracked record embeds its containing commit SHA.

## Result / evidence

Local M1 documentation delivery complete; owner milestone/behavior disposition pending. Exact current candidate: DESIGN-001 revision3, SHA-256 `0A29614548A4868915FCF0E13FDDD5BB9510615C3CAA5854E79144E624185769`.

Assignments accounted:

- `/root/m1_design_author`: completed bounded read-only substantive planning; returned first-echo/routing math, transition policies, controls and experiment design with primary sources. No writes, experiments, code/tests, installs or recursive delegation.
- Coordinator: integrated actual candidate and authority/requirements trace, corrected document defects, retained failed candidates/results, wrote all shared records and checked combined documents.
- `/root/m1_technical_review`: completed independent non-authoring review (revision1 REVISE F-006–F-009), affected follow-up (revision2 verified those corrections, REVISE F-010), final affected follow-up (revision3 PASS/no additional findings). REVIEW-002 preserves actual hashes/checks; both failed candidates remain task-owned snapshots.
- `/root/m1_readiness`: completed fresh non-authoring readiness, distinct from author and technical reviewer, PASS for presenting revision3; checkpoint-gate follow-up reverified candidate identity and retained PASS with public push explicitly blocked. READINESS-002 records limitations. No contributor remains assigned ongoing work.

Acceptance-criteria verification: source intent/advice/actual decisions remain separate; first-three-echo arithmetic and channel consequences checked under stated linear/proxy assumptions; transition return-old/no-restart/endpoint rules and paper sample indices independently verified; explicit fixtures/oracles/criteria/custody/negative controls and204-panel counts/storage checked; future prerequisites/owner actions remain visible; technical and fresh readiness PASS support presentation only. No numeric/host/performance/listening claim or behavior/algorithm freeze is created.

Actual coordinator checks: initial ordered startup/authority/known hashes; targeted remote metadata/refs; original AGENTS/brief/approved plan integrity; exact named-document whitespace and credential-marker checks; local named-file staging and diff-check on authored documents; root local Git checkpoint created without overwriting work. Product brief's original Markdown hard-break spaces were preserved; it was excluded from authored-document whitespace correction. Independent reviewer checked204 counts and1,933,632,000 primary raw bytes; coordinator independently checked the same arithmetic. This was document arithmetic, not experiment execution.

Findings: F-006–F-010 resolved at document level with corrective action and verification/qualified lessons retained in TODO; runtime effectiveness UNKNOWN. F-002/F-003/F-005 remain open prerequisites/limitations. F-004 partially resolved locally; F-011 blocks public backup. Repeated/failed reviews were never represented as initial PASS.

Scope checks: no application code/tests, harness execution, scaffold, installs, selected dependency versions, host/plugin validation, audio renders, listening session or benchmark. Runtime checks not applicable to M1; references establish documented options, not CHROMAVE conformance.

Public checkpoint gate discovered during execution: a safe named-file credential-marker scan found no matched credential markers. Sandboxed staging failed `.git/index.lock` permission; elevated local-only staging/commit succeeded. An attempted public push was rejected by automatic approval review: the supplied public URL/authorized checkpoint did not explicitly authorize public disclosure of this exact internal documentation payload. No push ran; no workaround or indirect retry is permitted. This overrides the contemplated push operation in the contract until explicit Product Owner payload approval. The work proceeds to a complete local candidate/checkpoint; F-011 and final handoff preserve the external gate. No private remote or changed visibility is invented.

## Final local checkpoint and exact public payload

All planned tracked record mutations are reconciled here before the final local commit. The final operation stages only these14 Markdown documents, checks the authored diff, commits and verifies clean local state/original and candidate hashes. Live HEAD/final tool evidence owns resulting identity; no containing SHA is written into this record. No tracking/live equality, successful push or remote backup can be claimed.

Public approval payload: AGENTS.md; CHROMAVE_APPLICATION_DEFINITION.md; MASTER_SPEC.md; PROJECT_STATE.md; DECISIONS.md; TODO.md; records/TASK-001.md; records/PLAN-001.md; records/TASK-002.md; records/DESIGN-001.md; records/REVIEW-002.md; records/READINESS-002.md; records/evidence/task-002/DESIGN-001-revision-1.md; records/evidence/task-002/DESIGN-001-revision-2.md. This includes product intent and all task/decision/finding/review history; everyone can read it if pushed to this public repository. Credential-marker checks do not replace permission for that disclosure.

Terminal state: `M1_AWAITING_PRODUCT_OWNER_ACCEPTANCE`; no active assignment/successor. Precise handoff: Product Owner disposes M1 revision3 and first-tap/Ping-Pong/timing proposals; separate public-payload permission decides F-011. EXP-001 execution/application work requires a separately bounded explicit task. If later permission allows push, reconcile any new decision record, create a fresh checkpoint and then verify local/tracking/live equality after its last tracked mutation; do not publish this stale tip without reconciliation.
