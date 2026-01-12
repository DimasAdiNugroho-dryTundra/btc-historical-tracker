# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--01--12%2012:58%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$91,296.20** | 🟢 `+0.31%` | Real-time Aggregate Spot |
| **24h Price Range** | `$90,128.44 — $92,519.95` | `Spread: $2,391.51` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.48 B` | `16,188.08 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.81 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-01-11` | $91,013.65 | `+$282.55` | 🟢 +0.31% | Intraday Shift |
| **7 Days** | `2026-01-05` | $93,859.71 | `-$2,563.51` | 🔴 -2.73% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-13` | $90,240.01 | `+$1,056.19` | 🟢 +1.17% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-14` | $113,028.14 | `-$21,731.94` | 🔴 -19.23% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-07-16` | $118,630.43 | `-$27,334.23` | 🔴 -23.04% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-01-12` | $94,545.06 | `-$3,248.86` | 🔴 -3.44% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$34,903.43` | 🔴 `-27.66%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-01-12` | $91,013.66 | $92,519.95 | $90,128.44 | $91,296.20 | 🟢 +0.31% | `16,188.08 BTC` |
| `2026-01-11` | $90,504.70 | $91,283.89 | $90,236.00 | $91,013.65 | 🟢 +0.56% | `5,477.14 BTC` |
| `2026-01-10` | $90,641.27 | $90,832.00 | $90,404.00 | $90,504.70 | 🔴 -0.15% | `3,104.12 BTC` |
| `2026-01-09` | $91,100.00 | $92,082.55 | $89,694.66 | $90,641.28 | 🔴 -0.50% | `15,590.28 BTC` |
| `2026-01-08` | $91,364.16 | $91,687.99 | $89,311.00 | $91,099.99 | 🔴 -0.29% | `16,132.79 BTC` |
| `2026-01-07` | $93,747.97 | $93,747.97 | $90,675.52 | $91,364.16 | 🔴 -2.54% | `14,276.49 BTC` |
| `2026-01-06` | $93,859.71 | $94,444.44 | $91,262.94 | $93,747.97 | 🔴 -0.12% | `18,546.42 BTC` |

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

*Last Telemetry Sync: `2026-01-12 12:58:56 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
