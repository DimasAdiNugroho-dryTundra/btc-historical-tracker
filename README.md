# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--29%2019:16%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$87,237.13** | 🔴 `-0.81%` | Real-time Aggregate Spot |
| **24h Price Range** | `$86,806.50 — $90,406.08` | `Spread: $3,599.58` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.76 B` | `19,894.99 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.73 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-28` | $87,952.71 | `-$715.58` | 🔴 -0.81% | Intraday Shift |
| **7 Days** | `2025-12-22` | $88,620.79 | `-$1,383.66` | 🔴 -1.56% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-29` | $90,802.44 | `-$3,565.31` | 🔴 -3.93% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-30` | $114,048.93 | `-$26,811.80` | 🔴 -23.51% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-07-02` | $108,849.60 | `-$21,612.47` | 🔴 -19.86% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-29` | $93,738.20 | `-$6,501.07` | 🔴 -6.94% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$38,962.50` | 🔴 `-30.87%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-29` | $87,952.71 | $90,406.08 | $86,806.50 | $87,237.13 | 🔴 -0.81% | `19,894.99 BTC` |
| `2025-12-28` | $87,877.00 | $88,088.75 | $87,435.00 | $87,952.71 | 🟢 +0.09% | `4,446.29 BTC` |
| `2025-12-27` | $87,369.56 | $87,984.00 | $87,253.05 | $87,877.01 | 🟢 +0.58% | `4,469.55 BTC` |
| `2025-12-26` | $87,225.27 | $89,567.75 | $86,655.08 | $87,369.56 | 🟢 +0.17% | `18,344.62 BTC` |
| `2025-12-25` | $87,669.44 | $88,592.74 | $86,934.72 | $87,225.27 | 🔴 -0.51% | `7,096.58 BTC` |
| `2025-12-24` | $87,486.00 | $88,049.89 | $86,420.00 | $87,669.45 | 🟢 +0.21% | `9,140.84 BTC` |
| `2025-12-23` | $88,620.79 | $88,940.00 | $86,601.90 | $87,486.00 | 🔴 -1.28% | `13,910.33 BTC` |

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

*Last Telemetry Sync: `2025-12-29 19:16:48 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
