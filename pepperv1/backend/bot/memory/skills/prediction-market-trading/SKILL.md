---
name: prediction-market-trading
description: Execute prediction market analysis, identify mispriced contracts, build trading bots, perform cross-platform arbitrage, and construct AI-driven information edge systems on Polymarket and Kalshi. Covers market making, Kelly sizing, resolution risk, and the full AI trading stack.
---

# Prediction Market Trading

Systematic extraction of alpha from prediction markets using information arbitrage, cross-platform arb, market making, speed trading, domain specialization, and high-probability bond strategies.

**Master Reference:** `bot/outputs/prediction-market-master-playbook.md`
**Prior Research:** `bot/outputs/prediction-markets-alternative-trading-research.md`, `bot/outputs/ai-ml-trading-strategies-research-2025-2026.md`

## When to Use

Trigger when user requests:
- "Find mispriced prediction markets"
- "Build a Polymarket/Kalshi bot"
- "Analyze this prediction market"
- "Cross-platform arbitrage opportunities"
- "What should I bet on"
- "Market make on prediction markets"
- "Trade economic indicators / sports / weather events"
- Any request involving Polymarket, Kalshi, or event contract trading

Do NOT use for: traditional stock/options trading, generic sports betting (without prediction market context), or crypto spot trading.

---

## Phase 1: Identify the Strategy

Determine which of the six proven profit models applies. Each has different capital requirements, technical demands, and edge sources.

### Strategy Selection Matrix

| Strategy | Min Capital | Technical Skill | Edge Source | Risk | Ref |
|----------|-----------|----------------|------------|------|-----|
| Cross-Platform Arb | $200 | Low-Med | Price discrepancy | Low (if resolution matches) | [Playbook S3.2] |
| High-Probability Bonds | $500 | Low | Favorite-longshot bias | Low-Med (black swan) | [Playbook S3.3] |
| Domain Specialization | $1,000 | Med | Deep expertise | Med (overconfidence) | [Playbook S3.5] |
| Market Making | $5,000 | High | Spread capture | Med (adverse selection) | [Playbook S3.4] |
| Information Arbitrage | $5,000 | High | Original research / AI | Med-High | [Playbook S3.1] |
| Speed Trading | $2,000 | Very High | Latency advantage | High | [Playbook S3.6] |

**Capital-based recommendation:**
- **$200-$1K**: Cross-platform arb + bonds → [Playbook S10, "$200-$1,000"]
- **$1K-$5K**: Domain specialization + MM on 3-5 markets → [Playbook S10, "$1,000-$5,000"]
- **$5K-$25K**: AI info arb + MM across 10-20 markets → [Playbook S10, "$5,000-$25,000"]
- **$25K+**: Multi-strategy portfolio → [Playbook S10, "$25,000+"]

---

## Phase 2: The Math (Always Apply)

### Kelly Criterion for Binary Markets

```
f* = (p - p_m) / (1 - p_m)
```

- `p` = your true probability estimate
- `p_m` = market price (implied probability)
- **ALWAYS use 0.25x for new strategies, 0.50x for proven**
- Overbetting degrades returns QUADRATICALLY; probability errors degrade LINEARLY
- Full derivation and sensitivity analysis → [Playbook S2.1-2.3]

### Expected Value Per Contract

```
EV = p_true - p_market
```

Only trade when EV > 0 AND you have genuine reason to believe your p_true is more accurate than the market's.

### Slippage Model

```
Slippage = Order_Quantity / (2 * Depth_at_Price_Level)
```

Keep individual trades to $500-$2,000 to avoid excessive slippage → [Playbook S2.5]

---

## Phase 3: Pre-Trade Checklist

Before EVERY trade, verify:

1. **Resolution criteria**: Read the FULL market description (not just the title). Verify source agency, settlement timing, and exact conditions. Cases where literal wording killed traders: Zelenskyy suit, Warner "Bros" vs "Brothers" → [Playbook S5.4]

2. **Cross-platform divergence risk** (for arb): Kalshi uses centralized resolution (Rule 6.3(c) allows last-traded-price settlement). Polymarket International uses UMA Optimistic Oracle ($750 bond, 2hr challenge, DVM escalation). They can resolve DIFFERENTLY. Cardi B case: Polymarket YES, Kalshi $0.26 → [Playbook S5.1-5.3]

3. **UMA oracle vulnerability**: UMA market cap ~$44M vs Polymarket TVL ~$330M. 51% oracle control = ~$22M. Manipulation is economically rational for large positions → [Playbook S3.2, "UMA vulnerability"]

4. **Fee impact**: Kalshi sports fees = `ceil(0.07 * contracts * price * (1 - price))`, ranging 0.6-1.75%. Polymarket ~0.01%. Your edge must exceed fees → [Playbook S8.3]

5. **Liquidity check**: Check order book depth on both sides. Remember CLOB duality: YES book = inverse of NO book → [Playbook S1.1]

