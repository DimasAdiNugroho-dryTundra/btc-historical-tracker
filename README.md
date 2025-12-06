# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--06%2008:11%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$89,236.79** | 🔴 `-0.10%` | Real-time Aggregate Spot |
| **24h Price Range** | `$88,908.01 — $90,289.97` | `Spread: $1,381.96` | Intraday Volatility Band |
| **24h Trading Volume** | `$753.42 M` | `8,409.50 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.77 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-05` | $89,330.04 | `-$93.25` | 🔴 -0.10% | Intraday Shift |
| **7 Days** | `2025-11-29` | $90,802.44 | `-$1,565.65` | 🔴 -1.72% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-06` | $101,346.04 | `-$12,109.25` | 🔴 -11.95% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-07` | $111,137.34 | `-$21,900.55` | 🔴 -19.71% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-06-09` | $110,263.02 | `-$21,026.23` | 🔴 -19.07% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-06` | $99,740.84 | `-$10,504.05` | 🔴 -10.53% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$36,962.84` | 🔴 `-29.29%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-06` | $89,330.04 | $90,289.97 | $88,908.01 | $89,236.79 | 🔴 -0.10% | `8,409.50 BTC` |
| `2025-12-05` | $92,078.06 | $92,692.36 | $88,056.00 | $89,330.04 | 🔴 -2.98% | `19,792.97 BTC` |
| `2025-12-04` | $93,429.95 | $94,080.00 | $90,889.00 | $92,078.06 | 🔴 -1.45% | `19,803.94 BTC` |
| `2025-12-03` | $91,277.88 | $94,150.00 | $90,990.23 | $93,429.95 | 🟢 +2.36% | `25,712.53 BTC` |
| `2025-12-02` | $86,286.01 | $92,307.65 | $86,184.39 | $91,277.88 | 🟢 +5.79% | `28,210.23 BTC` |
| `2025-12-01` | $90,360.01 | $90,417.00 | $83,822.76 | $86,286.01 | 🔴 -4.51% | `34,509.01 BTC` |
| `2025-11-30` | $90,802.44 | $92,000.01 | $90,336.90 | $90,360.00 | 🔴 -0.49% | `9,687.74 BTC` |

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

*Last Telemetry Sync: `2025-12-06 08:11:14 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
