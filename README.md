# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--09--15%2016:21%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$115,349.71** | 🟢 `+0.07%` | Real-time Aggregate Spot |
| **24h Price Range** | `$114,384.00 — $116,757.99` | `Spread: $2,373.99` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.52 B` | `13,212.51 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$2.29 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-09-14` | $115,268.01 | `+$81.70` | 🟢 +0.07% | Intraday Shift |
| **7 Days** | `2025-09-08` | $112,065.23 | `+$3,284.48` | 🟢 +2.93% | Weekly Momentum |
| **30 Days (1M)** | `2025-08-16` | $117,380.66 | `-$2,030.95` | 🔴 -1.73% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-06-17` | $104,551.17 | `+$10,798.54` | 🟢 +10.33% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-03-19` | $86,845.94 | `+$28,503.77` | 🟢 +32.82% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-09-15` | $59,132.00 | `+$56,217.71` | 🟢 +95.07% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-08-14` | $124,474.00 | `-$9,124.29` | 🔴 `-7.33%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-09-15` | $115,268.01 | $116,757.99 | $114,384.00 | $115,349.71 | 🟢 +0.07% | `13,212.51 BTC` |
| `2025-09-14` | $115,918.29 | $116,165.19 | $115,135.00 | $115,268.01 | 🔴 -0.56% | `6,707.60 BTC` |
| `2025-09-13` | $116,029.41 | $116,298.78 | $115,127.27 | $115,918.29 | 🔴 -0.10% | `8,269.40 BTC` |
| `2025-09-12` | $115,482.69 | $116,665.63 | $114,740.99 | $116,029.42 | 🟢 +0.47% | `15,324.11 BTC` |
| `2025-09-11` | $113,960.00 | $115,488.09 | $113,430.00 | $115,482.69 | 🟢 +1.34% | `13,676.73 BTC` |
| `2025-09-10` | $111,546.38 | $114,313.13 | $110,917.45 | $113,960.00 | 🟢 +2.16% | `17,517.42 BTC` |
| `2025-09-09` | $112,065.23 | $113,293.29 | $110,766.66 | $111,546.39 | 🔴 -0.46% | `15,379.28 BTC` |

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

*Last Telemetry Sync: `2025-09-15 16:21:31 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
