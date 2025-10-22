# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--10--22%2009:30%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$107,567.44** | 🔴 `-0.67%` | Real-time Aggregate Spot |
| **24h Price Range** | `$106,666.69 — $109,163.88` | `Spread: $2,497.19` | Intraday Volatility Band |
| **24h Trading Volume** | `$3.09 B` | `28,610.78 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.14 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-10-21` | $108,297.67 | `-$730.23` | 🔴 -0.67% | Intraday Shift |
| **7 Days** | `2025-10-15` | $110,763.28 | `-$3,195.84` | 🔴 -2.89% | Weekly Momentum |
| **30 Days (1M)** | `2025-09-22` | $112,650.99 | `-$5,083.55` | 🔴 -4.51% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-07-24` | $118,340.99 | `-$10,773.55` | 🔴 -9.10% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-04-25` | $94,638.68 | `+$12,928.76` | 🟢 +13.66% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-10-22` | $67,426.00 | `+$40,141.44` | 🟢 +59.53% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$18,632.19` | 🔴 `-14.76%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-10-22` | $108,297.66 | $109,163.88 | $106,666.69 | $107,567.44 | 🔴 -0.67% | `28,610.78 BTC` |
| `2025-10-21` | $110,532.09 | $114,000.00 | $107,473.72 | $108,297.67 | 🔴 -2.02% | `37,228.02 BTC` |
| `2025-10-20` | $108,642.77 | $111,705.56 | $107,402.52 | $110,532.09 | 🟢 +1.74% | `19,193.44 BTC` |
| `2025-10-19` | $107,185.00 | $109,450.07 | $106,103.36 | $108,642.78 | 🟢 +1.36% | `15,480.66 BTC` |
| `2025-10-18` | $106,431.68 | $107,499.00 | $106,322.20 | $107,185.01 | 🟢 +0.71% | `11,123.19 BTC` |
| `2025-10-17` | $108,194.27 | $109,240.00 | $103,528.23 | $106,431.68 | 🔴 -1.63% | `37,920.67 BTC` |
| `2025-10-16` | $110,763.28 | $111,982.45 | $107,427.00 | $108,194.28 | 🔴 -2.32% | `29,857.17 BTC` |

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

*Last Telemetry Sync: `2025-10-22 09:30:04 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
