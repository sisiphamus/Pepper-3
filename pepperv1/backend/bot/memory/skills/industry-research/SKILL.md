---
name: tech-trend-industry-opportunity-search
description: Discover emerging technology trends by asking clarifying questions, then searching across academic papers, developer activity, funding patterns, patents, hiring data, and more. Produces markdown reports with evidence. All output should go in the reports folder with a clear name.
---

# Tech Trend Search

Systematic discovery of emerging technology trends using the signal cascade methodology (research -> developer -> funding -> mainstream).

## When to Use

Trigger when users request:
- "Find tech trends in [industry]"
- "What's emerging in [area]?"
- "Research trends before they go mainstream"
- "What are weak signals in [sector]?"

Do NOT use for: specific known technologies, historical analysis, or general knowledge questions.

## Three-Phase Workflow

### Phase 1: Refine Scope (Ask 4 Questions)

1. **Industry/Domain**: AI/ML, Energy, Construction, Healthcare, Finance, Manufacturing, Space, Climate Tech, Developer Tools, Multiple domains
2. **Stage of Trend**: Very early weak signals (research) | Emerging with traction (early adopters) | Fast-growing not mainstream | All stages
3. **Time Horizon**: 0-6 months | 6mo-2 years | 2-5 years | Mix
4. **Signal Types**: Technical developments | Market adoption | Funding signals | All types

After answers, confirm understanding in 1-2 sentences before proceeding.

### Phase 2: Broad Search (15-20 Web Searches)

Execute searches across source categories by lead time:

**Academic/Research (3-5 years):**
- "[domain] arxiv papers 2024 2025"
- "[technology] breakthrough research"
- "DARPA programs [domain]"

**Developer Ecosystem (18-36 months):**
- "[technology] github trending"
- "npm downloads [technology]"
- "stack overflow trends [technology]"
- "hacker news [technology]"

Look for: >1000 stars/month growth, fork ratio >0.15, cross-org contributors

**Startup & Funding (2-3 years):**
- "Y Combinator [domain] 2024 2025"
- "[technology] seed funding 2025"
- "[domain] VC investment thesis"

**Hiring Data (12-24 months):**
- "[technology] job postings growth 2025"
- "new job titles [technology]"

**Patents (2-4 years):**
- "[technology] patents 2024 2025"
- "cross-domain patents [industry A] [technology B]"

**Alternative Data (6-18 months):**
- "[component] shortage 2025"
- "[technology] supply chain constraints"

**Communities (6-12 months):**
- "reddit [technology] community growth"
- "twitter [technology] trending"

### Identify 5-10 Promising Signals

**Strong Signal = Multi-Source Convergence:**
- Appears in 3+ independent source categories
- Shows acceleration (growing faster over time)
- Has concrete evidence with metrics
- Demonstrates "adjacent possible" (new combinations feasible)

### Phase 3: Deep Investigation

Deploy sub agents to investigate (reduce context burden). Ask user which 2-3 signals to investigate deeply. For each:

**A. Signal Cascade Mapping** (earliest research, original paper, timeline)
**B. Current State** (production deployment, technical challenges, leading companies)
**C. Adoption & Momentum** (adoption rate, case studies, companies using)
**D. Funding Activity** (startup funding, venture capital)
**E. Forward Analysis** (what does this enable, what's driving adoption, structural tailwinds)

## Final Report Structure

Choose based on findings:
- **Option A - Signal Cascade:** Use when trends follow research -> developer -> funding pattern
- **Option B - Insight-First:** Use when a few dominant trends are most important
- **Option C - Source-Type:** Use when specific source categories revealed strong signals

Always include:
- Action Items (High Priority 1 week, Medium Priority 1 month, Watch List quarterly)
- Evidence links for every claim

## Search Quality Standards

- Run 100-200 total searches
- Verify with 3+ independent sources for "strong" rating
- Look for acceleration, not just activity
- Always link to evidence
- Distinguish hype (media only) from substance (developer adoption)