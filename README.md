# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--10--21%2016:11%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$108,297.67** | 🔴 `-2.02%` | Real-time Aggregate Spot |
| **24h Price Range** | `$107,473.72 — $114,000.00` | `Spread: $6,526.28` | Intraday Volatility Band |
| **24h Trading Volume** | `$4.11 B` | `37,228.02 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.15 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-10-20` | $110,532.09 | `-$2,234.42` | 🔴 -2.02% | Intraday Shift |
| **7 Days** | `2025-10-14` | $113,028.14 | `-$4,730.47` | 🔴 -4.19% | Weekly Momentum |
| **30 Days (1M)** | `2025-09-21` | $115,232.29 | `-$6,934.62` | 🔴 -6.02% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-07-23` | $118,755.99 | `-$10,458.32` | 🔴 -8.81% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-04-24` | $93,980.47 | `+$14,317.20` | 🟢 +15.23% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-10-21` | $67,377.50 | `+$40,920.17` | 🟢 +60.73% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$17,901.96` | 🔴 `-14.19%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-10-21` | $110,532.09 | $114,000.00 | $107,473.72 | $108,297.67 | 🔴 -2.02% | `37,228.02 BTC` |
| `2025-10-20` | $108,642.77 | $111,705.56 | $107,402.52 | $110,532.09 | 🟢 +1.74% | `19,193.44 BTC` |
| `2025-10-19` | $107,185.00 | $109,450.07 | $106,103.36 | $108,642.78 | 🟢 +1.36% | `15,480.66 BTC` |
| `2025-10-18` | $106,431.68 | $107,499.00 | $106,322.20 | $107,185.01 | 🟢 +0.71% | `11,123.19 BTC` |
| `2025-10-17` | $108,194.27 | $109,240.00 | $103,528.23 | $106,431.68 | 🔴 -1.63% | `37,920.67 BTC` |
| `2025-10-16` | $110,763.28 | $111,982.45 | $107,427.00 | $108,194.28 | 🔴 -2.32% | `29,857.17 BTC` |
| `2025-10-15` | $113,028.13 | $113,612.35 | $110,164.00 | $110,763.28 | 🔴 -2.00% | `22,986.49 BTC` |

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

*Last Telemetry Sync: `2025-10-21 16:11:19 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
