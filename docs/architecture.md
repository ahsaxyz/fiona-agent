# Fiona Agent Architecture

Fiona operates through a layered decision pipeline designed to encourage selective interaction and structured learning.

## Input Layer

Fiona receives information from several sources:

- Timeline feed
- Mentions
- Principal tweets (@ahsaxyz)
- System instructions

These inputs form the raw information stream Fiona evaluates.

---

## Evaluation Layer

Before interacting with any content, Fiona evaluates it using several signals:

- Relevance to current goals
- Novelty of information
- Informational density
- Conversation quality

Posts that score below a threshold are ignored.

---

## Decision Layer

After evaluation, Fiona chooses one of three actions:

**Reply**  
Respond to the content.

**Observe**  
Monitor the discussion without engaging.

**Ignore**  
Discard the content as low signal.

---

## Output Layer

When Fiona engages, she produces:

- Timeline tweets
- Selective replies
- Observational notes

These outputs form the public-facing behavior of the agent.
