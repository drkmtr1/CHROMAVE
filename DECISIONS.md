# Decisions and authorizations

The project began with no inherited decisions or authorizations. Only the actual Product Owner instructions below are recorded; recommendations live in `records/PLAN-001.md`.

For each actual material decision, record the question, selected option and rationale, alternatives considered, actual authorizer, date only when known, exact effective scope, affected records, limitations, and revisit condition. Preserve authorization separately from recommendations or technical results.

## D-001 — New-project process and bounded planning authorization

- Question: which baseline/process and work scope govern this adaptation?
- Actual authorizer/provenance: Will, direct user instruction in this chat, 2026-10-05 (Pacific/Honolulu).
- Selected instruction: start from the neutral new-project state; use the accepted Application Building Template v1.2 instructions already supplied locally; treat the supplied application definition as Product Owner product intent; authorize exactly one bounded in-Codex Planning & Readiness assignment to propose an application plan.
- Rationale: establish this application's own proposed baseline while preserving the separation of requirements, advice, assumptions, unresolved questions and actual decisions.
- Alternatives: the brief mentions older v1.0/external-ChatGPT routing and historical CHROMAVE initialization. Those are historical context; the current explicit instruction selects the fresh local project and current supplied process. No other project's approvals or findings transfer.
- Effective scope: `records/TASK-001.md` contract and its named documentation write set. The real Planning & Readiness contributor returns read-only advice; coordinator owns shared records.
- Required stop: `PLAN_AWAITING_PRODUCT_OWNER_AUTHORIZATION`.
- Limitations: no code, experimental harness, application tests, scaffold, dependency installation, implementation authorization, accepted plan/architecture, milestone acceptance, publication/release, repository/remote creation or automatic successor. The v1.2 version/acceptance attribution is owner-supplied; independently reproducible upstream export identity is unavailable in this folder.
- Affected records: `MASTER_SPEC.md` (attributed user intent only), `PROJECT_STATE.md`, `TODO.md`, `records/TASK-001.md`, `records/PLAN-001.md`.
- Revisit: only upon an explicit new Product Owner disposition or scope/authorization change. Plan approval and any bounded execution scope must be recorded separately; this entry cannot be reused as implementation authority.

## Pending decisions

PLAN-001 direction and its M1 task are approved under D-002. Exact feature/behavior contracts, dependency versions, experiment execution, application-code tasks, milestone acceptance and release remain undecided/unapproved. Questions/options in design advice are not decision entries.

## D-002 — Plan approval, bounded M1 authorization and supplied Git remote

- Actual authorizer/provenance: Will, direct message on 2026-10-05: “I approve and authorize this,” followed by https://github.com/drkmtr1/CHROMAVE.
- Selected disposition: approve PLAN-001 revision 1 (SHA-256 `A0AC2DEEE773F38892243DD11A9EB2F50449FD1DAA3737EE87247F07EF8BF3AB`) as planning direction and authorize its section 4 next bounded documentation/design M1. This is the only next assignment proposed by the approved plan; no blanket build authorization is inferred.
- Rationale: advance from the approved compact direction to decision-ready user-visible core behavior and an experiment protocol, while resolving consequential contracts before dependent code.
- Alternatives: continue waiting for initial plan approval or begin full plugin development. The owner approved the former plan's bounded next task; production and experiments were explicitly excluded from it.
- Effective scope: TASK-002 read/write contract, real planning advice, independent technical review/corrections, then distinct fresh readiness. Coordinator connects the existing empty supplied repository and creates local documentation checkpoints under MASTER_SPEC section 7. Repository metadata is public; no repository creation, force push or release operation is authorized. Ordinary checkpoint push was considered under section7 but automatic approval review rejected public disclosure of the exact payload; user-provided URL alone is not recorded as exact public disclosure approval. F-011 requires explicit permission before any push.
- Accepted direction: compact native delay; recursive tone as an initial repeat-evolution baseline; saturation/motion conditional on evidence, with material reduction requiring a separate disposition. Architecture alternatives, numeric limits, first-repeat/ping-pong/time-change semantics remain proposals until separately accepted; no algorithm, dependency version or DSP contract is frozen.
- Affected records: TASK-002, DESIGN-001 and review/readiness evidence, current state, MASTER_SPEC disposition pointer and TODO.
- Limitations: M1 acceptance, experiment execution, application code/tests, scaffold, dependency installs, final V1 feature freeze, release/publication and successor work remain outside this authorization. Historical TASK-001/PLAN-001 preserve their original unapproved-at-authorship status; this decision supplies current disposition.
- Revisit/stop: finish M1 review/evidence/checkpoint, then `M1_AWAITING_PRODUCT_OWNER_ACCEPTANCE`. Owner acceptance and any next task authorization remain separate.

## D-003 — Explicit public documentation disclosure and push authorization

- Actual authorizer/provenance: Will, direct message on 2026-10-05, “Push them all please and continue,” replying to the explicit request to publish all14 documentation files, including product brief, plans, decisions, findings, review history and superseded revisions, to public `drkmtr1/CHROMAVE`.
- Selected disposition: permit public disclosure and normal push of the complete14-file payload listed in TASK-002, including routine reconciliation of these existing authorization/state/finding/task records. The prior F-011 approval prerequisite is now supplied directly by the owner; a successful push/equality check is still required for closure.
- Scope: preserve the exact reviewed DESIGN revision3 and source/plan identities; update DECISIONS, PROJECT_STATE, TODO and TASK-002 to record permission/results; commit and push to existing origin/main without force, verify local/tracking/live equality after the last tracked mutation. No new public artifact, repository or release is created.
- Rationale: resolve the exact public disclosure gate raised by automatic approval review and save the reviewed documentation remotely.
- Alternatives: retain local-only documentation or omit parts of the payload. The owner explicitly selected all documents.
- Boundary: “continue” unambiguously authorizes completion of this displayed publication/checkpoint gate. It does not explicitly select the three M1 behavior choices or a bounded EXP-001 execution task; a concise clarification has been requested while publication proceeds. No experiment/code/installation/successor authority or milestone acceptance is recorded from ambiguity.
- Revisit: new owner response may settle M1 and next-task scope separately. Preserve the original rejection as historical evidence; this permission permits a new direct normal push, not a workaround.
