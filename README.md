# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--06--02%2015:42%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$66,760.83** | 🔴 `-6.51%` | Real-time Aggregate Spot |
| **24h Price Range** | `$66,193.00 — $71,408.90` | `Spread: $5,215.90` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.25 B` | `32,858.20 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.33 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-06-01` | $71,408.90 | `-$4,648.07` | 🔴 -6.51% | Intraday Shift |
| **7 Days** | `2026-05-26` | $75,930.01 | `-$9,169.18` | 🔴 -12.08% | Weekly Momentum |
| **30 Days (1M)** | `2026-05-03` | $78,568.57 | `-$11,807.74` | 🔴 -15.03% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-03-04` | $72,666.77 | `-$5,905.94` | 🔴 -8.13% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-12-04` | $92,078.06 | `-$25,317.23` | 🔴 -27.50% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-06-02` | $105,857.99 | `-$39,097.16` | 🔴 -36.93% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$59,438.80` | 🔴 `-47.10%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-06-02` | $71,408.90 | $71,408.90 | $66,193.00 | $66,760.83 | 🔴 -6.51% | `32,858.20 BTC` |
| `2026-06-01` | $73,674.39 | $74,092.00 | $70,686.68 | $71,408.90 | 🔴 -3.08% | `23,921.09 BTC` |
| `2026-05-31` | $73,884.38 | $74,275.66 | $73,400.00 | $73,674.39 | 🔴 -0.28% | `6,986.46 BTC` |
| `2026-05-30` | $73,460.78 | $74,143.76 | $73,216.00 | $73,884.38 | 🟢 +0.58% | `7,515.41 BTC` |
| `2026-05-29` | $73,617.52 | $74,514.10 | $72,512.49 | $73,460.78 | 🔴 -0.21% | `18,686.74 BTC` |
| `2026-05-28` | $74,449.31 | $74,590.77 | $72,582.82 | $73,617.51 | 🔴 -1.12% | `21,274.02 BTC` |
| `2026-05-27` | $75,930.01 | $76,174.15 | $74,243.99 | $74,449.30 | 🔴 -1.95% | `16,877.77 BTC` |

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

*Last Telemetry Sync: `2026-06-02 15:42:49 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
