# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--11--25%2022:42%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$87,369.96** | 🔴 `-1.05%` | Real-time Aggregate Spot |
| **24h Price Range** | `$86,116.00 — $88,519.99` | `Spread: $2,403.99` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.71 B` | `19,567.04 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.73 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-11-24` | $88,300.01 | `-$930.05` | 🔴 -1.05% | Intraday Shift |
| **7 Days** | `2025-11-18` | $92,960.83 | `-$5,590.87` | 🔴 -6.01% | Weekly Momentum |
| **30 Days (1M)** | `2025-10-26` | $114,559.40 | `-$27,189.44` | 🔴 -23.73% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-08-27` | $111,262.01 | `-$23,892.05` | 🔴 -21.47% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-05-29` | $105,589.75 | `-$18,219.79` | 🔴 -17.26% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-11-25` | $93,010.01 | `-$5,640.05` | 🔴 -6.06% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$38,829.67` | 🔴 `-30.77%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-11-25` | $88,300.01 | $88,519.99 | $86,116.00 | $87,369.96 | 🔴 -1.05% | `19,567.04 BTC` |
| `2025-11-24` | $86,830.00 | $89,228.00 | $85,272.00 | $88,300.01 | 🟢 +1.69% | `24,663.13 BTC` |
| `2025-11-23` | $84,739.75 | $88,127.64 | $84,667.57 | $86,830.00 | 🟢 +2.47% | `19,734.46 BTC` |
| `2025-11-22` | $85,129.42 | $85,620.00 | $83,500.00 | $84,739.74 | 🔴 -0.46% | `14,193.93 BTC` |
| `2025-11-21` | $86,637.22 | $87,498.94 | $80,600.00 | $85,129.43 | 🔴 -1.74% | `72,256.13 BTC` |
| `2025-11-20` | $91,554.96 | $93,160.00 | $86,100.00 | $86,637.23 | 🔴 -5.37% | `39,733.19 BTC` |
| `2025-11-19` | $92,960.83 | $92,980.22 | $88,608.00 | $91,554.96 | 🔴 -1.51% | `32,286.64 BTC` |

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

*Last Telemetry Sync: `2025-11-25 22:42:18 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
