# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--06--17%2021:37%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$64,509.40** | 🔴 `-1.77%` | Real-time Aggregate Spot |
| **24h Price Range** | `$63,915.77 — $66,445.93` | `Spread: $2,530.16` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.24 B` | `19,048.65 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.28 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-06-16` | $65,675.01 | `-$1,165.61` | 🔴 -1.77% | Intraday Shift |
| **7 Days** | `2026-06-10` | $61,510.99 | `+$2,998.41` | 🟢 +4.87% | Weekly Momentum |
| **30 Days (1M)** | `2026-05-18` | $77,001.87 | `-$12,492.47` | 🔴 -16.22% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-03-19` | $69,930.00 | `-$5,420.60` | 🔴 -7.75% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-12-19` | $88,136.94 | `-$23,627.54` | 🔴 -26.81% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-06-17` | $104,551.17 | `-$40,041.77` | 🔴 -38.30% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$61,690.23` | 🔴 `-48.88%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-06-17` | $65,675.02 | $66,445.93 | $63,915.77 | $64,509.40 | 🔴 -1.77% | `19,048.65 BTC` |
| `2026-06-16` | $66,328.74 | $66,992.00 | $65,360.92 | $65,675.01 | 🔴 -0.99% | `14,302.06 BTC` |
| `2026-06-15` | $65,746.45 | $67,292.15 | $65,354.00 | $66,328.74 | 🟢 +0.89% | `18,559.80 BTC` |
| `2026-06-14` | $64,458.01 | $65,800.00 | $63,678.83 | $65,746.45 | 🟢 +2.00% | `13,203.03 BTC` |
| `2026-06-13` | $63,580.00 | $64,762.77 | $63,418.66 | $64,458.01 | 🟢 +1.38% | `9,960.74 BTC` |
| `2026-06-12` | $63,626.00 | $64,394.44 | $62,829.81 | $63,580.01 | 🔴 -0.07% | `16,397.05 BTC` |
| `2026-06-11` | $61,510.99 | $63,933.02 | $61,510.99 | $63,625.99 | 🟢 +3.44% | `17,380.95 BTC` |

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

*Last Telemetry Sync: `2026-06-17 21:37:34 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
