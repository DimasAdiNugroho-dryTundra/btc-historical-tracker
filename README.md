# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--11--26%2015:39%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$90,484.02** | 🟢 `+3.56%` | Real-time Aggregate Spot |
| **24h Price Range** | `$86,306.77 — $90,656.08` | `Spread: $4,349.31` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.92 B` | `21,675.82 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.80 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-11-25` | $87,369.96 | `+$3,114.06` | 🟢 +3.56% | Intraday Shift |
| **7 Days** | `2025-11-19` | $91,554.96 | `-$1,070.94` | 🔴 -1.17% | Weekly Momentum |
| **30 Days (1M)** | `2025-10-27` | $114,107.65 | `-$23,623.63` | 🔴 -20.70% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-08-28` | $112,566.90 | `-$22,082.88` | 🔴 -19.62% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-05-30` | $103,985.48 | `-$13,501.46` | 🔴 -12.98% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-11-26` | $91,965.16 | `-$1,481.14` | 🔴 -1.61% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$35,715.61` | 🔴 `-28.30%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-11-26` | $87,369.97 | $90,656.08 | $86,306.77 | $90,484.02 | 🟢 +3.56% | `21,675.82 BTC` |
| `2025-11-25` | $88,300.01 | $88,519.99 | $86,116.00 | $87,369.96 | 🔴 -1.05% | `19,567.04 BTC` |
| `2025-11-24` | $86,830.00 | $89,228.00 | $85,272.00 | $88,300.01 | 🟢 +1.69% | `24,663.13 BTC` |
| `2025-11-23` | $84,739.75 | $88,127.64 | $84,667.57 | $86,830.00 | 🟢 +2.47% | `19,734.46 BTC` |
| `2025-11-22` | $85,129.42 | $85,620.00 | $83,500.00 | $84,739.74 | 🔴 -0.46% | `14,193.93 BTC` |
| `2025-11-21` | $86,637.22 | $87,498.94 | $80,600.00 | $85,129.43 | 🔴 -1.74% | `72,256.13 BTC` |
| `2025-11-20` | $91,554.96 | $93,160.00 | $86,100.00 | $86,637.23 | 🔴 -5.37% | `39,733.19 BTC` |

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

*Last Telemetry Sync: `2025-11-26 15:39:57 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
