# Repository-specific agent instructions

These instructions add repository-specific guidance; they supplement, rather than replace, the agent's general defaults and other applicable instructions.

## Commits

- A request to commit authorizes a local commit only. Never push or publish unless explicitly asked in the current conversation. Treat committing and pushing as separate actions; after a requested commit, stop and report it without pushing.
- Keep each commit focused on one logical change. Do not mix unrelated code, documentation, configuration, or process changes in a commit, even if they are all pending in the worktree.
- Before committing, inspect the staged diff and make sure every included change belongs to the same requested task. When asked to commit a specific change, include only that change and leave unrelated work uncommitted.
- Write a brief, descriptive commit subject that says what changed, not only which part of the project changed or why. Keep it informative in a shortlog (for example, `Limit bookmark groups to two columns on mobile`, not `Improve bookmark layout on iPhone 13 mini`); put extra context in the body only when useful.
- Use the Git-configured identity as the commit author. When the user asks to take credit, keep them as author and add Copilot only as a `Co-authored-by` trailer; never replace the author identity with Copilot.
