# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--10--30%2012:46%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$108,322.88** | 🔴 `-1.54%` | Real-time Aggregate Spot |
| **24h Price Range** | `$106,304.34 — $111,592.00` | `Spread: $5,287.66` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.83 B` | `25,988.83 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.15 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-10-29` | $110,021.29 | `-$1,698.41` | 🔴 -1.54% | Intraday Shift |
| **7 Days** | `2025-10-23` | $110,078.18 | `-$1,755.30` | 🔴 -1.59% | Weekly Momentum |
| **30 Days (1M)** | `2025-09-30` | $114,048.93 | `-$5,726.05` | 🔴 -5.02% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-08-01` | $113,297.93 | `-$4,975.05` | 🔴 -4.39% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-05-03` | $95,856.42 | `+$12,466.46` | 🟢 +13.01% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-10-30` | $72,344.74 | `+$35,978.14` | 🟢 +49.73% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$17,876.75` | 🔴 `-14.17%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-10-30` | $110,021.30 | $111,592.00 | $106,304.34 | $108,322.88 | 🔴 -1.54% | `25,988.83 BTC` |
| `2025-10-29` | $112,898.44 | $113,643.73 | $109,200.00 | $110,021.29 | 🔴 -2.55% | `21,079.71 BTC` |
| `2025-10-28` | $114,107.65 | $116,086.00 | $112,211.00 | $112,898.45 | 🔴 -1.06% | `15,523.42 BTC` |
| `2025-10-27` | $114,559.41 | $116,400.00 | $113,830.01 | $114,107.65 | 🔴 -0.39% | `21,450.23 BTC` |
| `2025-10-26` | $111,646.27 | $115,466.80 | $111,260.45 | $114,559.40 | 🟢 +2.61% | `13,454.48 BTC` |
| `2025-10-25` | $111,004.90 | $111,943.19 | $110,672.86 | $111,646.27 | 🟢 +0.58% | `6,407.97 BTC` |
| `2025-10-24` | $110,078.19 | $112,104.98 | $109,700.01 | $111,004.89 | 🟢 +0.84% | `15,005.17 BTC` |

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

*Last Telemetry Sync: `2025-10-30 12:46:14 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
