# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--28%2006:51%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$59,801.38** | 🔴 `-0.10%` | Real-time Aggregate Spot |
| **24h Price Range** | `$59,537.17 — $60,200.00` | `Spread: $662.83` | Intraday Volatility Band |
| **24h Trading Volume** | `$74.00 M` | `1,237.36 BTC` | 24h Spot Pair Turnover |
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
| **24 Hours** | `2026-11-27` | $59,858.49 | `-$57.11` | 🔴 -0.10% | Intraday Shift |
| **7 Days** | `2026-11-21` | $60,086.00 | `-$284.62` | 🔴 -0.47% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-29` | $77,780.33 | `-$17,978.95` | 🔴 -23.12% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-30` | $77,665.14 | `-$17,863.76` | 🔴 -23.00% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-06-01` | $71,314.42 | `-$11,513.04` | 🔴 -16.14% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-14` | $88,171.61 | `-$28,370.23` | 🔴 -32.18% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$49,098.62` | 🔴 `-45.09%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28` | $59,858.49 | $60,200.00 | $59,537.17 | $59,801.38 | 🔴 -0.10% | `1,237.36 BTC` |
| `2026-11-27` | $60,495.56 | $62,140.28 | $58,700.00 | $59,858.49 | 🔴 -1.05% | `15,239.79 BTC` |
| `2026-11-26` | $60,383.50 | $61,526.89 | $59,842.43 | $60,495.57 | 🟢 +0.19% | `5,928.12 BTC` |
| `2026-11-25` | $59,741.39 | $60,487.00 | $57,208.17 | $60,383.51 | 🟢 +1.07% | `16,694.51 BTC` |
| `2026-11-24` | $61,190.81 | $61,603.49 | $59,189.67 | $59,740.87 | 🔴 -2.37% | `13,455.73 BTC` |
| `2026-11-23` | $61,163.01 | $64,533.96 | $60,286.92 | $61,189.97 | 🟢 +0.04% | `16,914.31 BTC` |
| `2026-11-22` | $60,086.00 | $61,568.11 | $58,636.18 | $61,163.01 | 🟢 +1.79% | `8,857.87 BTC` |

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

*Last Telemetry Sync: `2026-11-28 06:51:07 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
