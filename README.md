# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--09--25%2003:59%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$84,200.45** | 🔴 `-0.22%` | Real-time Aggregate Spot |
| **24h Price Range** | `$84,037.70 — $84,882.18` | `Spread: $844.48` | Intraday Volatility Band |
| **24h Trading Volume** | `$102.46 M` | `1,216.82 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.67 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-09-24` | $84,385.46 | `-$185.01` | 🔴 -0.22% | Intraday Shift |
| **7 Days** | `2026-09-18` | $80,875.04 | `+$3,325.41` | 🟢 +4.11% | Weekly Momentum |
| **30 Days (1M)** | `2026-08-26` | $79,026.18 | `+$5,174.27` | 🟢 +6.55% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-06-27` | $59,934.84 | `+$24,265.61` | 🟢 +40.49% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-03-29` | $65,956.94 | `+$18,243.51` | 🟢 +27.66% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-10-11` | $110,768.89 | `-$26,568.44` | 🔴 -23.99% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-27` | $116,410.06 | `-$32,209.61` | 🔴 `-27.67%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-09-25` | $84,385.47 | $84,882.18 | $84,037.70 | $84,200.45 | 🔴 -0.22% | `1,216.82 BTC` |
| `2026-09-24` | $84,378.31 | $84,929.78 | $82,708.96 | $84,385.46 | 🟢 +0.01% | `6,839.38 BTC` |
| `2026-09-23` | $86,198.05 | $87,282.81 | $83,513.00 | $84,378.31 | 🔴 -2.11% | `7,836.10 BTC` |
| `2026-09-22` | $86,594.94 | $86,734.00 | $85,059.28 | $86,198.05 | 🔴 -0.46% | `8,943.88 BTC` |
| `2026-09-21` | $81,160.33 | $87,397.00 | $80,837.42 | $86,594.94 | 🟢 +6.70% | `14,077.54 BTC` |
| `2026-09-20` | $81,233.91 | $81,472.04 | $80,085.00 | $81,159.64 | 🔴 -0.09% | `3,612.27 BTC` |
| `2026-09-19` | $80,875.04 | $81,925.00 | $80,822.48 | $81,233.91 | 🟢 +0.44% | `3,325.31 BTC` |

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

*Last Telemetry Sync: `2026-09-25 03:59:10 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
