# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--11--13%2022:21%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$99,692.02** | 🔴 `-1.93%` | Real-time Aggregate Spot |
| **24h Price Range** | `$98,000.40 — $104,085.01` | `Spread: $6,084.61` | Intraday Volatility Band |
| **24h Trading Volume** | `$3.65 B` | `36,198.51 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.98 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-11-12` | $101,654.37 | `-$1,962.35` | 🔴 -1.93% | Intraday Shift |
| **7 Days** | `2025-11-06` | $101,346.04 | `-$1,654.02` | 🔴 -1.63% | Weekly Momentum |
| **30 Days (1M)** | `2025-10-14` | $113,028.14 | `-$13,336.12` | 🔴 -11.80% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-08-15` | $117,342.05 | `-$17,650.03` | 🔴 -15.04% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-05-17` | $103,126.65 | `-$3,434.63` | 🔴 -3.33% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-11-13` | $90,375.20 | `+$9,316.82` | 🟢 +10.31% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$26,507.61` | 🔴 `-21.00%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-11-13` | $101,654.37 | $104,085.01 | $98,000.40 | $99,692.02 | 🔴 -1.93% | `36,198.51 BTC` |
| `2025-11-12` | $103,059.00 | $105,333.33 | $100,813.59 | $101,654.37 | 🔴 -1.36% | `20,457.64 BTC` |
| `2025-11-11` | $106,011.13 | $107,500.00 | $102,476.09 | $103,058.99 | 🔴 -2.78% | `24,196.51 BTC` |
| `2025-11-10` | $104,722.95 | $106,670.11 | $104,265.02 | $106,011.13 | 🟢 +1.23% | `22,682.26 BTC` |
| `2025-11-09` | $102,312.95 | $105,495.62 | $101,400.00 | $104,722.96 | 🟢 +2.36% | `16,338.97 BTC` |
| `2025-11-08` | $103,339.09 | $103,406.22 | $101,454.00 | $102,312.94 | 🔴 -0.99% | `12,390.78 BTC` |
| `2025-11-07` | $101,346.04 | $104,096.36 | $99,260.86 | $103,339.08 | 🟢 +1.97% | `32,059.51 BTC` |

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

*Last Telemetry Sync: `2025-11-13 22:21:29 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
