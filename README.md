# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--22%2005:40%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$58,783.92** | 🔴 `-2.17%` | Real-time Aggregate Spot |
| **24h Price Range** | `$58,666.46 — $60,217.77` | `Spread: $1,551.31` | Intraday Volatility Band |
| **24h Trading Volume** | `$105.48 M` | `1,794.36 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.17 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-11-21` | $60,086.00 | `-$1,302.08` | 🔴 -2.17% | Intraday Shift |
| **7 Days** | `2026-11-15` | $65,315.35 | `-$6,531.43` | 🔴 -10.00% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-23` | $81,078.04 | `-$22,294.12` | 🔴 -27.50% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-24` | $78,981.59 | `-$20,197.67` | 🔴 -25.57% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-26` | $75,826.10 | `-$17,042.18` | 🔴 -22.48% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-08` | $90,653.86 | `-$31,869.94` | 🔴 -35.16% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$50,116.08` | 🔴 `-46.02%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22` | $60,086.00 | $60,217.77 | $58,666.46 | $58,783.92 | 🔴 -2.17% | `1,794.36 BTC` |
| `2026-11-21` | $58,815.33 | $60,883.03 | $55,106.00 | $60,086.00 | 🟢 +2.16% | `17,117.92 BTC` |
| `2026-11-20` | $61,911.58 | $62,562.15 | $57,655.17 | $58,814.99 | 🔴 -5.00% | `23,600.20 BTC` |
| `2026-11-19` | $62,981.71 | $64,023.69 | $61,350.00 | $61,913.23 | 🔴 -1.70% | `13,357.18 BTC` |
| `2026-11-18` | $64,873.18 | $64,933.39 | $62,000.00 | $62,981.71 | 🔴 -2.92% | `12,482.68 BTC` |
| `2026-11-17` | $64,816.79 | $65,383.29 | $63,256.75 | $64,873.18 | 🟢 +0.09% | `11,768.55 BTC` |
| `2026-11-16` | $65,315.35 | $65,626.98 | $63,833.47 | $64,816.79 | 🔴 -0.76% | `13,678.70 BTC` |

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

*Last Telemetry Sync: `2026-11-22 05:40:01 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
