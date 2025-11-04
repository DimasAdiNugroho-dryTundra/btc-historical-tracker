# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--11--04%2008:54%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$101,497.22** | 🔴 `-4.77%` | Real-time Aggregate Spot |
| **24h Price Range** | `$98,944.36 — $107,299.00` | `Spread: $8,354.64` | Intraday Volatility Band |
| **24h Trading Volume** | `$5.20 B` | `50,534.87 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.01 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-11-03` | $106,583.04 | `-$5,085.82` | 🔴 -4.77% | Intraday Shift |
| **7 Days** | `2025-10-28` | $112,898.45 | `-$11,401.23` | 🔴 -10.10% | Weekly Momentum |
| **30 Days (1M)** | `2025-10-05` | $123,482.31 | `-$21,985.09` | 🔴 -17.80% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-08-06` | $114,992.27 | `-$13,495.05` | 🔴 -11.74% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-05-08` | $103,261.60 | `-$1,764.38` | 🔴 -1.71% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-11-04` | $67,850.01 | `+$33,647.21` | 🟢 +49.59% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$24,702.41` | 🔴 `-19.57%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-11-04` | $106,583.05 | $107,299.00 | $98,944.36 | $101,497.22 | 🔴 -4.77% | `50,534.87 BTC` |
| `2025-11-03` | $110,540.69 | $110,750.00 | $105,306.56 | $106,583.04 | 🔴 -3.58% | `28,681.19 BTC` |
| `2025-11-02` | $110,098.10 | $111,250.01 | $109,471.34 | $110,540.68 | 🟢 +0.40% | `12,107.00 BTC` |
| `2025-11-01` | $109,608.01 | $110,564.49 | $109,394.81 | $110,098.10 | 🟢 +0.45% | `7,378.50 BTC` |
| `2025-10-31` | $108,322.87 | $111,190.00 | $108,275.28 | $109,608.01 | 🟢 +1.19% | `21,518.20 BTC` |
| `2025-10-30` | $110,021.30 | $111,592.00 | $106,304.34 | $108,322.88 | 🔴 -1.54% | `25,988.83 BTC` |
| `2025-10-29` | $112,898.44 | $113,643.73 | $109,200.00 | $110,021.29 | 🔴 -2.55% | `21,079.71 BTC` |

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

*Last Telemetry Sync: `2025-11-04 08:54:46 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
