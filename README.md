# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--10--25%2017:21%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$111,646.27** | 🟢 `+0.58%` | Real-time Aggregate Spot |
| **24h Price Range** | `$110,672.86 — $111,943.19` | `Spread: $1,270.33` | Intraday Volatility Band |
| **24h Trading Volume** | `$714.20 M` | `6,407.97 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.22 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-10-24` | $111,004.89 | `+$641.38` | 🟢 +0.58% | Intraday Shift |
| **7 Days** | `2025-10-18` | $107,185.01 | `+$4,461.26` | 🟢 +4.16% | Weekly Momentum |
| **30 Days (1M)** | `2025-09-25` | $108,994.49 | `+$2,651.78` | 🟢 +2.43% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-07-27` | $119,415.55 | `-$7,769.28` | 🔴 -6.51% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-04-28` | $95,011.18 | `+$16,635.09` | 🟢 +17.51% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-10-25` | $66,698.33 | `+$44,947.94` | 🟢 +67.39% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$14,553.36` | 🔴 `-11.53%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-10-25` | $111,004.90 | $111,943.19 | $110,672.86 | $111,646.27 | 🟢 +0.58% | `6,407.97 BTC` |
| `2025-10-24` | $110,078.19 | $112,104.98 | $109,700.01 | $111,004.89 | 🟢 +0.84% | `15,005.17 BTC` |
| `2025-10-23` | $107,567.45 | $111,293.61 | $107,500.00 | $110,078.18 | 🟢 +2.33% | `17,573.09 BTC` |
| `2025-10-22` | $108,297.66 | $109,163.88 | $106,666.69 | $107,567.44 | 🔴 -0.67% | `28,610.78 BTC` |
| `2025-10-21` | $110,532.09 | $114,000.00 | $107,473.72 | $108,297.67 | 🔴 -2.02% | `37,228.02 BTC` |
| `2025-10-20` | $108,642.77 | $111,705.56 | $107,402.52 | $110,532.09 | 🟢 +1.74% | `19,193.44 BTC` |
| `2025-10-19` | $107,185.00 | $109,450.07 | $106,103.36 | $108,642.78 | 🟢 +1.36% | `15,480.66 BTC` |

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

*Last Telemetry Sync: `2025-10-25 17:21:15 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
