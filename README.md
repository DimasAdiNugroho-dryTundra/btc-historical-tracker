# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--07--13%2022:46%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$62,334.52** | 🔴 `-2.27%` | Real-time Aggregate Spot |
| **24h Price Range** | `$61,824.97 — $64,425.00` | `Spread: $2,600.03` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.36 B` | `21,682.50 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.24 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-07-12` | $63,780.00 | `-$1,445.48` | 🔴 -2.27% | Intraday Shift |
| **7 Days** | `2026-07-06` | $64,042.02 | `-$1,707.50` | 🔴 -2.67% | Weekly Momentum |
| **30 Days (1M)** | `2026-06-13` | $64,458.01 | `-$2,123.49` | 🔴 -3.29% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-04-14` | $74,131.55 | `-$11,797.03` | 🔴 -15.91% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-01-14` | $96,951.78 | `-$34,617.26` | 🔴 -35.71% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-07-13` | $119,086.64 | `-$56,752.12` | 🔴 -47.66% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$63,865.11` | 🔴 `-50.61%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-07-13` | $63,780.00 | $64,425.00 | $61,824.97 | $62,334.52 | 🔴 -2.27% | `21,682.50 BTC` |
| `2026-07-12` | $63,819.01 | $64,290.11 | $63,640.83 | $63,780.00 | 🔴 -0.06% | `13,914.84 BTC` |
| `2026-07-11` | $64,161.72 | $64,504.11 | $63,819.00 | $63,819.00 | 🔴 -0.53% | `9,151.97 BTC` |
| `2026-07-10` | $63,230.01 | $64,692.83 | $62,926.01 | $64,161.72 | 🟢 +1.47% | `17,589.00 BTC` |
| `2026-07-09` | $62,290.01 | $63,500.00 | $61,705.29 | $63,230.00 | 🟢 +1.51% | `16,742.81 BTC` |
| `2026-07-08` | $63,364.00 | $63,761.99 | $61,544.56 | $62,290.00 | 🔴 -1.69% | `18,620.10 BTC` |
| `2026-07-07` | $64,042.93 | $64,314.00 | $62,671.39 | $63,363.99 | 🔴 -1.06% | `16,834.21 BTC` |

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

*Last Telemetry Sync: `2026-07-13 22:46:46 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
