# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--12%2010:11%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$90,268.42** | 🔴 `-2.43%` | Real-time Aggregate Spot |
| **24h Price Range** | `$89,480.00 — $92,754.00` | `Spread: $3,274.00` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.52 B` | `16,679.19 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.79 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-11` | $92,513.38 | `-$2,244.96` | 🔴 -2.43% | Intraday Shift |
| **7 Days** | `2025-12-05` | $89,330.04 | `+$938.38` | 🟢 +1.05% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-12` | $101,654.37 | `-$11,385.95` | 🔴 -11.20% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-13` | $115,918.29 | `-$25,649.87` | 🔴 -22.13% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-06-15` | $105,594.01 | `-$15,325.59` | 🔴 -14.51% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-12` | $100,004.29 | `-$9,735.87` | 🔴 -9.74% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$35,931.21` | 🔴 `-28.47%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-12` | $92,513.38 | $92,754.00 | $89,480.00 | $90,268.42 | 🔴 -2.43% | `16,679.19 BTC` |
| `2025-12-11` | $92,015.38 | $93,555.00 | $89,260.63 | $92,513.38 | 🟢 +0.54% | `19,972.59 BTC` |
| `2025-12-10` | $92,678.81 | $94,476.00 | $91,563.15 | $92,015.37 | 🔴 -0.72% | `18,998.68 BTC` |
| `2025-12-09` | $90,634.35 | $94,588.99 | $89,500.00 | $92,678.80 | 🟢 +2.26% | `21,240.43 BTC` |
| `2025-12-08` | $90,395.32 | $92,287.15 | $89,612.00 | $90,634.34 | 🟢 +0.26% | `15,793.64 BTC` |
| `2025-12-07` | $89,236.80 | $91,760.00 | $87,719.28 | $90,395.31 | 🟢 +1.30% | `13,021.11 BTC` |
| `2025-12-06` | $89,330.04 | $90,289.97 | $88,908.01 | $89,236.79 | 🔴 -0.10% | `8,409.50 BTC` |

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

*Last Telemetry Sync: `2025-12-12 10:11:26 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
