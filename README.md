# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--27%2007:18%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$61,716.25** | 🟢 `+2.02%` | Real-time Aggregate Spot |
| **24h Price Range** | `$60,380.83 — $61,935.00` | `Spread: $1,554.17` | Intraday Volatility Band |
| **24h Trading Volume** | `$138.27 M` | `2,240.49 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.23 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

---

### 📈 30-Day Rolling Price Action & Volatility Trend

<div align="center">
  <img src="assets/btc_trend.svg" alt="Bitcoin 30-Day Price Trend" width="100%" />
</div>

---

### 📊 Multi-Timeframe Performance & ROI Matrix

Comparison of current spot valuation against standard macroeconomic and historical milestones.

| Timeframe Horizon | Benchmark Date | Historical Base Price | Net Change ($) | ROI Return (%) | Direction & Velocity |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **24 Hours** | `2026-11-26` | $60,495.57 | `+$1,220.68` | 🟢 +2.02% | Intraday Shift |
| **7 Days** | `2026-11-20` | $58,814.99 | `+$2,901.26` | 🟢 +4.93% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-28` | $81,249.31 | `-$19,533.06` | 🔴 -24.04% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-29` | $78,233.93 | `-$16,517.68` | 🔴 -21.11% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-31` | $73,575.17 | `-$11,858.92` | 🔴 -16.12% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-13` | $90,255.32 | `-$28,539.07` | 🔴 -31.62% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$47,183.75` | 🔴 `-43.33%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27` | $60,495.56 | $61,935.00 | $60,380.83 | $61,716.25 | 🟢 +2.02% | `2,240.49 BTC` |
| `2026-11-26` | $60,383.50 | $61,526.89 | $59,842.43 | $60,495.57 | 🟢 +0.19% | `5,928.12 BTC` |
| `2026-11-25` | $59,741.39 | $60,487.00 | $57,208.17 | $60,383.51 | 🟢 +1.07% | `16,694.51 BTC` |
| `2026-11-24` | $61,190.81 | $61,603.49 | $59,189.67 | $59,740.87 | 🔴 -2.37% | `13,455.73 BTC` |
| `2026-11-23` | $61,163.01 | $64,533.96 | $60,286.92 | $61,189.97 | 🟢 +0.04% | `16,914.31 BTC` |
| `2026-11-22` | $60,086.00 | $61,568.11 | $58,636.18 | $61,163.01 | 🟢 +1.79% | `8,857.87 BTC` |
| `2026-11-21` | $58,815.33 | $60,883.03 | $55,106.00 | $60,086.00 | 🟢 +2.16% | `17,117.92 BTC` |

---

### ⚙️ Automation & Pipeline Architecture

- **Automated Execution:** Synced daily at `00:00 UTC` via GitHub Actions (`.github/workflows/update.yml`).
- **Resilient Pipeline:** Cascading multi-exchange API architecture (Binance -> Coinbase -> Kraken -> CoinGecko).
- **Git-Native Telemetry:** Dynamic SVG vector graphics and Markdown dashboards saved directly into Git history.

```
[ GitHub Actions Cron: 00:00 UTC ]
               │
               ▼
   [ fetch_btc.py Executed ] ──► [ Query Multi-Exchange Feeds ]
               │
               ▼
   [ Generate assets/btc_trend.svg & README.md ]
               │
               ▼
   [ Auto Git Commit & Push (main) ]
```

---

<div align="center">

*Last Telemetry Sync: `2026-11-27 07:18:09 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
