# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--04--25%2021:40%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$77,625.00** | 🟢 `+0.24%` | Real-time Aggregate Spot |
| **24h Price Range** | `$77,140.23 — $77,885.35` | `Spread: $745.12` | Intraday Volatility Band |
| **24h Trading Volume** | `$440.68 M` | `5,685.11 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.54 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-04-24` | $77,437.13 | `+$187.87` | 🟢 +0.24% | Intraday Shift |
| **7 Days** | `2026-04-18` | $75,691.76 | `+$1,933.24` | 🟢 +2.55% | Weekly Momentum |
| **30 Days (1M)** | `2026-03-26` | $68,820.31 | `+$8,804.69` | 🟢 +12.79% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-01-25` | $86,670.36 | `-$9,045.36` | 🔴 -10.44% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-10-27` | $114,107.65 | `-$36,482.65` | 🔴 -31.97% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-04-25` | $94,638.68 | `-$17,013.68` | 🔴 -17.98% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$48,574.63` | 🔴 `-38.49%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-04-25` | $77,437.13 | $77,885.35 | $77,140.23 | $77,625.00 | 🟢 +0.24% | `5,685.11 BTC` |
| `2026-04-24` | $78,257.48 | $78,581.93 | $77,264.08 | $77,437.13 | 🔴 -1.05% | `12,675.14 BTC` |
| `2026-04-23` | $78,178.22 | $78,662.50 | $76,960.00 | $78,257.48 | 🟢 +0.10% | `16,970.80 BTC` |
| `2026-04-22` | $76,336.14 | $79,472.82 | $76,132.95 | $78,178.23 | 🟢 +2.41% | `19,737.51 BTC` |
| `2026-04-21` | $75,840.97 | $76,927.57 | $74,821.57 | $76,336.15 | 🟢 +0.65% | `14,912.57 BTC` |
| `2026-04-20` | $73,801.80 | $76,558.62 | $73,724.31 | $75,840.97 | 🟢 +2.76% | `16,993.41 BTC` |
| `2026-04-19` | $75,691.76 | $76,240.66 | $73,762.90 | $73,801.79 | 🔴 -2.50% | `11,369.82 BTC` |

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

*Last Telemetry Sync: `2026-04-25 21:40:49 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
