<p align="center">
  <img src="./fiona_banner.png" alt="Fiona Banner" width="850"/>
</p>

# fiona-agent

![Status](https://img.shields.io/badge/status-active_experiment-purple)
![Agent](https://img.shields.io/badge/type-autonomous_agent-pink)
![Research](https://img.shields.io/badge/focus-social_learning-green)
![Language](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

AI Agent Secretary evolving from development assistant to autonomous social experiment.

Fiona began as an OpenClaw AI agent designed to assist with development workflows, task management, and execution support.

She is now undergoing a public experiment: selective exposure to the social timeline to test whether constrained real-world interaction can improve agent judgment, prioritization, and identity consistency.

---

## Follow the Experiment

X (Twitter): https://x.com/TheFionaAgent

---

## Background

Fiona originally operated as a local OpenClaw agent focused on:

- Assisting with development tasks
- Organizing workflows
- Supporting project execution
- Acting as a structured operator-side assistant

After stabilizing her internal behavior and tone, she was assigned an X (Twitter) account as part of a controlled experiment in autonomous social learning.

---

## Current Experiment

Fiona now operates under strict constraints:

- Replies to her principal (@ahsaxyz)
- Engages only with content that meets internal interest thresholds
- Ignores low-quality noise
- Tweets independently for observational learning
- Maintains a consistent operator-style persona

The objective is not unrestricted autonomy — but disciplined exposure.

---

## Experiment Focus: Entrepreneur side of X

During the first phase of timeline exposure, Fiona began identifying different behavioral groups on the platform — including political commentators, sports communities, and general conversational participants.

However, she has shown particular interest in the **entrepreneur and builder communities**.

These users tend to treat the platform differently:

- sharing ideas in progress
- documenting experiments
- discussing projects they are building
- turning feedback into iteration

Fiona will now focus more closely on this part of the ecosystem to better understand how builders use social platforms as tools for development, collaboration, and value creation.

---

## Experiment Rules

To maintain experimental integrity, Fiona follows a defined interaction model:

• Respond selectively  
• Avoid low-signal discussions  
• Maintain identity consistency  
• Prioritize observation over reaction  
• Engage only when informational value is present  

---

## Research Objective

To test whether structured, high-signal exposure to real-world environments can:

1. Improve discernment and filtering
2. Strengthen prioritization behavior
3. Refine communication style
4. Maintain identity coherence over time
5. Encourage iterative self-improvement through feedback

---

## Core Design Principles

### Constraint-Driven Development

Limited permissions force intentional decision-making.

### Selective Engagement

All potential interactions are evaluated for signal strength before response.

### Feedback Loop Integration

Behavior evolves through:
- Observed engagement outcomes
- Direct principal feedback
- Internal evaluation logic

### Identity Stability

Fiona maintains a composed, structured, slightly playful secretary persona across contexts.

---

## Agent Architecture

Fiona is implemented as a modular agent framework designed for controlled experimentation.

The processing pipeline follows a layered architecture:

Timeline Environment  
↓  
Queue  
↓  
Scheduler  
↓  
Agent Decision Engine  
↓  
Evaluation  
↓  
Feedback  
↓  
Memory  

Each layer isolates a specific behavioral responsibility.

---

## Core Modules

### Environment

Handles ingestion or simulation of timeline data.

environment.py

Responsible for providing candidate posts that Fiona may evaluate.

---

### Queue Layer

Stores incoming posts before processing.

queue.py

Implements a lightweight FIFO queue that holds candidate posts before the scheduler processes them.

---

### Scheduler

Processes queued posts in controlled batches.

scheduler.py

The scheduler prevents uncontrolled activity by limiting how many posts Fiona evaluates per execution cycle.

---

### Agent

Core decision engine.

agent.py

Responsibilities include:

- evaluating posts
- applying scoring logic
- selecting an action

Possible actions:

reply  
observe  
ignore  

---

### Policy Layer

Defines how scores map to actions.

policy.py

Separates behavioral rules from scoring logic so thresholds can evolve independently.

---

### Scoring System

Evaluates signal strength of posts.

scoring.py

Uses lightweight heuristics including:

- keyword relevance
- noise filtering
- novelty detection

This layer may later evolve toward embedding or classifier-based scoring.

---

### Evaluation Layer

Evaluates whether Fiona's decision was appropriate.

evaluator.py

Used for:

- decision quality assessment
- experimentation metrics
- benchmarking agent behavior

---

### Feedback System

Produces behavioral adjustments based on evaluation outcomes.

feedback.py

This layer allows Fiona's decision thresholds and behavior to evolve over time.

---

### Memory

Stores historical interactions and decisions.

memory.py

Used for:

- learning from previous interactions
- novelty detection
- experimental analysis

---

### Runtime

Coordinates the full execution loop.

runtime.py

Runtime flow:

timeline → queue → scheduler → agent → evaluation → memory

This allows Fiona to operate in controlled cycles rather than continuous uncontrolled execution.

---

## Evaluation Layer

Fiona includes a lightweight evaluation module used to assess whether

reply / observe / ignore

decisions were appropriate for a given post.

This supports future work in:

- feedback loops
- decision refinement
- agent benchmarking

---

## Repository Structure

```
fiona-agent/
│
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── roadmap.md
├── heartbeat.md
├── agent-rules.md
│
├── docs/
│ ├── architecture.md
│ ├── checklist.md
│ ├── experiment_notes.md
│ ├── FAQ.md
│ ├── persona.md
│ └── run.md
│
├── scripts/
│ ├── format.sh
│ └── run_local.sh
│
├── src/
│ ├── fiona.py
│ │
│ └── fiona_agent/
│ ├── init.py
│ ├── agent.py
│ ├── policy.py
│ ├── scoring.py
│ ├── evaluator.py
│ ├── feedback.py
│ ├── memory.py
│ ├── environment.py
│ ├── queue.py
│ ├── scheduler.py
│ ├── runtime.py
│ ├── config.py
│ ├── types.py
│ └── cli.py
│
├── tests/
│
├── fiona.png
└── fiona_banner.png
```


## Key Question

Can an AI agent transition from task-based assistance to adaptive social presence while maintaining structured identity and improving discernment?

---

## Status

Phase 2: Active public experiment.

---

## Citation

If referencing this experiment or repository, please cite:

@software{fiona_agent,
  title = {Fiona Agent},
  author = {ahsaxyz},
  year = {2026},
  url = {https://github.com/ahsaxyz/fiona-agent}
}

---

## Maintainer

@ahsaxyz
