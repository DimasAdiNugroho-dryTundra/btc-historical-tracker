# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--05--18%2022:19%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$77,001.87** | 🔴 `-0.59%` | Real-time Aggregate Spot |
| **24h Price Range** | `$76,051.00 — $77,800.00` | `Spread: $1,749.00` | Intraday Volatility Band |
| **24h Trading Volume** | `$1.44 B` | `18,745.52 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.53 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-05-17` | $77,457.67 | `-$455.80` | 🔴 -0.59% | Intraday Shift |
| **7 Days** | `2026-05-11` | $81,745.65 | `-$4,743.78` | 🔴 -5.80% | Weekly Momentum |
| **30 Days (1M)** | `2026-04-18` | $75,691.76 | `+$1,310.11` | 🟢 +1.73% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-02-17` | $67,503.52 | `+$9,498.35` | 🟢 +14.07% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-11-19` | $91,554.96 | `-$14,553.09` | 🔴 -15.90% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-05-18` | $106,454.26 | `-$29,452.39` | 🔴 -27.67% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$49,197.76` | 🔴 `-38.98%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-05-18` | $77,457.67 | $77,800.00 | $76,051.00 | $77,001.87 | 🔴 -0.59% | `18,745.52 BTC` |
| `2026-05-17` | $78,148.05 | $78,599.99 | $76,735.16 | $77,457.67 | 🔴 -0.88% | `8,442.70 BTC` |
| `2026-05-16` | $79,113.20 | $79,227.77 | $77,640.00 | $78,148.05 | 🔴 -1.22% | `12,132.86 BTC` |
| `2026-05-15` | $81,090.00 | $81,664.45 | $78,659.00 | $79,113.21 | 🔴 -2.44% | `17,351.27 BTC` |
| `2026-05-14` | $79,313.61 | $82,048.13 | $78,922.00 | $81,089.99 | 🟢 +2.24% | `19,727.87 BTC` |
| `2026-05-13` | $80,504.47 | $81,324.64 | $78,754.65 | $79,313.61 | 🔴 -1.48% | `14,810.06 BTC` |
| `2026-05-12` | $81,745.66 | $81,788.00 | $79,843.59 | $80,504.47 | 🔴 -1.52% | `12,386.26 BTC` |

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

*Last Telemetry Sync: `2026-05-18 22:19:08 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
