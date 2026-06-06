# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--06--06%2014:55%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$60,884.62** | 🔴 `-0.28%` | Real-time Aggregate Spot |
| **24h Price Range** | `$59,500.00 — $61,530.05` | `Spread: $2,030.05` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.20 B` | `19,795.59 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.21 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-06-05` | $61,056.47 | `-$171.85` | 🔴 -0.28% | Intraday Shift |
| **7 Days** | `2026-05-30` | $73,884.38 | `-$12,999.76` | 🔴 -17.59% | Weekly Momentum |
| **30 Days (1M)** | `2026-05-07` | $80,006.00 | `-$19,121.38` | 🔴 -23.90% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-03-08` | $65,971.20 | `-$5,086.58` | 🔴 -7.71% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-12-08` | $90,634.34 | `-$29,749.72` | 🔴 -32.82% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-06-06` | $104,288.44 | `-$43,403.82` | 🔴 -41.62% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$65,315.01` | 🔴 `-51.76%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-06-06` | $61,056.47 | $61,530.05 | $59,500.00 | $60,884.62 | 🔴 -0.28% | `19,795.59 BTC` |
| `2026-06-05` | $63,885.99 | $63,978.00 | $59,130.91 | $61,056.47 | 🔴 -4.43% | `55,027.29 BTC` |
| `2026-06-04` | $64,142.75 | $64,764.32 | $61,383.56 | $63,885.99 | 🔴 -0.40% | `43,577.18 BTC` |
| `2026-06-03` | $66,760.84 | $67,516.00 | $64,092.49 | $64,142.75 | 🔴 -3.92% | `30,138.31 BTC` |
| `2026-06-02` | $71,408.90 | $71,408.90 | $66,193.00 | $66,760.83 | 🔴 -6.51% | `32,858.20 BTC` |
| `2026-06-01` | $73,674.39 | $74,092.00 | $70,686.68 | $71,408.90 | 🔴 -3.08% | `23,921.09 BTC` |
| `2026-05-31` | $73,884.38 | $74,275.66 | $73,400.00 | $73,674.39 | 🔴 -0.28% | `6,986.46 BTC` |

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

*Last Telemetry Sync: `2026-06-06 14:55:33 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
