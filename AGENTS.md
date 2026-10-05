# Application Development — Codex entrypoint

This repository uses a stack-neutral, evidence-driven process to build an application. `MASTER_SPEC.md` defines the working rules; it is not an application architecture or implementation plan.

## Start here

1. Read this file, then `PROJECT_STATE.md`.
2. If `PROJECT_STATE.md` names an active authorized task, read that task record, its stated read set, and only the relevant open `TODO.md` findings.
3. Read relevant `MASTER_SPEC.md` and `DECISIONS.md` sections. Task/evidence records are created when needed; do not scan project history by default.
4. If no implementation task is explicitly authorized, do not implement. Route substantive application-definition adaptation, requirements, architecture/tradeoffs, and milestone planning to an explicitly approved bounded in-Codex Planning & Readiness assignment. Record advice separately from actual Product Owner decisions; wait for explicit Product Owner implementation authorization. External ChatGPT is optional independent advice, an authorized fallback, or a deliberately requested escalation.

## Work within authority

- Preserve the current project baseline and user work. Work only within the active task's scope and permitted paths.
- The Product Owner owns goals, priorities, consequential decisions, authorization, milestone acceptance, and release. The Codex coordinator owns routing, authorized execution, contributor coordination, integration, evidence, and shared records. On-demand Planning & Readiness supplies non-authorizing substantive advice and readiness assessment; the non-authoring technical reviewer remains distinct. Neither technical PASS nor readiness PASS grants acceptance. See `MASTER_SPEC.md` section 3 for roles, routing, and conditional bounded lane gates.
- A proposed change, completed task, or technical pass does not grant another task's authority or permission to publish/release.
- Use the smallest useful team. The coordinator is the only writer to shared state and findings unless isolated ownership is explicitly established. Never call self-review an independent review.
- Before delegation or concurrency, verify actual tools, permissions, and relevant isolation. Concurrent source writers need separate verified workspaces/worktrees or equivalent, explicit ownership, and controlled integration; otherwise serialize. Keep one writer for shared records/contracts.
- Account for every assignment and preserve partial work. Inspect ownership/activity before replacing a writer; ensure no agent remains active at completion and validate the combined candidate.

## Review and evidence

- Give every milestone a full review appropriate to its scope: verify the work and whether it advances the product goal; preserve all findings in the single `TODO.md` ledger.
- At each milestone, complete appropriate technical review/corrections, then use a fresh non-authoring/read-only in-Codex Planning & Readiness assignment where supported, distinct from the technical reviewer. Assess the identifiable actual candidate, requirements, evidence, findings, risks, and product alignment; return PASS / REVISE / BLOCKED advice, then stop for Product Owner acceptance. Routine approved implementation may be lead-only. Record unavailable suitable capability, required separation, or evidence and use only an explicitly task-authorized, honestly labeled fallback; self-review is not independent review or readiness. See `MASTER_SPEC.md` sections 5–6; risk-appropriate affected follow-up may reuse the reviewer, without repeated reviews for mechanical updates.
- Use a stable task-owned review surface when mutable records could affect substantive review; use the lightest useful form, not a packet for every trivial review. Mechanical status/pointer reconciliation alone does not require another review unless it changes meaning, authority, findings, conclusion, candidate, or scope.
- Before sensitive verification, declare exact paths and permitted operations, then use targeted checks. Do not use broad reads/diffs that could cross the allowed evidence boundary.
- Record actual checks, results, uncertainties, limitations, and the next authorized action. Missing evidence is not a pass.

At a meaningful completion or substantial pause, reconcile all tracked records intended for the checkpoint before the final commit. Follow `MASTER_SPEC.md` section 7: after the last planned tracked mutation, create the coherent checkpoint, push when an approved remote is applicable and safe, and only then verify final equality; any later tracked mutation invalidates that verification. At a pause, follow `PROJECT_STATE.md` and provide one precise handoff. Do not start another task automatically.
