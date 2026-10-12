---
name: powertech-release
description: Run a fast, risk-based final check and publish a Powertech Performance website change when the user has authorized a push.
---

# Powertech release

Use after a Powertech website edit. Publishing requires the user's authorization, including authorization already given in the conversation.

1. Review `git status --short` and the changed-file list. Keep unrelated or generated files out of the commit. Inspect the actual diff once.
2. Run one focused check pass: `git diff --check`; confirm local links and assets touched by the change, relevant HTML/JSON validity, and the requested responsive behavior. Check forms or tracking only if edited. Run broader project validation only when it covers the change and can resolve a concrete remaining risk; report known baseline failures without repeating the same failing check.
3. Commit only intended files. Push when authorized. Verify the public URL once after deployment with an HTTP check; if it is not ready, retry briefly after the deployment has had time to finish.
4. Report the final URL, what changed, and any material unverified point. Do not equate a successful push or HTTP 200 with full visual or form-delivery verification.

Keep verification proportional to the change. Stop once the relevant checks pass.
