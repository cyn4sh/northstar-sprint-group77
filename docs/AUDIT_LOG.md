# Collaborative Delivery — Audit Log
Group 77 — Northstar Sprint

## Purpose
This log tracks each contribution to the shared repository, mapped to the responsible team member and the task it fulfills, to demonstrate balanced contribution across the sprint.

## Commit History Summary

| Author | Task | Type | Description |
|---|---|---|---|
| Victor | Task 1 | Code | Product, Order, Ticket models built and migrated to Postgres |
| Victor | Task 3 | Code | Order-status lookup endpoint — serializer, view, URL, 404 handling |
| Victor | Task 4 | Code | Stock-availability lookup endpoint — serializer, computed `in_stock`, view, URL, 404 handling |
| Victor | Task 2 (reassigned from Sandra) | Code | Seed data management command — sample Products, Orders, Tickets, idempotent via `get_or_create` |
| Melody | Task 10 | Docs | Corrected demo script aligned to real endpoints, delivered via PR #18 |
| Melody | Task 7 | Docs | Auto-response templates for order-status, stock-availability, and unclassified categories |
| Melody | Task 11 (reassigned from Sandra) | Docs | This audit log |
| Demeke | Task 9 | Docs | Go-live readiness note documenting what works, known issues, and next steps |
| Demeke | Task 12 | Docs | Final packaging of submission artifacts |
| Khalid | Tasks 5, 6, 8 | Code | Rule-based ticket classifier, routing logic, and unit tests (13 tests, all passing) |
| Victor | — | Chore | Dependency management (`requirements.txt`), repository cleanup, and git workflow support across the team |

## Contribution Balance Notes
- Task 2 (seed data) and Task 11 (audit log) were reassigned from Sandra due to continued unresponsiveness through the sprint, following the team's agreed 2-day silence escalation threshold documented in the Team Charter. Sandra did not accept the GitHub collaborator invitation and had no visible contribution in the repository.
- Victor completed Tasks 1, 2, 3, and 4 — the additional Task 2 was taken on to prevent the sprint from stalling, beyond his original assigned workload.
- Melody completed Task 10, and took on Task 11 in addition to her original Task 7, based on demonstrated documentation quality on prior tasks. She also assisted Demeke directly with his tasks during the final delivery push.
- Khalid completed Tasks 5, 6, and 8 — the most technically demanding implementation tasks — with support through pair-programming during final delivery to work through environment setup and testing.
- Demeke completed Task 9 and Task 12, correcting an initial scope misunderstanding on Task 9 after team review.
- Overall, contribution across the active team members (Victor, Khalid, Melody, Demeke) was reasonably balanced given the reassignment of Sandra's tasks, with each member delivering verified, tested work by the sprint deadline.
