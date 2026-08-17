# Victor — Journal: Retry/Backoff Strategies, Webhook Verification

**Day 1 — 17.08.2025**

### [14:22] Attempting: Understand the basic concepts behind retry and backoff strategies, including why retries are used and what makes a failure transient or permanent.

- Tried: Researched retry and backoff strategies, focusing on the meaning of retries, backoff, transient failures, and non-transient failures. Also looked into examples of failures that may be temporary, such as network blips, cold starts, microservice downtime, and server overload, and compared these with non-transient failures such as authentication errors, client errors, and bad data syntax.
- Result: Retry and backoff is a strategy used in computer systems to handle temporary errors. A retry means attempting a failed operation again, while backoff introduces a delay before the next attempt. Some failures are transient and may resolve themselves after a short period, making them suitable candidates for retrying. Permanent failures are unlikely to be fixed by simply trying the same operation again.
- Source consulted:
  - Microsoft Azure — Transient Faults: https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults
  - AWS Builder — Timeouts, retries, and backoff with jitter: https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter
  - urllib3 documentation — Retry: https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html
  - MDN — Retry-After header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After
  - DEV Community — Retry and Backoff Strategies: https://dev.to/godofgeeks/retry-and-backoff-strategies-jitter-2c1p
- Next: Research retryable versus non-retryable failures in more detail, including which HTTP status codes are commonly retried and why blindly retrying every failure can be dangerous.


