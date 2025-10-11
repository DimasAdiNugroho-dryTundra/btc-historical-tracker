# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--10--11%2021:16%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$110,644.40** | 🔴 `-1.89%` | Real-time Aggregate Spot |
| **24h Price Range** | `$109,561.59 — $113,322.39` | `Spread: $3,760.80` | Intraday Volatility Band |
| **24h Trading Volume** | `$3.96 B` | `35,448.52 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.20 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-10-10` | $112,774.50 | `-$2,130.10` | 🔴 -1.89% | Intraday Shift |
| **7 Days** | `2025-10-04` | $122,391.00 | `-$11,746.60` | 🔴 -9.60% | Weekly Momentum |
| **30 Days (1M)** | `2025-09-11` | $115,482.69 | `-$4,838.29` | 🔴 -4.19% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-07-13` | $119,086.64 | `-$8,442.24` | 🔴 -7.09% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-04-14` | $84,591.58 | `+$26,052.82` | 🟢 +30.80% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-10-11` | $62,540.00 | `+$48,104.40` | 🟢 +76.92% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$15,555.23` | 🔴 `-12.33%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-10-11` | $112,774.49 | $113,322.39 | $109,561.59 | $110,644.40 | 🔴 -1.89% | `35,448.52 BTC` |
| `2025-10-10` | $121,662.41 | $122,550.00 | $102,000.00 | $112,774.50 | 🔴 -7.31% | `64,171.94 BTC` |
| `2025-10-09` | $123,306.01 | $123,762.94 | $119,651.47 | $121,662.40 | 🔴 -1.33% | `21,559.36 BTC` |
| `2025-10-08` | $121,332.96 | $124,197.25 | $121,066.14 | $123,306.00 | 🟢 +1.63% | `17,012.62 BTC` |
| `2025-10-07` | $124,658.54 | $125,126.00 | $120,574.94 | $121,332.95 | 🔴 -2.67% | `21,633.99 BTC` |
| `2025-10-06` | $123,482.32 | $126,199.63 | $123,084.00 | $124,658.54 | 🟢 +0.95% | `19,494.63 BTC` |
| `2025-10-05` | $122,390.99 | $125,708.42 | $122,136.00 | $123,482.31 | 🟢 +0.89% | `22,043.10 BTC` |

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

*Last Telemetry Sync: `2025-10-11 21:16:13 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
