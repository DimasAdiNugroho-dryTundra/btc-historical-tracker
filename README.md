# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--05--29%2020:24%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$73,460.78** | 🔴 `-0.21%` | Real-time Aggregate Spot |
| **24h Price Range** | `$72,512.49 — $74,514.10` | `Spread: $2,001.61` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.38 B` | `18,686.74 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.46 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-05-28` | $73,617.51 | `-$156.73` | 🔴 -0.21% | Intraday Shift |
| **7 Days** | `2026-05-22` | $75,539.50 | `-$2,078.72` | 🔴 -2.75% | Weekly Momentum |
| **30 Days (1M)** | `2026-04-29` | $75,780.00 | `-$2,319.22` | 🔴 -3.06% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-02-28` | $66,973.26 | `+$6,487.52` | 🟢 +9.69% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-11-30` | $90,360.00 | `-$16,899.22` | 🔴 -18.70% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-05-29` | $105,589.75 | `-$32,128.97` | 🔴 -30.43% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$52,738.85` | 🔴 `-41.79%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-05-29` | $73,617.52 | $74,514.10 | $72,512.49 | $73,460.78 | 🔴 -0.21% | `18,686.74 BTC` |
| `2026-05-28` | $74,449.31 | $74,590.77 | $72,582.82 | $73,617.51 | 🔴 -1.12% | `21,274.02 BTC` |
| `2026-05-27` | $75,930.01 | $76,174.15 | $74,243.99 | $74,449.30 | 🔴 -1.95% | `16,877.77 BTC` |
| `2026-05-26` | $77,322.01 | $78,080.00 | $75,677.97 | $75,930.01 | 🔴 -1.80% | `16,953.48 BTC` |
| `2026-05-25` | $77,064.96 | $77,905.52 | $76,914.25 | $77,322.01 | 🟢 +0.33% | `7,672.32 BTC` |
| `2026-05-24` | $76,752.00 | $77,543.15 | $76,108.00 | $77,064.96 | 🟢 +0.41% | `8,398.00 BTC` |
| `2026-05-23` | $75,539.50 | $77,404.18 | $74,289.60 | $76,752.01 | 🟢 +1.61% | `15,086.89 BTC` |

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

*Last Telemetry Sync: `2026-05-29 20:24:51 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
