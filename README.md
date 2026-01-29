# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--01--29%2010:44%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$84,650.16** | 🔴 `-5.21%` | Real-time Aggregate Spot |
| **24h Price Range** | `$83,383.33 — $89,348.00` | `Spread: $5,964.67` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.61 B` | `30,431.38 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.68 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-01-28` | $89,299.99 | `-$4,649.83` | 🔴 -5.21% | Intraday Shift |
| **7 Days** | `2026-01-22` | $89,559.67 | `-$4,909.51` | 🔴 -5.48% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-30` | $88,485.49 | `-$3,835.33` | 🔴 -4.33% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-31` | $109,608.01 | `-$24,957.85` | 🔴 -22.77% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-08-02` | $112,546.35 | `-$27,896.19` | 🔴 -24.79% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-01-29` | $103,733.24 | `-$19,083.08` | 🔴 -18.40% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$41,549.47` | 🔴 `-32.92%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-01-29` | $89,300.00 | $89,348.00 | $83,383.33 | $84,650.16 | 🔴 -5.21% | `30,431.38 BTC` |
| `2026-01-28` | $89,249.99 | $90,600.00 | $88,833.65 | $89,299.99 | 🟢 +0.06% | `14,332.19 BTC` |
| `2026-01-27` | $88,347.08 | $89,523.16 | $87,304.33 | $89,250.00 | 🟢 +1.02% | `13,125.40 BTC` |
| `2026-01-26` | $86,670.36 | $88,860.00 | $86,509.63 | $88,347.08 | 🟢 +1.93% | `17,766.51 BTC` |
| `2026-01-25` | $89,225.34 | $89,319.13 | $86,074.72 | $86,670.36 | 🔴 -2.86% | `14,426.22 BTC` |
| `2026-01-24` | $89,600.26 | $89,957.39 | $89,162.08 | $89,225.34 | 🔴 -0.42% | `4,226.57 BTC` |
| `2026-01-23` | $89,559.68 | $91,224.99 | $88,578.36 | $89,600.26 | 🟢 +0.05% | `13,918.49 BTC` |

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

*Last Telemetry Sync: `2026-01-29 10:44:14 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
