# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--05--24%2011:59%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$77,064.96** | 🟢 `+0.41%` | Real-time Aggregate Spot |
| **24h Price Range** | `$76,108.00 — $77,543.15` | `Spread: $1,435.15` | Intraday Volatility Band |
| **24h Trading Volume** | `$644.93 M` | `8,398.00 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.53 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-05-23` | $76,752.01 | `+$312.95` | 🟢 +0.41% | Intraday Shift |
| **7 Days** | `2026-05-17` | $77,457.67 | `-$392.71` | 🔴 -0.51% | Weekly Momentum |
| **30 Days (1M)** | `2026-04-24` | $77,437.13 | `-$372.17` | 🔴 -0.48% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-02-23` | $64,656.02 | `+$12,408.94` | 🟢 +19.19% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-11-25` | $87,369.96 | `-$10,305.00` | 🔴 -11.79% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-05-24` | $107,761.91 | `-$30,696.95` | 🔴 -28.49% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$49,134.67` | 🔴 `-38.93%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-05-24` | $76,752.00 | $77,543.15 | $76,108.00 | $77,064.96 | 🟢 +0.41% | `8,398.00 BTC` |
| `2026-05-23` | $75,539.50 | $77,404.18 | $74,289.60 | $76,752.01 | 🟢 +1.61% | `15,086.89 BTC` |
| `2026-05-22` | $77,615.52 | $77,900.00 | $75,359.18 | $75,539.50 | 🔴 -2.67% | `11,272.36 BTC` |
| `2026-05-21` | $77,552.24 | $78,200.00 | $76,719.47 | $77,615.52 | 🟢 +0.08% | `11,318.26 BTC` |
| `2026-05-20` | $76,834.36 | $77,853.04 | $76,516.74 | $77,552.23 | 🟢 +0.93% | `11,296.26 BTC` |
| `2026-05-19` | $77,001.88 | $77,414.62 | $76,144.71 | $76,834.36 | 🔴 -0.22% | `11,024.86 BTC` |
| `2026-05-18` | $77,457.67 | $77,800.00 | $76,051.00 | $77,001.87 | 🔴 -0.59% | `18,745.52 BTC` |

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

*Last Telemetry Sync: `2026-05-24 11:59:20 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