---

## Phase 4: Execution

### For Cross-Platform Arbitrage

1. Monitor price feeds on both Polymarket and Kalshi via WebSocket
2. When `price_YES_poly + price_NO_kalshi < $1.00` (or inverse), flag opportunity
3. Verify resolution criteria match WORD FOR WORD
4. Execute both legs simultaneously using **FOK** orders (partial fills = naked exposure)
5. Expected: 0.5-3% per trade, $40M+ extracted market-wide Apr 2024-Apr 2025

**Open-source starter**: `CarlosIbCu/polymarket-kalshi-btc-arbitrage-bot` on GitHub
**Full arb mechanics** → [Playbook S3.2]

### For High-Probability Bonds

1. Scan all markets for contracts at $0.93+ with resolution < 7 days
2. Classify as "genuine certainty" vs "pseudo-certainty" using:
   - Historical accuracy of source agency
   - Whether market has already moved past the information event
   - Whether there are structural reasons the outcome is locked in (e.g., Fed decision 2 days out, confirmed by dot plot + forward guidance)
3. Maximum 10% of bankroll per position
4. Expected: 5% per trade, 2x/week = 520% simple annualized

**Bias exploited**: Favorite-longshot bias (22.4 pp gap documented across 12,084 events) → [Playbook S4.1]

### For Market Making

1. Use Avellaneda-Stoikov model adapted for binary terminal settlement
2. Post two-sided quotes (YES bid + YES offer) to earn ~3x Polymarket liquidity rewards
3. Implement inventory management: skew quotes away from accumulated position
4. Critical: detect and retreat from informed flow (large sudden fills = news event)
5. Use GTD orders to auto-expire before high-impact events
6. Kill switch: auto-pull all quotes if position exceeds limits

**Documented returns**: $200-$800/day depending on market conditions and capital
**Full MM mechanics** → [Playbook S3.4]

### For Domain Specialization

1. Pick ONE vertical: Fed policy, NBA player props, mention markets, weather, geopolitical
2. Build domain model:
   - Fed: Nowcasting (Atlanta Fed GDPNow, Cleveland Fed Nowcast) + alt data → [Playbook S7]
   - Sports: Elo + advanced metrics + injury/rest/travel → [Playbook S8.3]
   - Weather: Ornstein-Uhlenbeck + ECMWF ensemble data → [Playbook S9.1]
   - Mention markets: Corpus analysis of historical statements → [Playbook S3.5, "Axios"]
3. Compare model probability to market price
4. Trade only when divergence > 5% after fees
5. Expect 10-30 trades/year at high accuracy

**Case studies**: HyperLiquid0xb ($1.4M, sports), Axios (96% win rate, mentions), SeriouslySirius ($440K loss, overconfidence failure) → [Playbook S3.5]

### For AI Information Edge

Deploy the full AI trading stack:

```
Data Ingestion → NLP Processing → Probability Model → Kelly Sizer → Execution
```

Components:
- **Data**: Twitter/X API, RSS, Polymarket/Kalshi WebSocket, FRED, NOAA
- **NLP**: FinBERT (financial sentiment), GPT-4o (event classification, 60% accuracy), keyword detection (mention markets)
- **Model**: XGBoost/LightGBM on historical resolution data (NOT raw price prediction)
- **Sizing**: 0.25x fractional Kelly
- **Execution**: py-clob-client (Polymarket), Kalshi REST API

**What works**: Social media velocity predicts price moves with ~89% accuracy when combined with historical data
**What doesn't work**: LSTM/transformer on raw prices (signal-to-noise too low in bounded [0,1] markets)
**Full architecture** → [Playbook S6.1-6.4]

---

## Phase 5: Risk Management (Non-Negotiable)

Seven rules. No exceptions.

| Rule | Limit | Why | Ref |
|------|-------|-----|-----|
| Max single position | 10% bankroll | One bad resolution won't kill you | [Playbook S11.1] |
| Portfolio positions | 5-12 uncorrelated | Diversification across time and event type | [Playbook S11.2] |
| Cash reserve | 20-40% | Capital for unexpected opportunities | [Playbook S11.3] |
| Kelly fraction | 0.25x new / 0.50x proven | Overbetting degrades returns quadratically | [Playbook S11.4] |
| Kill switch | -15% day / -30% single position | Automated shutdown prevents cascading losses | [Playbook S11.5] |
| Resolution verification | Every single trade | Read FULL description, verify cross-platform | [Playbook S11.6] |
| Track CLV | Ongoing | If you consistently buy further from resolution than entry, you're losing edge | [Playbook S11.7] |

---

## Phase 6: Implementation Stack

### Polymarket (py-clob-client)

