# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--09--27%2016:02%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$109,635.85** | 🔴 `-0.01%` | Real-time Aggregate Spot |
| **24h Price Range** | `$109,064.40 — $109,743.91` | `Spread: $679.51` | Intraday Volatility Band |
| **24h Trading Volume** | `$601.95 M` | `5,501.79 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.18 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-09-26` | $109,643.46 | `-$7.61` | 🔴 -0.01% | Intraday Shift |
| **7 Days** | `2025-09-20` | $115,685.63 | `-$6,049.78` | 🔴 -5.23% | Weekly Momentum |
| **30 Days (1M)** | `2025-08-28` | $112,566.90 | `-$2,931.05` | 🔴 -2.60% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-06-29` | $108,356.93 | `+$1,278.92` | 🟢 +1.18% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-03-31` | $82,550.01 | `+$27,085.84` | 🟢 +32.81% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-09-27` | $65,769.95 | `+$43,865.90` | 🟢 +66.70% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-08-14` | $124,474.00 | `-$14,838.15` | 🔴 `-11.92%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-09-27` | $109,643.46 | $109,743.91 | $109,064.40 | $109,635.85 | 🔴 -0.01% | `5,501.79 BTC` |
| `2025-09-26` | $108,994.49 | $110,300.00 | $108,620.07 | $109,643.46 | 🟢 +0.60% | `14,243.02 BTC` |
| `2025-09-25` | $113,307.01 | $113,510.23 | $108,631.51 | $108,994.49 | 🔴 -3.81% | `21,231.15 BTC` |
| `2025-09-24` | $111,998.80 | $113,940.00 | $111,042.66 | $113,307.00 | 🟢 +1.17% | `12,369.26 BTC` |
| `2025-09-23` | $112,650.99 | $113,290.50 | $111,458.73 | $111,998.80 | 🔴 -0.58% | `12,301.32 BTC` |
| `2025-09-22` | $115,232.29 | $115,379.25 | $111,800.00 | $112,650.99 | 🔴 -2.24% | `20,781.71 BTC` |
| `2025-09-21` | $115,685.63 | $115,819.06 | $115,188.00 | $115,232.29 | 🔴 -0.39% | `4,511.52 BTC` |

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

*Last Telemetry Sync: `2025-09-27 16:02:00 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
