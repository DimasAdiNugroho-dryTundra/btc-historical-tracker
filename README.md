# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--06--26%2013:55%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$60,097.27** | 🟢 `+0.51%` | Real-time Aggregate Spot |
| **24h Price Range** | `$58,337.00 — $60,759.99` | `Spread: $2,422.99` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.64 B` | `27,403.56 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.19 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-06-25` | $59,794.00 | `+$303.27` | 🟢 +0.51% | Intraday Shift |
| **7 Days** | `2026-06-19` | $63,543.91 | `-$3,446.64` | 🔴 -5.42% | Weekly Momentum |
| **30 Days (1M)** | `2026-05-27` | $74,449.30 | `-$14,352.03` | 🔴 -19.28% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-03-28` | $66,377.03 | `-$6,279.76` | 🔴 -9.46% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-12-28` | $87,952.71 | `-$27,855.44` | 🔴 -31.67% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-06-26` | $106,947.06 | `-$46,849.79` | 🔴 -43.81% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$66,102.36` | 🔴 `-52.38%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-06-26` | $59,794.64 | $60,759.99 | $58,337.00 | $60,097.27 | 🟢 +0.51% | `27,403.56 BTC` |
| `2026-06-25` | $61,078.00 | $61,962.40 | $58,115.01 | $59,794.00 | 🔴 -2.10% | `30,386.01 BTC` |
| `2026-06-24` | $62,734.57 | $63,239.06 | $59,102.70 | $61,077.99 | 🔴 -2.64% | `30,678.29 BTC` |
| `2026-06-23` | $64,020.01 | $64,275.38 | $61,938.00 | $62,734.57 | 🔴 -2.01% | `20,222.99 BTC` |
| `2026-06-22` | $63,312.00 | $65,622.83 | $63,312.00 | $64,020.01 | 🟢 +1.12% | `15,423.11 BTC` |
| `2026-06-21` | $64,298.01 | $64,588.00 | $63,270.00 | $63,311.99 | 🔴 -1.53% | `8,034.66 BTC` |
| `2026-06-20` | $63,543.90 | $64,388.00 | $63,184.21 | $64,298.01 | 🟢 +1.19% | `9,522.10 BTC` |

---

### ⚙️ Automation & Pipeline Architecture

- **Automated Execution:** Synced daily at `00:00 UTC` via GitHub Actions (`.github/workflows/update.yml`).
- **Zero Overhead:** Pure Python engine generating dynamic SVG vector graphics and Markdown dashboards without heavy dependencies.
- **Git-Native Telemetry:** Historical state is preserved directly in Git commit history without third-party databases.

```
[ GitHub Actions Cron: 00:00 UTC ]
               │
               ▼
   [ fetch_btc.py Executed ] ──► [ Query Binance / CoinGecko API ]
               │
               ▼
   [ Generate assets/btc_trend.svg & README.md ]
               │
               ▼
   [ Auto Git Commit & Push (main) ]
```

---

<div align="center">

*Last Telemetry Sync: `2026-06-26 13:55:20 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
