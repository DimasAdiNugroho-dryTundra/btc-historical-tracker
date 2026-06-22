# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--06--22%2013:31%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$64,020.01** | 🟢 `+1.12%` | Real-time Aggregate Spot |
| **24h Price Range** | `$63,312.00 — $65,622.83` | `Spread: $2,310.83` | Intraday Volatility Band |
| **24h Trading Volume** | `$995.03 M` | `15,423.11 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.27 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-06-21` | $63,311.99 | `+$708.02` | 🟢 +1.12% | Intraday Shift |
| **7 Days** | `2026-06-15` | $66,328.74 | `-$2,308.73` | 🔴 -3.48% | Weekly Momentum |
| **30 Days (1M)** | `2026-05-23` | $76,752.01 | `-$12,732.00` | 🔴 -16.59% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-03-24` | $70,556.74 | `-$6,536.73` | 🔴 -9.26% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-12-24` | $87,669.45 | `-$23,649.44` | 🔴 -26.98% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-06-22` | $100,963.87 | `-$36,943.86` | 🔴 -36.59% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$62,179.62` | 🔴 `-49.27%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-06-22` | $63,312.00 | $65,622.83 | $63,312.00 | $64,020.01 | 🟢 +1.12% | `15,423.11 BTC` |
| `2026-06-21` | $64,298.01 | $64,588.00 | $63,270.00 | $63,311.99 | 🔴 -1.53% | `8,034.66 BTC` |
| `2026-06-20` | $63,543.90 | $64,388.00 | $63,184.21 | $64,298.01 | 🟢 +1.19% | `9,522.10 BTC` |
| `2026-06-19` | $62,958.01 | $63,666.00 | $62,316.44 | $63,543.91 | 🟢 +0.93% | `14,247.42 BTC` |
| `2026-06-18` | $64,509.40 | $64,806.00 | $62,272.07 | $62,958.01 | 🔴 -2.40% | `16,935.60 BTC` |
| `2026-06-17` | $65,675.02 | $66,445.93 | $63,915.77 | $64,509.40 | 🔴 -1.77% | `19,048.65 BTC` |
| `2026-06-16` | $66,328.74 | $66,992.00 | $65,360.92 | $65,675.01 | 🔴 -0.99% | `14,302.06 BTC` |

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

*Last Telemetry Sync: `2026-06-22 13:31:01 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
