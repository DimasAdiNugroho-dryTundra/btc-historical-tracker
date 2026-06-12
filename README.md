# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--06--12%2018:33%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$63,580.01** | 🔴 `-0.07%` | Real-time Aggregate Spot |
| **24h Price Range** | `$62,829.81 — $64,394.44` | `Spread: $1,564.63` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.04 B` | `16,397.05 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.26 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-06-11` | $63,625.99 | `-$45.98` | 🔴 -0.07% | Intraday Shift |
| **7 Days** | `2026-06-05` | $61,056.47 | `+$2,523.54` | 🟢 +4.13% | Weekly Momentum |
| **30 Days (1M)** | `2026-05-13` | $79,313.61 | `-$15,733.60` | 🔴 -19.84% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-03-14` | $71,211.95 | `-$7,631.94` | 🔴 -10.72% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-12-14` | $88,172.17 | `-$24,592.16` | 🔴 -27.89% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-06-12` | $105,671.73 | `-$42,091.72` | 🔴 -39.83% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$62,619.62` | 🔴 `-49.62%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-06-12` | $63,626.00 | $64,394.44 | $62,829.81 | $63,580.01 | 🔴 -0.07% | `16,397.05 BTC` |
| `2026-06-11` | $61,510.99 | $63,933.02 | $61,510.99 | $63,625.99 | 🟢 +3.44% | `17,380.95 BTC` |
| `2026-06-10` | $61,730.00 | $62,857.99 | $60,755.00 | $61,510.99 | 🔴 -0.35% | `15,998.72 BTC` |
| `2026-06-09` | $63,086.00 | $63,526.01 | $60,780.00 | $61,730.00 | 🔴 -2.15% | `21,636.22 BTC` |
| `2026-06-08` | $63,332.01 | $64,200.00 | $62,408.00 | $63,085.99 | 🔴 -0.39% | `23,053.39 BTC` |
| `2026-06-07` | $60,884.62 | $64,234.68 | $60,746.00 | $63,332.01 | 🟢 +4.02% | `26,612.10 BTC` |
| `2026-06-06` | $61,056.47 | $61,530.05 | $59,500.00 | $60,884.62 | 🔴 -0.28% | `19,795.59 BTC` |

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

*Last Telemetry Sync: `2026-06-12 18:33:51 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
