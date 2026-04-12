# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--04--12%2020:28%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$70,740.98** | 🔴 `-3.15%` | Real-time Aggregate Spot |
| **24h Price Range** | `$70,505.88 — $73,137.24` | `Spread: $2,631.36` | Intraday Volatility Band |
| **24h Trading Volume** | `$962.83 M` | `13,472.47 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.40 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-04-11` | $73,043.16 | `-$2,302.18` | 🔴 -3.15% | Intraday Shift |
| **7 Days** | `2026-04-05` | $69,034.18 | `+$1,706.80` | 🟢 +2.47% | Weekly Momentum |
| **30 Days (1M)** | `2026-03-13` | $70,930.00 | `-$189.02` | 🔴 -0.27% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-01-12` | $91,296.20 | `-$20,555.22` | 🔴 -22.51% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-10-14` | $113,028.14 | `-$42,287.16` | 🔴 -37.41% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-04-12` | $85,276.90 | `-$14,535.92` | 🔴 -17.05% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$55,458.65` | 🔴 `-43.95%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-04-12` | $73,043.16 | $73,137.24 | $70,505.88 | $70,740.98 | 🔴 -3.15% | `13,472.47 BTC` |
| `2026-04-11` | $72,962.71 | $73,790.00 | $72,513.09 | $73,043.16 | 🟢 +0.11% | `9,070.94 BTC` |
| `2026-04-10` | $71,787.98 | $73,434.00 | $71,426.15 | $72,962.70 | 🟢 +1.64% | `17,372.63 BTC` |
| `2026-04-09` | $71,069.93 | $73,145.00 | $70,466.00 | $71,787.97 | 🟢 +1.01% | `18,158.42 BTC` |
| `2026-04-08` | $71,924.22 | $72,857.00 | $70,707.23 | $71,069.93 | 🔴 -1.19% | `19,802.69 BTC` |
| `2026-04-07` | $68,853.66 | $72,761.00 | $67,732.01 | $71,924.22 | 🟢 +4.46% | `23,750.50 BTC` |
| `2026-04-06` | $69,034.18 | $70,351.46 | $68,300.00 | $68,853.66 | 🔴 -0.26% | `20,281.61 BTC` |

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

*Last Telemetry Sync: `2026-04-12 20:28:16 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
