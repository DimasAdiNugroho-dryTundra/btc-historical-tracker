# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--05--23%2010:45%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$76,752.01** | 🟢 `+1.61%` | Real-time Aggregate Spot |
| **24h Price Range** | `$74,289.60 — $77,404.18` | `Spread: $3,114.58` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.14 B` | `15,086.89 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.52 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-05-22` | $75,539.50 | `+$1,212.51` | 🟢 +1.61% | Intraday Shift |
| **7 Days** | `2026-05-16` | $78,148.05 | `-$1,396.04` | 🔴 -1.79% | Weekly Momentum |
| **30 Days (1M)** | `2026-04-23` | $78,257.48 | `-$1,505.47` | 🔴 -1.92% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-02-22` | $67,643.40 | `+$9,108.61` | 🟢 +13.47% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-11-24` | $88,300.01 | `-$11,548.00` | 🔴 -13.08% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-05-23` | $107,318.30 | `-$30,566.29` | 🔴 -28.48% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$49,447.62` | 🔴 `-39.18%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-05-23` | $75,539.50 | $77,404.18 | $74,289.60 | $76,752.01 | 🟢 +1.61% | `15,086.89 BTC` |
| `2026-05-22` | $77,615.52 | $77,900.00 | $75,359.18 | $75,539.50 | 🔴 -2.67% | `11,272.36 BTC` |
| `2026-05-21` | $77,552.24 | $78,200.00 | $76,719.47 | $77,615.52 | 🟢 +0.08% | `11,318.26 BTC` |
| `2026-05-20` | $76,834.36 | $77,853.04 | $76,516.74 | $77,552.23 | 🟢 +0.93% | `11,296.26 BTC` |
| `2026-05-19` | $77,001.88 | $77,414.62 | $76,144.71 | $76,834.36 | 🔴 -0.22% | `11,024.86 BTC` |
| `2026-05-18` | $77,457.67 | $77,800.00 | $76,051.00 | $77,001.87 | 🔴 -0.59% | `18,745.52 BTC` |
| `2026-05-17` | $78,148.05 | $78,599.99 | $76,735.16 | $77,457.67 | 🔴 -0.88% | `8,442.70 BTC` |

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

*Last Telemetry Sync: `2026-05-23 10:45:59 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
