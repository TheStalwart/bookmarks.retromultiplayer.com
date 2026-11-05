# Agent instructions

- A request to commit authorizes a local commit only. Never push, publish, or otherwise send changes to a remote unless explicitly asked in the current conversation.
- Treat committing and pushing as separate actions. After a requested commit, stop and report the commit without pushing.
- Use the Git-configured identity as the commit author. When the user asks to take credit, keep them as author and add Copilot only as a `Co-authored-by` trailer; never replace the author identity with Copilot.
