# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--10--14%2010:59%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$113,028.14** | 🔴 `-1.86%` | Real-time Aggregate Spot |
| **24h Price Range** | `$109,866.00 — $115,409.96` | `Spread: $5,543.96` | Intraday Volatility Band |
| **24h Trading Volume** | `$3.58 B` | `31,870.33 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.24 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-10-13` | $115,166.00 | `-$2,137.86` | 🔴 -1.86% | Intraday Shift |
| **7 Days** | `2025-10-07` | $121,332.95 | `-$8,304.81` | 🔴 -6.84% | Weekly Momentum |
| **30 Days (1M)** | `2025-09-14` | $115,268.01 | `-$2,239.87` | 🔴 -1.94% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-07-16` | $118,630.43 | `-$5,602.29` | 🔴 -4.72% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-04-17` | $84,947.91 | `+$28,080.23` | 🟢 +33.06% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-10-14` | $66,083.99 | `+$46,944.15` | 🟢 +71.04% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$13,171.49` | 🔴 `-10.44%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-10-14` | $115,166.00 | $115,409.96 | $109,866.00 | $113,028.14 | 🔴 -1.86% | `31,870.33 BTC` |
| `2025-10-13` | $114,958.81 | $115,963.81 | $113,616.50 | $115,166.00 | 🟢 +0.18% | `22,557.24 BTC` |
| `2025-10-12` | $110,644.40 | $115,770.00 | $109,565.06 | $114,958.80 | 🟢 +3.90% | `32,255.30 BTC` |
| `2025-10-11` | $112,774.49 | $113,322.39 | $109,561.59 | $110,644.40 | 🔴 -1.89% | `35,448.52 BTC` |
| `2025-10-10` | $121,662.41 | $122,550.00 | $102,000.00 | $112,774.50 | 🔴 -7.31% | `64,171.94 BTC` |
| `2025-10-09` | $123,306.01 | $123,762.94 | $119,651.47 | $121,662.40 | 🔴 -1.33% | `21,559.36 BTC` |
| `2025-10-08` | $121,332.96 | $124,197.25 | $121,066.14 | $123,306.00 | 🟢 +1.63% | `17,012.62 BTC` |

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

*Last Telemetry Sync: `2025-10-14 10:59:50 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
