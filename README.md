# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--01--25%2020:53%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$86,670.36** | 🔴 `-2.86%` | Real-time Aggregate Spot |
| **24h Price Range** | `$86,074.72 — $89,319.13` | `Spread: $3,244.41` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.26 B` | `14,426.22 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.72 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-01-24` | $89,225.34 | `-$2,554.98` | 🔴 -2.86% | Intraday Shift |
| **7 Days** | `2026-01-18` | $93,673.14 | `-$7,002.78` | 🔴 -7.48% | Weekly Momentum |
| **30 Days (1M)** | `2025-12-26` | $87,369.56 | `-$699.20` | 🔴 -0.80% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-10-27` | $114,107.65 | `-$27,437.29` | 🔴 -24.05% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-07-29` | $117,950.76 | `-$31,280.40` | 🔴 -26.52% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-01-25` | $104,746.85 | `-$18,076.49` | 🔴 -17.26% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$39,529.27` | 🔴 `-31.32%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-01-25` | $89,225.34 | $89,319.13 | $86,074.72 | $86,670.36 | 🔴 -2.86% | `14,426.22 BTC` |
| `2026-01-24` | $89,600.26 | $89,957.39 | $89,162.08 | $89,225.34 | 🔴 -0.42% | `4,226.57 BTC` |
| `2026-01-23` | $89,559.68 | $91,224.99 | $88,578.36 | $89,600.26 | 🟢 +0.05% | `13,918.49 BTC` |
| `2026-01-22` | $89,454.73 | $90,359.99 | $88,515.37 | $89,559.67 | 🟢 +0.12% | `10,825.50 BTC` |
| `2026-01-21` | $88,427.66 | $90,574.00 | $87,263.53 | $89,454.73 | 🟢 +1.16% | `20,617.50 BTC` |
| `2026-01-20` | $92,630.99 | $92,870.00 | $87,895.98 | $88,427.66 | 🔴 -4.54% | `22,007.33 BTC` |
| `2026-01-19` | $93,673.14 | $93,673.14 | $91,910.20 | $92,631.00 | 🔴 -1.11% | `14,295.53 BTC` |

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

*Last Telemetry Sync: `2026-01-25 20:53:51 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
