# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--24%2008:56%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$60,191.79** | 🔴 `-1.63%` | Real-time Aggregate Spot |
| **24h Price Range** | `$59,366.13 — $61,603.49` | `Spread: $2,237.36` | Intraday Volatility Band |
| **24h Trading Volume** | `$209.07 M` | `3,473.42 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.19 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-11-23` | $61,189.97 | `-$998.18` | 🔴 -1.63% | Intraday Shift |
| **7 Days** | `2026-11-17` | $64,873.18 | `-$4,681.39` | 🔴 -7.22% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-25` | $80,053.16 | `-$19,861.37` | 🔴 -24.81% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-26` | $79,026.18 | `-$18,834.39` | 🔴 -23.83% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-28` | $73,512.56 | `-$13,320.77` | 🔴 -18.12% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-10` | $92,035.99 | `-$31,844.20` | 🔴 -34.60% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$48,708.21` | 🔴 `-44.73%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24` | $61,190.81 | $61,603.49 | $59,366.13 | $60,191.79 | 🔴 -1.63% | `3,473.42 BTC` |
| `2026-11-23` | $61,163.01 | $64,533.96 | $60,286.92 | $61,189.97 | 🟢 +0.04% | `16,914.31 BTC` |
| `2026-11-22` | $60,086.00 | $61,568.11 | $58,636.18 | $61,163.01 | 🟢 +1.79% | `8,857.87 BTC` |
| `2026-11-21` | $58,815.33 | $60,883.03 | $55,106.00 | $60,086.00 | 🟢 +2.16% | `17,117.92 BTC` |
| `2026-11-20` | $61,911.58 | $62,562.15 | $57,655.17 | $58,814.99 | 🔴 -5.00% | `23,600.20 BTC` |
| `2026-11-19` | $62,981.71 | $64,023.69 | $61,350.00 | $61,913.23 | 🔴 -1.70% | `13,357.18 BTC` |
| `2026-11-18` | $64,873.18 | $64,933.39 | $62,000.00 | $62,981.71 | 🔴 -2.92% | `12,482.68 BTC` |

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

*Last Telemetry Sync: `2026-11-24 08:56:00 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
