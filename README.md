# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--05--03%2015:50%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$78,568.57** | 🔴 `-0.15%` | Real-time Aggregate Spot |
| **24h Price Range** | `$78,084.08 — $79,447.00` | `Spread: $1,362.92` | Intraday Volatility Band |
| **24h Trading Volume** | `$584.29 M` | `7,425.79 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.56 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-05-02` | $78,686.85 | `-$118.28` | 🔴 -0.15% | Intraday Shift |
| **7 Days** | `2026-04-26` | $78,657.55 | `-$88.98` | 🔴 -0.11% | Weekly Momentum |
| **30 Days (1M)** | `2026-04-03` | $66,964.30 | `+$11,604.27` | 🟢 +17.33% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-02-02` | $78,738.61 | `-$170.04` | 🔴 -0.22% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-11-04` | $101,497.22 | `-$22,928.65` | 🔴 -22.59% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-05-03` | $95,856.42 | `-$17,287.85` | 🔴 -18.04% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$47,631.06` | 🔴 `-37.74%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-05-03` | $78,686.84 | $79,447.00 | $78,084.08 | $78,568.57 | 🔴 -0.15% | `7,425.79 BTC` |
| `2026-05-02` | $78,231.13 | $79,199.48 | $78,040.00 | $78,686.85 | 🟢 +0.58% | `6,150.88 BTC` |
| `2026-05-01` | $76,346.58 | $78,914.12 | $76,320.42 | $78,231.13 | 🟢 +2.47% | `17,315.47 BTC` |
| `2026-04-30` | $75,780.00 | $76,669.14 | $75,323.65 | $76,346.57 | 🟢 +0.75% | `10,381.82 BTC` |
| `2026-04-29` | $76,342.78 | $77,904.93 | $74,937.52 | $75,780.00 | 🔴 -0.74% | `18,279.93 BTC` |
| `2026-04-28` | $77,371.32 | $77,478.00 | $75,666.60 | $76,342.77 | 🔴 -1.33% | `13,210.72 BTC` |
| `2026-04-27` | $78,657.55 | $79,485.66 | $76,459.64 | $77,371.32 | 🔴 -1.64% | `16,046.92 BTC` |

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

*Last Telemetry Sync: `2026-05-03 15:50:51 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
