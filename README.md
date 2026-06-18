# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--06--18%2022:08%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$62,958.01** | 🔴 `-2.40%` | Real-time Aggregate Spot |
| **24h Price Range** | `$62,272.07 — $64,806.00` | `Spread: $2,533.93` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.08 B` | `16,935.60 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.25 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-06-17` | $64,509.40 | `-$1,551.39` | 🔴 -2.40% | Intraday Shift |
| **7 Days** | `2026-06-11` | $63,625.99 | `-$667.98` | 🔴 -1.05% | Weekly Momentum |
| **30 Days (1M)** | `2026-05-19` | $76,834.36 | `-$13,876.35` | 🔴 -18.06% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-03-20` | $70,510.73 | `-$7,552.72` | 🔴 -10.71% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-12-20` | $88,360.90 | `-$25,402.89` | 🔴 -28.75% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-06-18` | $104,886.78 | `-$41,928.77` | 🔴 -39.98% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$63,241.62` | 🔴 `-50.11%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-06-18` | $64,509.40 | $64,806.00 | $62,272.07 | $62,958.01 | 🔴 -2.40% | `16,935.60 BTC` |
| `2026-06-17` | $65,675.02 | $66,445.93 | $63,915.77 | $64,509.40 | 🔴 -1.77% | `19,048.65 BTC` |
| `2026-06-16` | $66,328.74 | $66,992.00 | $65,360.92 | $65,675.01 | 🔴 -0.99% | `14,302.06 BTC` |
| `2026-06-15` | $65,746.45 | $67,292.15 | $65,354.00 | $66,328.74 | 🟢 +0.89% | `18,559.80 BTC` |
| `2026-06-14` | $64,458.01 | $65,800.00 | $63,678.83 | $65,746.45 | 🟢 +2.00% | `13,203.03 BTC` |
| `2026-06-13` | $63,580.00 | $64,762.77 | $63,418.66 | $64,458.01 | 🟢 +1.38% | `9,960.74 BTC` |
| `2026-06-12` | $63,626.00 | $64,394.44 | $62,829.81 | $63,580.01 | 🔴 -0.07% | `16,397.05 BTC` |

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

*Last Telemetry Sync: `2026-06-18 22:08:21 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
