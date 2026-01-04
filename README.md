# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--01--04%2011:32%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$91,529.73** | 🟢 `+0.99%` | Real-time Aggregate Spot |
| **24h Price Range** | `$90,628.00 — $91,810.00` | `Spread: $1,182.00` | Intraday Volatility Band |
| **24h Trading Volume** | `$952.16 M` | `10,426.53 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.82 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-01-03` | $90,628.01 | `+$901.72` | 🟢 +0.99% | Intraday Shift |
| **7 Days** | `2025-12-28` | $87,952.71 | `+$3,577.02` | 🟢 +4.07% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-05` | $89,330.04 | `+$2,199.69` | 🟢 +2.46% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-06` | $124,658.54 | `-$33,128.81` | 🔴 -26.58% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-07-08` | $108,922.98 | `-$17,393.25` | 🔴 -15.97% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-01-04` | $98,220.50 | `-$6,690.77` | 🔴 -6.81% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$34,669.90` | 🔴 `-27.47%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-01-04` | $90,628.01 | $91,810.00 | $90,628.00 | $91,529.73 | 🟢 +0.99% | `10,426.53 BTC` |
| `2026-01-03` | $89,995.14 | $90,741.16 | $89,314.01 | $90,628.01 | 🟢 +0.70% | `7,057.47 BTC` |
| `2026-01-02` | $88,839.05 | $90,961.81 | $88,379.88 | $89,995.13 | 🟢 +1.30% | `17,396.97 BTC` |
| `2026-01-01` | $87,648.21 | $88,919.45 | $87,550.43 | $88,839.04 | 🟢 +1.36% | `6,279.57 BTC` |
| `2025-12-31` | $88,485.50 | $89,200.00 | $87,250.00 | $87,648.22 | 🔴 -0.95% | `11,558.62 BTC` |
| `2025-12-30` | $87,237.13 | $89,400.00 | $86,845.66 | $88,485.49 | 🟢 +1.43% | `13,105.91 BTC` |
| `2025-12-29` | $87,952.71 | $90,406.08 | $86,806.50 | $87,237.13 | 🔴 -0.81% | `19,894.99 BTC` |

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

*Last Telemetry Sync: `2026-01-04 11:32:47 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
