# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--05--13%2009:59%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$79,313.61** | 🔴 `-1.48%` | Real-time Aggregate Spot |
| **24h Price Range** | `$78,754.65 — $81,324.64` | `Spread: $2,569.99` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.18 B` | `14,810.06 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.57 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-05-12` | $80,504.47 | `-$1,190.86` | 🔴 -1.48% | Intraday Shift |
| **7 Days** | `2026-05-06` | $81,447.01 | `-$2,133.40` | 🔴 -2.62% | Weekly Momentum |
| **30 Days (1M)** | `2026-04-13` | $74,417.99 | `+$4,895.62` | 🟢 +6.58% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-02-12` | $66,272.17 | `+$13,041.44` | 🟢 +19.68% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-11-14` | $94,594.00 | `-$15,280.39` | 🔴 -16.15% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-05-13` | $104,103.72 | `-$24,790.11` | 🔴 -23.81% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$46,886.02` | 🔴 `-37.15%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-05-13` | $80,504.47 | $81,324.64 | $78,754.65 | $79,313.61 | 🔴 -1.48% | `14,810.06 BTC` |
| `2026-05-12` | $81,745.66 | $81,788.00 | $79,843.59 | $80,504.47 | 🔴 -1.52% | `12,386.26 BTC` |
| `2026-05-11` | $82,210.07 | $82,380.00 | $80,462.97 | $81,745.65 | 🔴 -0.56% | `12,951.76 BTC` |
| `2026-05-10` | $80,678.41 | $82,479.32 | $80,279.77 | $82,210.07 | 🟢 +1.90% | `12,034.32 BTC` |
| `2026-05-09` | $80,193.18 | $81,080.00 | $80,129.85 | $80,678.40 | 🟢 +0.61% | `7,548.42 BTC` |
| `2026-05-08` | $80,006.00 | $80,500.00 | $79,181.48 | $80,193.17 | 🟢 +0.23% | `16,001.31 BTC` |
| `2026-05-07` | $81,447.01 | $81,708.32 | $79,500.00 | $80,006.00 | 🔴 -1.77% | `16,154.80 BTC` |

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

*Last Telemetry Sync: `2026-05-13 09:59:19 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
