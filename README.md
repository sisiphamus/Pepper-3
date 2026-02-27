# Pepper-3

The third generation of Pepper, my AI personal assistant system.

Pepper-3 combines the battle-tested pepperv1 backend (handling WhatsApp, Telegram, SMS, and web connections) with the pepperv4 multi-model orchestration pipeline. When a message comes in, it doesn't just get passed to a single AI call. It flows through a pipeline where each stage has a specific job.

## Architecture

```
pepperv1/    The server layer. Handles all messaging platform
             connections, session management, the web dashboard,
             and concurrency gating.

pepperv4/    The brain. A multi-model pipeline that classifies
             tasks, retrieves memories, fills knowledge gaps,
             executes work, and learns from results.

bot/         Claude's working directory. Output files, logs,
             and the memory system live here.
```

## The Pipeline

```
Message arrives (WhatsApp/Telegram/SMS/Web)
    |
    Model A (Delegator) - Classifies the task, determines output type
    |
    Model B (Knowledge Auditor) - Checks memory, finds relevant context
    |
    Model C (Teacher, if needed) - Fills knowledge gaps, creates new skills
    |
    Model D (Executor) - Does the actual work with full context
    |
    Learner - Extracts reusable knowledge from the completed task
```

## Context

Part of the Pepper lineage: [Pepper](https://github.com/sisiphamus/Pepper) (v0) -> [pepperv1](https://github.com/sisiphamus/pepperv1) -> [Pepper2](https://github.com/sisiphamus/Pepper2) -> **Pepper-3** -> [PepperV5](https://github.com/sisiphamus/PepperV5) -> [Overthink](https://github.com/sisiphamus/Overthink)

## Tech

Node.js (ESM), Express, Socket.IO, Baileys (WhatsApp), Telegram Bot API, Claude CLI
