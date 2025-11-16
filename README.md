# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--11--16%2015:30%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$94,261.44** | 🔴 `-1.40%` | Real-time Aggregate Spot |
| **24h Price Range** | `$93,005.55 — $96,635.11` | `Spread: $3,629.56` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.26 B` | `23,889.41 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.87 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-11-15` | $95,596.24 | `-$1,334.80` | 🔴 -1.40% | Intraday Shift |
| **7 Days** | `2025-11-09` | $104,722.96 | `-$10,461.52` | 🔴 -9.99% | Weekly Momentum |
| **30 Days (1M)** | `2025-10-17` | $106,431.68 | `-$12,170.24` | 🔴 -11.43% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-08-18` | $116,227.05 | `-$21,965.61` | 🔴 -18.90% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-05-20` | $106,849.99 | `-$12,588.55` | 🔴 -11.78% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-11-16` | $90,586.92 | `+$3,674.52` | 🟢 +4.06% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$31,938.19` | 🔴 `-25.31%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-11-16` | $95,596.23 | $96,635.11 | $93,005.55 | $94,261.44 | 🔴 -1.40% | `23,889.41 BTC` |
| `2025-11-15` | $94,594.00 | $96,846.68 | $94,558.49 | $95,596.24 | 🟢 +1.06% | `15,110.89 BTC` |
| `2025-11-14` | $99,692.03 | $99,866.02 | $94,012.45 | $94,594.00 | 🔴 -5.11% | `47,288.14 BTC` |
| `2025-11-13` | $101,654.37 | $104,085.01 | $98,000.40 | $99,692.02 | 🔴 -1.93% | `36,198.51 BTC` |
| `2025-11-12` | $103,059.00 | $105,333.33 | $100,813.59 | $101,654.37 | 🔴 -1.36% | `20,457.64 BTC` |
| `2025-11-11` | $106,011.13 | $107,500.00 | $102,476.09 | $103,058.99 | 🔴 -2.78% | `24,196.51 BTC` |
| `2025-11-10` | $104,722.95 | $106,670.11 | $104,265.02 | $106,011.13 | 🟢 +1.23% | `22,682.26 BTC` |

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

*Last Telemetry Sync: `2025-11-16 15:30:34 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
