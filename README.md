# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--04--20%2020:34%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$75,840.97** | 🟢 `+2.76%` | Real-time Aggregate Spot |
| **24h Price Range** | `$73,724.31 — $76,558.62` | `Spread: $2,834.31` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.28 B` | `16,993.41 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.51 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-04-19` | $73,801.79 | `+$2,039.18` | 🟢 +2.76% | Intraday Shift |
| **7 Days** | `2026-04-13` | $74,417.99 | `+$1,422.98` | 🟢 +1.91% | Weekly Momentum |
| **30 Days (1M)** | `2026-03-21` | $68,918.12 | `+$6,922.85` | 🟢 +10.05% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-01-20` | $88,427.66 | `-$12,586.69` | 🔴 -14.23% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-10-22` | $107,567.44 | `-$31,726.47` | 🔴 -29.49% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-04-20` | $85,179.24 | `-$9,338.27` | 🔴 -10.96% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$50,358.66` | 🔴 `-39.90%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-04-20` | $73,801.80 | $76,558.62 | $73,724.31 | $75,840.97 | 🟢 +2.76% | `16,993.41 BTC` |
| `2026-04-19` | $75,691.76 | $76,240.66 | $73,762.90 | $73,801.79 | 🔴 -2.50% | `11,369.82 BTC` |
| `2026-04-18` | $77,072.01 | $77,420.08 | $75,445.16 | $75,691.76 | 🔴 -1.79% | `9,141.84 BTC` |
| `2026-04-17` | $75,154.28 | $78,333.00 | $74,529.40 | $77,072.00 | 🟢 +2.55% | `25,941.37 BTC` |
| `2026-04-16` | $74,809.99 | $75,534.76 | $73,309.85 | $75,154.29 | 🟢 +0.46% | `17,088.69 BTC` |
| `2026-04-15` | $74,131.55 | $75,425.00 | $73,514.00 | $74,809.99 | 🟢 +0.92% | `14,425.04 BTC` |
| `2026-04-14` | $74,418.00 | $76,038.00 | $73,795.47 | $74,131.55 | 🔴 -0.38% | `26,532.94 BTC` |

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

*Last Telemetry Sync: `2026-04-20 20:34:28 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
