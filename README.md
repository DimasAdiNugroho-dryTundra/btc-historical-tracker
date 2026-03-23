# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--03--23%2020:06%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$70,906.45** | 🟢 `+4.49%` | Real-time Aggregate Spot |
| **24h Price Range** | `$67,445.18 — $71,817.09` | `Spread: $4,371.91` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.98 B` | `28,335.09 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.41 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-03-22` | $67,859.00 | `+$3,047.45` | 🟢 +4.49% | Intraday Shift |
| **7 Days** | `2026-03-16` | $74,884.67 | `-$3,978.22` | 🔴 -5.31% | Weekly Momentum |
| **30 Days (1M)** | `2026-02-21` | $67,975.93 | `+$2,930.52` | 🟢 +4.31% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-12-23` | $87,486.00 | `-$16,579.55` | 🔴 -18.95% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-09-24` | $113,307.00 | `-$42,400.55` | 🔴 -37.42% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-03-23` | $86,082.50 | `-$15,176.05` | 🔴 -17.63% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$55,293.18` | 🔴 `-43.81%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-03-23` | $67,859.00 | $71,817.09 | $67,445.18 | $70,906.45 | 🟢 +4.49% | `28,335.09 BTC` |
| `2026-03-22` | $68,918.12 | $69,588.79 | $67,360.66 | $67,859.00 | 🔴 -1.54% | `14,843.79 BTC` |
| `2026-03-21` | $70,510.73 | $71,100.94 | $68,571.42 | $68,918.12 | 🔴 -2.26% | `13,397.17 BTC` |
| `2026-03-20` | $69,930.01 | $71,367.00 | $69,388.00 | $70,510.73 | 🟢 +0.83% | `18,121.17 BTC` |
| `2026-03-19` | $71,246.55 | $71,613.79 | $68,793.35 | $69,930.00 | 🔴 -1.85% | `22,364.82 BTC` |
| `2026-03-18` | $73,909.37 | $74,672.34 | $70,500.00 | $71,246.54 | 🔴 -3.60% | `23,392.88 BTC` |
| `2026-03-17` | $74,884.67 | $76,000.00 | $73,399.19 | $73,909.36 | 🔴 -1.30% | `24,521.27 BTC` |

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

*Last Telemetry Sync: `2026-03-23 20:06:07 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
