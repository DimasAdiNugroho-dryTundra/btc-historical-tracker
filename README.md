# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--09--15%2003:55%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$77,712.66** | 🔴 `-0.59%` | Real-time Aggregate Spot |
| **24h Price Range** | `$77,680.00 — $78,242.76` | `Spread: $562.76` | Intraday Volatility Band |
| **24h Trading Volume** | `$59.43 M` | `764.72 BTC` | 24h Spot Pair Turnover |
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
| **24 Hours** | `2026-09-14` | $78,175.01 | `-$462.35` | 🔴 -0.59% | Intraday Shift |
| **7 Days** | `2026-09-08` | $78,447.11 | `-$734.45` | 🔴 -0.94% | Weekly Momentum |
| **30 Days (1M)** | `2026-08-16` | $62,836.66 | `+$14,876.00` | 🟢 +23.67% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-06-17` | $64,446.04 | `+$13,266.62` | 🟢 +20.59% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-03-19` | $69,918.30 | `+$7,794.36` | 🟢 +11.15% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-10-01` | $118,659.97 | `-$40,947.31` | 🔴 -34.51% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,296.00 | `-$48,583.34` | 🔴 `-38.47%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-09-15` | $78,175.00 | $78,242.76 | $77,680.00 | $77,712.66 | 🔴 -0.59% | `764.72 BTC` |
| `2026-09-14` | $76,799.85 | $79,591.17 | $76,347.27 | $78,175.01 | 🟢 +1.79% | `6,547.43 BTC` |
| `2026-09-13` | $77,262.85 | $77,425.43 | $76,457.09 | $76,799.85 | 🔴 -0.60% | `2,218.40 BTC` |
| `2026-09-12` | $77,208.55 | $77,495.00 | $77,049.56 | $77,262.85 | 🟢 +0.07% | `1,669.18 BTC` |
| `2026-09-11` | $76,536.55 | $79,852.22 | $76,030.00 | $77,208.55 | 🟢 +0.88% | `7,311.00 BTC` |
| `2026-09-10` | $78,283.98 | $78,554.18 | $76,440.00 | $76,536.55 | 🔴 -2.23% | `6,390.76 BTC` |
| `2026-09-09` | $78,449.28 | $79,752.73 | $77,727.00 | $78,283.98 | 🔴 -0.21% | `5,255.84 BTC` |

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

*Last Telemetry Sync: `2026-09-15 03:55:54 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
