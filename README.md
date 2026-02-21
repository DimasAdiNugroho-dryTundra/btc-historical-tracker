# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--02--21%2012:21%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$67,975.93** | 🔴 `-0.06%` | Real-time Aggregate Spot |
| **24h Price Range** | `$67,534.69 — $68,698.70` | `Spread: $1,164.01` | Intraday Volatility Band |
| **24h Trading Volume** | `$547.59 M` | `8,032.84 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.35 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-02-20` | $68,020.01 | `-$44.08` | 🔴 -0.06% | Intraday Shift |
| **7 Days** | `2026-02-14` | $69,822.95 | `-$1,847.02` | 🔴 -2.65% | Weekly Momentum |
| **30 Days (1M)** | `2026-01-22` | $89,559.67 | `-$21,583.74` | 🔴 -24.10% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-11-23` | $86,830.00 | `-$18,854.07` | 🔴 -21.71% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-08-25` | $110,111.98 | `-$42,136.05` | 🔴 -38.27% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-02-21` | $96,181.98 | `-$28,206.05` | 🔴 -29.33% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$58,223.70` | 🔴 `-46.14%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-02-21` | $68,020.00 | $68,698.70 | $67,534.69 | $67,975.93 | 🔴 -0.06% | `8,032.84 BTC` |
| `2026-02-20` | $67,003.73 | $68,318.39 | $66,280.20 | $68,020.01 | 🟢 +1.52% | `35,351.87 BTC` |
| `2026-02-19` | $66,461.00 | $67,320.00 | $65,631.83 | $67,003.73 | 🟢 +0.82% | `14,542.27 BTC` |
| `2026-02-18` | $67,503.52 | $68,476.22 | $65,870.00 | $66,461.00 | 🔴 -1.54% | `15,492.44 BTC` |
| `2026-02-17` | $68,892.43 | $69,241.50 | $66,621.06 | $67,503.52 | 🔴 -2.02% | `16,489.07 BTC` |
| `2026-02-16` | $68,832.59 | $70,126.67 | $67,294.11 | $68,892.43 | 🟢 +0.09% | `15,515.77 BTC` |
| `2026-02-15` | $69,822.94 | $70,983.00 | $68,000.00 | $68,832.58 | 🔴 -1.42% | `22,290.05 BTC` |

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

*Last Telemetry Sync: `2026-02-21 12:21:56 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
