# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--09--21%2003:55%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$81,427.90** | 🟢 `+0.33%` | Real-time Aggregate Spot |
| **24h Price Range** | `$80,837.42 — $82,087.11` | `Spread: $1,249.69` | Intraday Volatility Band |
| **24h Trading Volume** | `$101.86 M` | `1,250.93 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.62 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-09-20` | $81,159.64 | `+$268.26` | 🟢 +0.33% | Intraday Shift |
| **7 Days** | `2026-09-14` | $78,175.01 | `+$3,252.89` | 🟢 +4.16% | Weekly Momentum |
| **30 Days (1M)** | `2026-08-22` | $77,054.44 | `+$4,373.46` | 🟢 +5.68% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-06-23` | $62,644.86 | `+$18,783.04` | 🟢 +29.98% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-03-25` | $71,301.53 | `+$10,126.37` | 🟢 +14.20% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-10-07` | $121,393.95 | `-$39,966.05` | 🔴 -32.92% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-07` | $125,226.34 | `-$43,798.44` | 🔴 `-34.98%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-09-21` | $81,160.33 | $82,087.11 | $80,837.42 | $81,427.90 | 🟢 +0.33% | `1,250.93 BTC` |
| `2026-09-20` | $81,233.91 | $81,472.04 | $80,085.00 | $81,159.64 | 🔴 -0.09% | `3,612.27 BTC` |
| `2026-09-19` | $80,875.04 | $81,925.00 | $80,822.48 | $81,233.91 | 🟢 +0.44% | `3,325.31 BTC` |
| `2026-09-18` | $76,348.74 | $81,388.47 | $76,205.46 | $80,875.04 | 🟢 +5.93% | `12,360.25 BTC` |
| `2026-09-17` | $76,144.99 | $77,105.42 | $75,921.88 | $76,348.74 | 🟢 +0.27% | `5,353.30 BTC` |
| `2026-09-16` | $75,584.17 | $76,499.99 | $74,911.53 | $76,144.99 | 🟢 +0.74% | `6,945.70 BTC` |
| `2026-09-15` | $78,175.00 | $78,242.76 | $74,887.50 | $75,584.17 | 🔴 -3.31% | `10,155.20 BTC` |

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

*Last Telemetry Sync: `2026-09-21 03:55:56 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
