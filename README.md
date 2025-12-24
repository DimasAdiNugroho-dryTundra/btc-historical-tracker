# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--24%2018:22%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$87,669.45** | 🟢 `+0.21%` | Real-time Aggregate Spot |
| **24h Price Range** | `$86,420.00 — $88,049.89` | `Spread: $1,629.89` | Intraday Volatility Band |
| **24h Trading Volume** | `$797.46 M` | `9,140.84 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.74 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-23` | $87,486.00 | `+$183.45` | 🟢 +0.21% | Intraday Shift |
| **7 Days** | `2025-12-17` | $86,243.22 | `+$1,426.23` | 🟢 +1.65% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-24` | $88,300.01 | `-$630.56` | 🔴 -0.71% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-25` | $108,994.49 | `-$21,325.04` | 🔴 -19.57% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-06-27` | $107,047.59 | `-$19,378.14` | 🔴 -18.10% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-24` | $98,663.58 | `-$10,994.13` | 🔴 -11.14% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$38,530.18` | 🔴 `-30.53%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-24` | $87,486.00 | $88,049.89 | $86,420.00 | $87,669.45 | 🟢 +0.21% | `9,140.84 BTC` |
| `2025-12-23` | $88,620.79 | $88,940.00 | $86,601.90 | $87,486.00 | 🔴 -1.28% | `13,910.33 BTC` |
| `2025-12-22` | $88,658.87 | $90,588.23 | $87,900.00 | $88,620.79 | 🔴 -0.04% | `14,673.22 BTC` |
| `2025-12-21` | $88,360.91 | $89,081.77 | $87,600.04 | $88,658.86 | 🟢 +0.34% | `7,132.87 BTC` |
| `2025-12-20` | $88,136.95 | $88,573.07 | $87,795.76 | $88,360.90 | 🟢 +0.25% | `5,123.13 BTC` |
| `2025-12-19` | $85,516.41 | $89,399.97 | $85,110.24 | $88,136.94 | 🟢 +3.06% | `21,256.65 BTC` |
| `2025-12-18` | $86,243.23 | $89,477.61 | $84,450.01 | $85,516.41 | 🔴 -0.84% | `25,405.42 BTC` |

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

*Last Telemetry Sync: `2025-12-24 18:22:42 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
