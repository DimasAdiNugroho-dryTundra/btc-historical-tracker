# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--09--22%2003:53%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$85,494.71** | 🔴 `-1.27%` | Real-time Aggregate Spot |
| **24h Price Range** | `$85,265.26 — $86,610.96` | `Spread: $1,345.70` | Intraday Volatility Band |
| **24h Trading Volume** | `$102.86 M` | `1,203.15 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.70 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-09-21` | $86,594.94 | `-$1,100.23` | 🔴 -1.27% | Intraday Shift |
| **7 Days** | `2026-09-15` | $75,584.17 | `+$9,910.54` | 🟢 +13.11% | Weekly Momentum |
| **30 Days (1M)** | `2026-08-23` | $77,729.36 | `+$7,765.35` | 🟢 +9.99% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-06-24` | $60,983.13 | `+$24,511.58` | 🟢 +40.19% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-03-26` | $68,769.02 | `+$16,725.69` | 🟢 +24.32% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-10-08` | $123,343.25 | `-$37,848.54` | 🔴 -30.69% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-08` | $124,254.31 | `-$38,759.60` | 🔴 `-31.19%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-09-22` | $86,594.94 | $86,610.96 | $85,265.26 | $85,494.71 | 🔴 -1.27% | `1,203.15 BTC` |
| `2026-09-21` | $81,160.33 | $87,397.00 | $80,837.42 | $86,594.94 | 🟢 +6.70% | `14,077.54 BTC` |
| `2026-09-20` | $81,233.91 | $81,472.04 | $80,085.00 | $81,159.64 | 🔴 -0.09% | `3,612.27 BTC` |
| `2026-09-19` | $80,875.04 | $81,925.00 | $80,822.48 | $81,233.91 | 🟢 +0.44% | `3,325.31 BTC` |
| `2026-09-18` | $76,348.74 | $81,388.47 | $76,205.46 | $80,875.04 | 🟢 +5.93% | `12,360.25 BTC` |
| `2026-09-17` | $76,144.99 | $77,105.42 | $75,921.88 | $76,348.74 | 🟢 +0.27% | `5,353.30 BTC` |
| `2026-09-16` | $75,584.17 | $76,499.99 | $74,911.53 | $76,144.99 | 🟢 +0.74% | `6,945.70 BTC` |

---

### ⚙️ Automation & Pipeline Architecture

- **Automated Execution:** Synced daily at `00:00 UTC` via GitHub Actions (`.github/workflows/update.yml`).
- **Resilient Pipeline:** Cascading multi-exchange API architecture (Binance -> Coinbase -> Kraken -> CoinGecko).
- **Git-Native Telemetry:** Dynamic SVG vector graphics and Markdown dashboards saved directly into Git history.

```
[ GitHub Actions Cron: 00:00 UTC ]
               │
               ▼
   [ fetch_btc.py Executed ] ──► [ Query Multi-Exchange Feeds ]
               │
               ▼
   [ Generate assets/btc_trend.svg & README.md ]
               │
               ▼
   [ Auto Git Commit & Push (main) ]
```

---

<div align="center">

*Last Telemetry Sync: `2026-09-22 03:53:08 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
