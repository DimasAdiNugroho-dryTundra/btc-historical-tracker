# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--18%2018:18%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$85,516.41** | 🔴 `-0.84%` | Real-time Aggregate Spot |
| **24h Price Range** | `$84,450.01 — $89,477.61` | `Spread: $5,027.60` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.20 B` | `25,405.42 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.70 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-17` | $86,243.22 | `-$726.81` | 🔴 -0.84% | Intraday Shift |
| **7 Days** | `2025-12-11` | $92,513.38 | `-$6,996.97` | 🔴 -7.56% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-18` | $92,960.83 | `-$7,444.42` | 🔴 -8.01% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-19` | $115,632.38 | `-$30,115.97` | 🔴 -26.04% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-06-21` | $102,120.01 | `-$16,603.60` | 🔴 -16.26% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-18` | $100,204.01 | `-$14,687.60` | 🔴 -14.66% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$40,683.22` | 🔴 `-32.24%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-18` | $86,243.23 | $89,477.61 | $84,450.01 | $85,516.41 | 🔴 -0.84% | `25,405.42 BTC` |
| `2025-12-17` | $87,863.43 | $90,365.85 | $85,314.00 | $86,243.22 | 🔴 -1.84% | `19,834.12 BTC` |
| `2025-12-16` | $86,432.08 | $88,175.98 | $85,266.00 | $87,863.42 | 🟢 +1.66% | `18,456.05 BTC` |
| `2025-12-15` | $88,172.16 | $90,052.64 | $85,146.64 | $86,432.08 | 🔴 -1.97% | `19,778.69 BTC` |
| `2025-12-14` | $90,240.00 | $90,472.40 | $87,577.36 | $88,172.17 | 🔴 -2.29% | `9,416.94 BTC` |
| `2025-12-13` | $90,268.43 | $90,634.55 | $89,766.39 | $90,240.01 | 🔴 -0.03% | `5,895.71 BTC` |
| `2025-12-12` | $92,513.38 | $92,754.00 | $89,480.00 | $90,268.42 | 🔴 -2.43% | `16,679.19 BTC` |

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

*Last Telemetry Sync: `2025-12-18 18:18:50 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
