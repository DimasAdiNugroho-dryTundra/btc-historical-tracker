# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--01--05%2012:00%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$93,859.71** | 🟢 `+2.55%` | Real-time Aggregate Spot |
| **24h Price Range** | `$91,514.81 — $94,789.08` | `Spread: $3,274.27` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.93 B` | `20,673.60 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.86 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-01-04` | $91,529.73 | `+$2,329.98` | 🟢 +2.55% | Intraday Shift |
| **7 Days** | `2025-12-29` | $87,237.13 | `+$6,622.58` | 🟢 +7.59% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-06` | $89,236.79 | `+$4,622.92` | 🟢 +5.18% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-07` | $121,332.95 | `-$27,473.24` | 🔴 -22.64% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-07-09` | $111,233.99 | `-$17,374.28` | 🔴 -15.62% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-01-05` | $98,363.61 | `-$4,503.90` | 🔴 -4.58% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$32,339.92` | 🔴 `-25.63%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-01-05` | $91,529.74 | $94,789.08 | $91,514.81 | $93,859.71 | 🟢 +2.55% | `20,673.60 BTC` |
| `2026-01-04` | $90,628.01 | $91,810.00 | $90,628.00 | $91,529.73 | 🟢 +0.99% | `10,426.53 BTC` |
| `2026-01-03` | $89,995.14 | $90,741.16 | $89,314.01 | $90,628.01 | 🟢 +0.70% | `7,057.47 BTC` |
| `2026-01-02` | $88,839.05 | $90,961.81 | $88,379.88 | $89,995.13 | 🟢 +1.30% | `17,396.97 BTC` |
| `2026-01-01` | $87,648.21 | $88,919.45 | $87,550.43 | $88,839.04 | 🟢 +1.36% | `6,279.57 BTC` |
| `2025-12-31` | $88,485.50 | $89,200.00 | $87,250.00 | $87,648.22 | 🔴 -0.95% | `11,558.62 BTC` |
| `2025-12-30` | $87,237.13 | $89,400.00 | $86,845.66 | $88,485.49 | 🟢 +1.43% | `13,105.91 BTC` |

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

*Last Telemetry Sync: `2026-01-05 12:00:35 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
