# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--01--28%2018:46%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$89,299.99** | 🟢 `+0.06%` | Real-time Aggregate Spot |
| **24h Price Range** | `$88,833.65 — $90,600.00` | `Spread: $1,766.35` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.28 B` | `14,332.19 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.77 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-01-27` | $89,250.00 | `+$49.99` | 🟢 +0.06% | Intraday Shift |
| **7 Days** | `2026-01-21` | $89,454.73 | `-$154.74` | 🔴 -0.17% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-29` | $87,237.13 | `+$2,062.86` | 🟢 +2.36% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-30` | $108,322.88 | `-$19,022.89` | 🔴 -17.56% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-08-01` | $113,297.93 | `-$23,997.94` | 🔴 -21.18% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-01-28` | $101,335.52 | `-$12,035.53` | 🔴 -11.88% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$36,899.64` | 🔴 `-29.24%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-01-28` | $89,249.99 | $90,600.00 | $88,833.65 | $89,299.99 | 🟢 +0.06% | `14,332.19 BTC` |
| `2026-01-27` | $88,347.08 | $89,523.16 | $87,304.33 | $89,250.00 | 🟢 +1.02% | `13,125.40 BTC` |
| `2026-01-26` | $86,670.36 | $88,860.00 | $86,509.63 | $88,347.08 | 🟢 +1.93% | `17,766.51 BTC` |
| `2026-01-25` | $89,225.34 | $89,319.13 | $86,074.72 | $86,670.36 | 🔴 -2.86% | `14,426.22 BTC` |
| `2026-01-24` | $89,600.26 | $89,957.39 | $89,162.08 | $89,225.34 | 🔴 -0.42% | `4,226.57 BTC` |
| `2026-01-23` | $89,559.68 | $91,224.99 | $88,578.36 | $89,600.26 | 🟢 +0.05% | `13,918.49 BTC` |
| `2026-01-22` | $89,454.73 | $90,359.99 | $88,515.37 | $89,559.67 | 🟢 +0.12% | `10,825.50 BTC` |

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

*Last Telemetry Sync: `2026-01-28 18:46:06 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
