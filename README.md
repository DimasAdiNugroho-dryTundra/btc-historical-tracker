# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--10--22%2003:46%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$82,720.81** | 🔴 `-1.55%` | Real-time Aggregate Spot |
| **24h Price Range** | `$82,589.65 — $84,305.25` | `Spread: $1,715.60` | Intraday Volatility Band |
| **24h Trading Volume** | `$82.88 M` | `1,001.87 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.64 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-10-21` | $84,024.67 | `-$1,303.86` | 🔴 -1.55% | Intraday Shift |
| **7 Days** | `2026-10-15` | $82,131.46 | `+$589.35` | 🟢 +0.72% | Weekly Momentum |
| **30 Days (1M)** | `2026-09-22` | $86,198.05 | `-$3,477.24` | 🔴 -4.03% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-07-24` | $64,083.32 | `+$18,637.49` | 🟢 +29.08% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-04-25` | $77,650.72 | `+$5,070.09` | 🟢 +6.53% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-11-07` | $103,284.27 | `-$20,563.46` | 🔴 -19.91% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$26,179.19` | 🔴 `-24.04%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22` | $84,024.67 | $84,305.25 | $82,589.65 | $82,720.81 | 🔴 -1.55% | `1,001.87 BTC` |
| `2026-10-21` | $82,938.26 | $84,856.07 | $82,535.00 | $84,024.67 | 🟢 +1.31% | `7,643.92 BTC` |
| `2026-10-20` | $81,837.70 | $83,344.25 | $81,080.64 | $82,938.26 | 🟢 +1.34% | `5,237.79 BTC` |
| `2026-10-19` | $82,006.85 | $83,076.23 | $81,634.43 | $81,837.69 | 🔴 -0.21% | `4,758.02 BTC` |
| `2026-10-18` | $81,387.16 | $82,183.56 | $80,564.57 | $82,006.85 | 🟢 +0.76% | `2,937.80 BTC` |
| `2026-10-17` | $81,500.04 | $81,655.47 | $80,700.00 | $81,378.21 | 🔴 -0.15% | `1,890.36 BTC` |
| `2026-10-16` | $82,131.46 | $82,831.01 | $80,693.69 | $81,500.04 | 🔴 -0.77% | `5,082.37 BTC` |

---

### ⚙️ Automation & Pipeline Architecture

- **Automated Execution:** Synced daily at `00:00 UTC` via GitHub Actions (`.github/workflows/update.yml`).
- **Resilient Pipeline:** Cascading multi-exchange API architecture (Binance -> Coinbase -> Kraken -> CoinGecko).
- **Git-Native Telemetry:** Dynamic SVG vector graphics and Markdown dashboards saved directly into Git history.

```
[ GitHub Actions Cron: 00:00 UTC ]
               │
               ▼
   [ fetch_btc.py Executed ] ──► [ Query Multi-Exchange Feeds ]
               │
               ▼
   [ Generate assets/btc_trend.svg & README.md ]
               │
               ▼
   [ Auto Git Commit & Push (main) ]
```

---

<div align="center">

*Last Telemetry Sync: `2026-10-22 03:46:25 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
