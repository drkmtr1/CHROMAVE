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

In progress. Actual assignment results, checks, limitations and final checkpoint handoff will be reconciled here before the checkpoint.
