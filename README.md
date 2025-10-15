# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--10--15%2022:12%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$110,763.28** | 🔴 `-2.00%` | Real-time Aggregate Spot |
| **24h Price Range** | `$110,164.00 — $113,612.35` | `Spread: $3,448.35` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.57 B` | `22,986.49 BTC` | 24h Spot Pair Turnover |
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
| **24 Hours** | `2025-10-14` | $113,028.14 | `-$2,264.86` | 🔴 -2.00% | Intraday Shift |
| **7 Days** | `2025-10-08` | $123,306.00 | `-$12,542.72` | 🔴 -10.17% | Weekly Momentum |
| **30 Days (1M)** | `2025-09-15` | $115,349.71 | `-$4,586.43` | 🔴 -3.98% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-07-17` | $119,177.56 | `-$8,414.28` | 🔴 -7.06% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-04-18` | $84,474.69 | `+$26,288.59` | 🟢 +31.12% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-10-15` | $67,074.14 | `+$43,689.14` | 🟢 +65.14% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$15,436.35` | 🔴 `-12.23%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-10-15` | $113,028.13 | $113,612.35 | $110,164.00 | $110,763.28 | 🔴 -2.00% | `22,986.49 BTC` |
| `2025-10-14` | $115,166.00 | $115,409.96 | $109,866.00 | $113,028.14 | 🔴 -1.86% | `31,870.33 BTC` |
| `2025-10-13` | $114,958.81 | $115,963.81 | $113,616.50 | $115,166.00 | 🟢 +0.18% | `22,557.24 BTC` |
| `2025-10-12` | $110,644.40 | $115,770.00 | $109,565.06 | $114,958.80 | 🟢 +3.90% | `32,255.30 BTC` |
| `2025-10-11` | $112,774.49 | $113,322.39 | $109,561.59 | $110,644.40 | 🔴 -1.89% | `35,448.52 BTC` |
| `2025-10-10` | $121,662.41 | $122,550.00 | $102,000.00 | $112,774.50 | 🔴 -7.31% | `64,171.94 BTC` |
| `2025-10-09` | $123,306.01 | $123,762.94 | $119,651.47 | $121,662.40 | 🔴 -1.33% | `21,559.36 BTC` |

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

*Last Telemetry Sync: `2025-10-15 22:12:28 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
