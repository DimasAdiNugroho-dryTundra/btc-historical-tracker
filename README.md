# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--21%2009:18%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$88,658.86** | 🟢 `+0.34%` | Real-time Aggregate Spot |
| **24h Price Range** | `$87,600.04 — $89,081.77` | `Spread: $1,481.73` | Intraday Volatility Band |
| **24h Trading Volume** | `$629.72 M` | `7,132.87 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.76 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-20` | $88,360.90 | `+$297.96` | 🟢 +0.34% | Intraday Shift |
| **7 Days** | `2025-12-14` | $88,172.17 | `+$486.69` | 🟢 +0.55% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-21` | $85,129.43 | `+$3,529.43` | 🟢 +4.15% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-22` | $112,650.99 | `-$23,992.13` | 🔴 -21.30% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-06-24` | $106,083.00 | `-$17,424.14` | 🔴 -16.43% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-21` | $97,291.99 | `-$8,633.13` | 🔴 -8.87% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$37,540.77` | 🔴 `-29.75%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-21` | $88,360.91 | $89,081.77 | $87,600.04 | $88,658.86 | 🟢 +0.34% | `7,132.87 BTC` |
| `2025-12-20` | $88,136.95 | $88,573.07 | $87,795.76 | $88,360.90 | 🟢 +0.25% | `5,123.13 BTC` |
| `2025-12-19` | $85,516.41 | $89,399.97 | $85,110.24 | $88,136.94 | 🟢 +3.06% | `21,256.65 BTC` |
| `2025-12-18` | $86,243.23 | $89,477.61 | $84,450.01 | $85,516.41 | 🔴 -0.84% | `25,405.42 BTC` |
| `2025-12-17` | $87,863.43 | $90,365.85 | $85,314.00 | $86,243.22 | 🔴 -1.84% | `19,834.12 BTC` |
| `2025-12-16` | $86,432.08 | $88,175.98 | $85,266.00 | $87,863.42 | 🟢 +1.66% | `18,456.05 BTC` |
| `2025-12-15` | $88,172.16 | $90,052.64 | $85,146.64 | $86,432.08 | 🔴 -1.97% | `19,778.69 BTC` |

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

*Last Telemetry Sync: `2025-12-21 09:18:33 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
