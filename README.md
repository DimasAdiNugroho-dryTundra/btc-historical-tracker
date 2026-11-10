# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--10%2006:26%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$74,601.65** | 🔴 `-0.87%` | Real-time Aggregate Spot |
| **24h Price Range** | `$74,253.01 — $75,340.23` | `Spread: $1,087.22` | Intraday Volatility Band |
| **24h Trading Volume** | `$118.96 M` | `1,594.56 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.48 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-11-09` | $75,259.28 | `-$657.63` | 🔴 -0.87% | Intraday Shift |
| **7 Days** | `2026-11-03` | $77,336.75 | `-$2,735.10` | 🔴 -3.54% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-11` | $83,678.29 | `-$9,076.64` | 🔴 -10.85% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-12` | $63,411.72 | `+$11,189.93` | 🟢 +17.65% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-14` | $81,079.39 | `-$6,477.74` | 🔴 -7.99% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-11-26` | $90,468.84 | `-$15,867.19` | 🔴 -17.54% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$34,298.35` | 🔴 `-31.50%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10` | $75,257.77 | $75,340.23 | $74,253.01 | $74,601.65 | 🔴 -0.87% | `1,594.56 BTC` |
| `2026-11-09` | $74,756.52 | $75,500.00 | $73,636.00 | $75,259.28 | 🟢 +0.67% | `10,186.64 BTC` |
| `2026-11-08` | $75,753.95 | $76,094.99 | $73,477.00 | $74,754.08 | 🔴 -1.32% | `3,709.69 BTC` |
| `2026-11-07` | $75,731.05 | $76,152.43 | $75,452.88 | $75,753.96 | 🟢 +0.03% | `2,438.27 BTC` |
| `2026-11-06` | $75,969.06 | $76,306.26 | $74,722.00 | $75,731.04 | 🔴 -0.31% | `8,332.69 BTC` |
| `2026-11-05` | $80,428.30 | $80,843.85 | $75,035.10 | $75,969.06 | 🔴 -5.54% | `15,496.67 BTC` |
| `2026-11-04` | $77,336.75 | $81,130.79 | $75,600.64 | $80,428.31 | 🟢 +4.00% | `13,198.74 BTC` |

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

*Last Telemetry Sync: `2026-11-10 06:26:11 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
