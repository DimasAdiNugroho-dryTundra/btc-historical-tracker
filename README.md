# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--01--16%2015:04%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$95,550.94** | 🔴 `-0.06%` | Real-time Aggregate Spot |
| **24h Price Range** | `$94,293.46 — $95,871.47` | `Spread: $1,578.01` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.06 B` | `11,167.71 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.90 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-01-15` | $95,604.80 | `-$53.86` | 🔴 -0.06% | Intraday Shift |
| **7 Days** | `2026-01-09` | $90,641.28 | `+$4,909.66` | 🟢 +5.42% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-17` | $86,243.22 | `+$9,307.72` | 🟢 +10.79% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-18` | $107,185.01 | `-$11,634.07` | 🔴 -10.85% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-07-20` | $117,265.12 | `-$21,714.18` | 🔴 -18.52% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-01-16` | $99,987.30 | `-$4,436.36` | 🔴 -4.44% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$30,648.69` | 🔴 `-24.29%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-01-16` | $95,604.81 | $95,871.47 | $94,293.46 | $95,550.94 | 🔴 -0.06% | `11,167.71 BTC` |
| `2026-01-15` | $96,951.78 | $97,193.34 | $95,134.48 | $95,604.80 | 🔴 -1.39% | `21,725.81 BTC` |
| `2026-01-14` | $95,413.99 | $97,924.49 | $94,559.28 | $96,951.78 | 🟢 +1.61% | `22,851.89 BTC` |
| `2026-01-13` | $91,296.20 | $96,495.00 | $91,042.66 | $95,414.00 | 🟢 +4.51% | `23,021.51 BTC` |
| `2026-01-12` | $91,013.66 | $92,519.95 | $90,128.44 | $91,296.20 | 🟢 +0.31% | `16,188.08 BTC` |
| `2026-01-11` | $90,504.70 | $91,283.89 | $90,236.00 | $91,013.65 | 🟢 +0.56% | `5,477.14 BTC` |
| `2026-01-10` | $90,641.27 | $90,832.00 | $90,404.00 | $90,504.70 | 🔴 -0.15% | `3,104.12 BTC` |

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

*Last Telemetry Sync: `2026-01-16 15:04:26 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
