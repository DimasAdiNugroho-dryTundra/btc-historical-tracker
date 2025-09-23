# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--09--23%2019:07%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$111,998.80** | 🔴 `-0.58%` | Real-time Aggregate Spot |
| **24h Price Range** | `$111,458.73 — $113,290.50` | `Spread: $1,831.77` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.38 B` | `12,301.32 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.22 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-09-22` | $112,650.99 | `-$652.19` | 🔴 -0.58% | Intraday Shift |
| **7 Days** | `2025-09-16` | $116,788.96 | `-$4,790.16` | 🔴 -4.10% | Weekly Momentum |
| **30 Days (1M)** | `2025-08-24` | $113,493.59 | `-$1,494.79` | 🔴 -1.32% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-06-25` | $107,340.58 | `+$4,658.22` | 🟢 +4.34% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-03-27` | $87,232.01 | `+$24,766.79` | 🟢 +28.39% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-09-23` | $63,339.99 | `+$48,658.81` | 🟢 +76.82% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-08-14` | $124,474.00 | `-$12,475.20` | 🔴 `-10.02%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-09-23` | $112,650.99 | $113,290.50 | $111,458.73 | $111,998.80 | 🔴 -0.58% | `12,301.32 BTC` |
| `2025-09-22` | $115,232.29 | $115,379.25 | $111,800.00 | $112,650.99 | 🔴 -2.24% | `20,781.71 BTC` |
| `2025-09-21` | $115,685.63 | $115,819.06 | $115,188.00 | $115,232.29 | 🔴 -0.39% | `4,511.52 BTC` |
| `2025-09-20` | $115,632.39 | $116,121.81 | $115,408.47 | $115,685.63 | 🟢 +0.05% | `4,674.93 BTC` |
| `2025-09-19` | $117,073.53 | $117,459.99 | $115,100.00 | $115,632.38 | 🔴 -1.23% | `8,992.09 BTC` |
| `2025-09-18` | $116,447.60 | $117,900.00 | $116,092.76 | $117,073.53 | 🟢 +0.54% | `11,657.23 BTC` |
| `2025-09-17` | $116,788.96 | $117,286.73 | $114,720.81 | $116,447.59 | 🔴 -0.29% | `16,754.25 BTC` |

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

*Last Telemetry Sync: `2025-09-23 19:07:10 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
