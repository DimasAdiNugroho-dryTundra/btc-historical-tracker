# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--01%2012:48%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$86,286.01** | 🔴 `-4.51%` | Real-time Aggregate Spot |
| **24h Price Range** | `$83,822.76 — $90,417.00` | `Spread: $6,594.24` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.98 B` | `34,509.01 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.71 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-11-30` | $90,360.00 | `-$4,073.99` | 🔴 -4.51% | Intraday Shift |
| **7 Days** | `2025-11-24` | $88,300.01 | `-$2,014.00` | 🔴 -2.28% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-01` | $110,098.10 | `-$23,812.09` | 🔴 -21.63% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-02` | $111,240.01 | `-$24,954.00` | 🔴 -22.43% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-06-04` | $104,696.86 | `-$18,410.85` | 🔴 -17.58% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-01` | $97,185.18 | `-$10,899.17` | 🔴 -11.21% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$39,913.62` | 🔴 `-31.63%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-01` | $90,360.01 | $90,417.00 | $83,822.76 | $86,286.01 | 🔴 -4.51% | `34,509.01 BTC` |
| `2025-11-30` | $90,802.44 | $92,000.01 | $90,336.90 | $90,360.00 | 🔴 -0.49% | `9,687.74 BTC` |
| `2025-11-29` | $90,890.71 | $91,165.65 | $90,155.47 | $90,802.44 | 🔴 -0.10% | `7,429.88 BTC` |
| `2025-11-28` | $91,333.94 | $93,092.00 | $90,180.63 | $90,890.70 | 🔴 -0.49% | `18,830.86 BTC` |
| `2025-11-27` | $90,484.01 | $91,950.00 | $90,089.91 | $91,333.95 | 🟢 +0.94% | `16,833.51 BTC` |
| `2025-11-26` | $87,369.97 | $90,656.08 | $86,306.77 | $90,484.02 | 🟢 +3.56% | `21,675.82 BTC` |
| `2025-11-25` | $88,300.01 | $88,519.99 | $86,116.00 | $87,369.96 | 🔴 -1.05% | `19,567.04 BTC` |

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

*Last Telemetry Sync: `2025-12-01 12:48:43 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
