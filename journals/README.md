# Learning & Blocker Journals — The Meridian Pivot (Week 2)

## Purpose
Each teammate keeps their own journal here, logging real-time progress on
their privately assigned tool during Days 1–2 (Assignment 1). This is your
evidence of genuine, unsupervised troubleshooting — not a summary written
after the fact.

## Rules
- **One file per person.** Do not edit anyone else's file.
- **Log live.** Add an entry as soon as something happens — don't
  batch-write at the end of the day from memory.
- **One commit per entry (or small batch).** Commit history timestamps are
  part of the evidence — that's the point of keeping this in the repo
  instead of a doc.
- **Never rewrite past entries.** If something you wrote turns out to be
  wrong, add a *new* entry noting the correction. Don't edit history.
- **Commit message format:** `docs(journal): <short description>`
  e.g. `docs(journal): log first webhook signature failure`
- Work happens on the `journal` branch — keep it separate from Day 3+
  feature branches.

## Entry format
Each entry follows this structure:

```
### [HH:MM] Attempting: <what you're trying to do>
- Tried: <specific thing you did>
- Result: <what happened — error text, unexpected output, success>
- Source consulted: <docs link / AI-explained concept / nothing>
- Next: <what you're trying next, and why>
```

## Assigned tools
| Person | Tool(s) |
|---|---|
| Victor | Retry/backoff strategies, Webhook verification |
| Khalid | Message queue (RabbitMQ/Celery basics) |
| Demeke | GraphQL |
| Melody | Serverless functions |