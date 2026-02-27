# Pepper-3

Third generation of Pepper, where it stopped being a chatbot and became a pipeline.

Every message flows through a chain of specialized models, each with exactly one job:

```
User message
  -> Delegator         classify what this is
  -> Knowledge Auditor what do we already know?
  -> Teacher           fill gaps only if needed
  -> Executor          do the work
  -> Learner           extract reusable knowledge
```

The Knowledge Auditor is the key insight. Before burning tokens on generation, check what the system already knows. The Teacher only fires when there's a genuine gap -- not every time. This matters when you're paying per token.

Connects to WhatsApp (via Baileys), Telegram, SMS, and a web interface. One backend serving all of them through Express and Socket.IO. I message Pepper from my phone and it runs through the full pipeline regardless of channel.

```bash
cd pepperv1/backend && npm install && node server.js
```

Needs a config file with API keys for Claude and messaging services.

Node.js, Express, Socket.IO, Baileys, Telegram Bot API, Claude CLI.
