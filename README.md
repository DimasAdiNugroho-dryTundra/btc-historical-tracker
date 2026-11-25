# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--25%2007:32%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$58,944.93** | 🔴 `-1.33%` | Real-time Aggregate Spot |
| **24h Price Range** | `$58,851.92 — $59,749.17` | `Spread: $897.25` | Intraday Volatility Band |
| **24h Trading Volume** | `$172.76 M` | `2,930.83 BTC` | 24h Spot Pair Turnover |
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
| **24 Hours** | `2026-11-24` | $59,740.87 | `-$795.94` | 🔴 -1.33% | Intraday Shift |
| **7 Days** | `2026-11-18` | $62,981.71 | `-$4,036.78` | 🔴 -6.41% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-26` | $80,008.79 | `-$21,063.86` | 🔴 -26.33% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-27` | $80,275.34 | `-$21,330.41` | 🔴 -26.57% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-29` | $73,366.77 | `-$14,421.84` | 🔴 -19.66% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-11` | $92,542.00 | `-$33,597.07` | 🔴 -36.30% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$49,955.07` | 🔴 `-45.87%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25` | $59,741.39 | $59,749.17 | $58,851.92 | $58,944.93 | 🔴 -1.33% | `2,930.83 BTC` |
| `2026-11-24` | $61,190.81 | $61,603.49 | $59,189.67 | $59,740.87 | 🔴 -2.37% | `13,455.73 BTC` |
| `2026-11-23` | $61,163.01 | $64,533.96 | $60,286.92 | $61,189.97 | 🟢 +0.04% | `16,914.31 BTC` |
| `2026-11-22` | $60,086.00 | $61,568.11 | $58,636.18 | $61,163.01 | 🟢 +1.79% | `8,857.87 BTC` |
| `2026-11-21` | $58,815.33 | $60,883.03 | $55,106.00 | $60,086.00 | 🟢 +2.16% | `17,117.92 BTC` |
| `2026-11-20` | $61,911.58 | $62,562.15 | $57,655.17 | $58,814.99 | 🔴 -5.00% | `23,600.20 BTC` |
| `2026-11-19` | $62,981.71 | $64,023.69 | $61,350.00 | $61,913.23 | 🔴 -1.70% | `13,357.18 BTC` |

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

*Last Telemetry Sync: `2026-11-25 07:32:36 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