```python
pip install py-clob-client web3==6.14.0 python-dotenv

from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType, MarketOrderArgs

# Initialize
client = ClobClient(
    host="https://clob.polymarket.com",
    key=PRIVATE_KEY, chain_id=137,
    signature_type=1, funder=FUNDER_ADDRESS
)

# Limit order (GTC)
order = client.create_order(OrderArgs(price=0.55, size=100, side="BUY", token_id=TOKEN_ID))
client.post_order(order, order_type=OrderType.GTC)

# Market order (FOK for arb)
order = client.create_market_order(MarketOrderArgs(token_id=TOKEN_ID, amount=25.0, side="BUY"))
client.post_order(order, order_type=OrderType.FOK)
```

**API architecture**: Gamma (discovery), CLOB (trading), Data (positions)
**Batch size**: Up to 15 orders per API call
**Full code patterns** → [Playbook S6.3]

### Kalshi

- REST API: 50-200ms latency, free for verified users
- WebSocket for real-time price feeds
- Generate keys: Settings > API
- Open-source bots: `OctagonAI/kalshi-deep-trading-bot`, `ryanfrigo/kalshi-ai-trading-bot`
- Full details → [Playbook S6.4]

### Essential Tools

| Tool | Use | Cost |
|------|-----|------|
| PolyTrack | Whale tracking, copy trading | Free |
| Polymarket Analytics | Dashboards, research | Free |
| Prediction Hunt | Cross-platform arb alerts | Free/Paid |
| py-clob-client | Polymarket Python SDK | Free |
| Kalshi API | Kalshi trading | Free |

Full ecosystem map → [Playbook S13]

---

## Key Numbers to Remember

| Metric | Value | Ref |
|--------|-------|-----|
| Cross-platform arb extracted (1 year) | $40M+ | [Playbook S14] |
| Top arb trader (4,049 trades) | $2M | [Playbook S14] |
| Market making peak | $700-800/day | [Playbook S14] |
| Theo's info arb profit | $85M | [Playbook S14] |
| Bot from $313 starting capital | $437K profit | [Playbook S14] |
| Mention market win rate | 96% | [Playbook S14] |
| Wallets with $1K+ profit | 0.51% | [Playbook S14] |
| Kalshi Fed accuracy | 100% (2022-Jun 2025) | [Playbook S14] |
| Favorite-longshot bias gap | 22.4 pp | [Playbook S14] |
| Kalshi sports fee range | 0.6-1.75% | [Playbook S8.3] |

---

## Behavioral Biases to Exploit

1. **Favorite-longshot bias**: Contracts $0.01-$0.15 systematically overpriced. Contracts $0.85-$0.99 systematically underpriced. 22.4 pp gap. → [Playbook S4.1]

2. **News overreaction**: Markets overshoot 5-15 minutes after surprising news. Trade the reversion. → [Playbook S4.2]

3. **Morning-line manipulation**: Early prices on sports markets may be deliberately misleading. Don't trade opening prices naively. → [Playbook S4.3]

4. **Recency/narrative bias**: Retail anchors on recent events and stories. Systematic models exploit this consistently. → [Playbook S4.4]

---

## Common Mistakes (from 0.51% success rate data)

1. **Overtrading**: Best traders do 10-30 trades/year. Most losers trade daily. → [Playbook S12, "Knowing when NOT to trade"]

2. **Ignoring resolution rules**: Markets resolve on EXACT WORDING, not intent. Read the fine print. → [Playbook S5.4]

3. **Full Kelly sizing**: Destroys accounts. Use 0.25x-0.50x. → [Playbook S2.2]

4. **Assuming cross-platform arb is risk-free**: Settlement divergence is real. → [Playbook S3.2, "Cardi B"]

5. **Chasing speed in liquid markets**: You can't beat institutional latency. Find niche markets instead. → [Playbook S3.6]

6. **No kill switch**: Automated risk controls are mandatory, not optional. → [Playbook S11.5]

---

## Build Sequence (For Starting From Zero)

**Week 1-2**: Fork cross-platform arb bot, deploy with $500, FOK execution → [Playbook S12, "Week 1-2"]

**Week 3-4**: Build high-probability bond scanner ($0.93+ contracts, <7 days to resolution) → [Playbook S12, "Week 3-4"]

**Month 2**: Choose ONE domain, build predictive model, paper trade 2 weeks → [Playbook S12, "Month 2"]

**Month 3+**: Build market making bot with Stoikov adaptation, collect liquidity rewards → [Playbook S12, "Month 3+"]

**Ongoing**: Build AI information edge pipeline (NLP + news ingestion + automated execution) → [Playbook S12, "Ongoing"]

---

## Output Standards

- All analysis output goes in `bot/outputs/` with descriptive names
- Include probability estimates with confidence intervals
- Show Kelly sizing calculations
- Flag resolution risks explicitly
- Link to specific playbook sections for every recommendation
- Never recommend a trade without specifying: entry price, position size (as % bankroll), exit conditions, maximum acceptable loss
