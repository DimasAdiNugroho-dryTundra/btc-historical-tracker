# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--31%2017:16%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$87,648.22** | 🔴 `-0.95%` | Real-time Aggregate Spot |
| **24h Price Range** | `$87,250.00 — $89,200.00` | `Spread: $1,950.00` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.02 B` | `11,558.62 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.74 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-30` | $88,485.49 | `-$837.27` | 🔴 -0.95% | Intraday Shift |
| **7 Days** | `2025-12-24` | $87,669.45 | `-$21.23` | 🔴 -0.02% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-01` | $86,286.01 | `+$1,362.21` | 🟢 +1.58% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-02` | $120,529.35 | `-$32,881.13` | 🔴 -27.28% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-07-04` | $107,984.24 | `-$20,336.02` | 🔴 -18.83% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-31` | $93,576.00 | `-$5,927.78` | 🔴 -6.33% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$38,551.41` | 🔴 `-30.55%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-31` | $88,485.50 | $89,200.00 | $87,250.00 | $87,648.22 | 🔴 -0.95% | `11,558.62 BTC` |
| `2025-12-30` | $87,237.13 | $89,400.00 | $86,845.66 | $88,485.49 | 🟢 +1.43% | `13,105.91 BTC` |
| `2025-12-29` | $87,952.71 | $90,406.08 | $86,806.50 | $87,237.13 | 🔴 -0.81% | `19,894.99 BTC` |
| `2025-12-28` | $87,877.00 | $88,088.75 | $87,435.00 | $87,952.71 | 🟢 +0.09% | `4,446.29 BTC` |
| `2025-12-27` | $87,369.56 | $87,984.00 | $87,253.05 | $87,877.01 | 🟢 +0.58% | `4,469.55 BTC` |
| `2025-12-26` | $87,225.27 | $89,567.75 | $86,655.08 | $87,369.56 | 🟢 +0.17% | `18,344.62 BTC` |
| `2025-12-25` | $87,669.44 | $88,592.74 | $86,934.72 | $87,225.27 | 🔴 -0.51% | `7,096.58 BTC` |

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

*Last Telemetry Sync: `2025-12-31 17:16:44 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
