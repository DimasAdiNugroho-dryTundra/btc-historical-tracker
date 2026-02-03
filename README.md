# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--02--03%2013:20%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$75,770.21** | 🔴 `-3.77%` | Real-time Aggregate Spot |
| **24h Price Range** | `$72,945.50 — $79,186.81` | `Spread: $6,241.31` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.99 B` | `39,120.11 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.50 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-02-02` | $78,738.61 | `-$2,968.40` | 🔴 -3.77% | Intraday Shift |
| **7 Days** | `2026-01-27` | $89,250.00 | `-$13,479.79` | 🔴 -15.10% | Weekly Momentum |
| **30 Days (1M)** | `2026-01-04` | $91,529.73 | `-$15,759.52` | 🔴 -17.22% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-11-05` | $103,885.16 | `-$28,114.95` | 🔴 -27.06% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-08-07` | $117,472.01 | `-$41,701.80` | 🔴 -35.50% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-02-03` | $101,328.52 | `-$25,558.31` | 🔴 -25.22% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$50,429.42` | 🔴 `-39.96%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-02-03` | $78,738.60 | $79,186.81 | $72,945.50 | $75,770.21 | 🔴 -3.77% | `39,120.11 BTC` |
| `2026-02-02` | $76,968.22 | $79,360.00 | $74,604.00 | $78,738.61 | 🟢 +2.30% | `42,273.59 BTC` |
| `2026-02-01` | $78,741.10 | $79,424.00 | $75,700.00 | $76,968.21 | 🔴 -2.25% | `25,395.48 BTC` |
| `2026-01-31` | $84,260.50 | $84,270.02 | $75,719.90 | $78,741.09 | 🔴 -6.55% | `39,491.89 BTC` |
| `2026-01-30` | $84,650.16 | $84,735.75 | $81,118.00 | $84,260.49 | 🔴 -0.46% | `35,195.85 BTC` |
| `2026-01-29` | $89,300.00 | $89,348.00 | $83,383.33 | $84,650.16 | 🔴 -5.21% | `30,431.38 BTC` |
| `2026-01-28` | $89,249.99 | $90,600.00 | $88,833.65 | $89,299.99 | 🟢 +0.06% | `14,332.19 BTC` |

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

*Last Telemetry Sync: `2026-02-03 13:20:40 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
