# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--11--22%2013:18%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$84,739.74** | 🔴 `-0.46%` | Real-time Aggregate Spot |
| **24h Price Range** | `$83,500.00 — $85,620.00` | `Spread: $2,120.00` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.20 B` | `14,193.93 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.68 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-11-21` | $85,129.43 | `-$389.69` | 🔴 -0.46% | Intraday Shift |
| **7 Days** | `2025-11-15` | $95,596.24 | `-$10,856.50` | 🔴 -11.36% | Weekly Momentum |
| **30 Days (1M)** | `2025-10-23` | $110,078.18 | `-$25,338.44` | 🔴 -23.02% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-08-24` | $113,493.59 | `-$28,753.85` | 🔴 -25.34% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-05-26` | $109,434.79 | `-$24,695.05` | 🔴 -22.57% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-11-22` | $98,892.00 | `-$14,152.26` | 🔴 -14.31% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$41,459.89` | 🔴 `-32.85%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-11-22` | $85,129.42 | $85,620.00 | $83,500.00 | $84,739.74 | 🔴 -0.46% | `14,193.93 BTC` |
| `2025-11-21` | $86,637.22 | $87,498.94 | $80,600.00 | $85,129.43 | 🔴 -1.74% | `72,256.13 BTC` |
| `2025-11-20` | $91,554.96 | $93,160.00 | $86,100.00 | $86,637.23 | 🔴 -5.37% | `39,733.19 BTC` |
| `2025-11-19` | $92,960.83 | $92,980.22 | $88,608.00 | $91,554.96 | 🔴 -1.51% | `32,286.64 BTC` |
| `2025-11-18` | $92,215.14 | $93,836.01 | $89,253.78 | $92,960.83 | 🟢 +0.81% | `39,835.15 BTC` |
| `2025-11-17` | $94,261.45 | $96,043.00 | $91,220.00 | $92,215.14 | 🔴 -2.17% | `39,218.60 BTC` |
| `2025-11-16` | $95,596.23 | $96,635.11 | $93,005.55 | $94,261.44 | 🔴 -1.40% | `23,889.41 BTC` |

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

*Last Telemetry Sync: `2025-11-22 13:18:55 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
