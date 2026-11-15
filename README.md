# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--15%2005:25%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$64,887.19** | 🟢 `+1.20%` | Real-time Aggregate Spot |
| **24h Price Range** | `$61,946.17 — $65,564.18` | `Spread: $3,618.01` | Intraday Volatility Band |
| **24h Trading Volume** | `$451.22 M` | `6,953.86 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.29 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-11-14` | $64,118.79 | `+$768.40` | 🟢 +1.20% | Intraday Shift |
| **7 Days** | `2026-11-08` | $74,754.08 | `-$9,866.89` | 🔴 -13.20% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-16` | $81,500.04 | `-$16,612.85` | 🔴 -20.38% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-17` | $64,484.18 | `+$403.01` | 🟢 +0.62% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-19` | $76,767.48 | `-$11,880.29` | 🔴 -15.48% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-01` | $86,282.36 | `-$21,395.17` | 🔴 -24.80% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$44,012.81` | 🔴 `-40.42%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15` | $64,118.86 | $65,564.18 | $61,946.17 | $64,887.19 | 🟢 +1.20% | `6,953.86 BTC` |
| `2026-11-14` | $68,236.54 | $68,380.00 | $63,270.00 | $64,118.79 | 🔴 -6.03% | `16,354.54 BTC` |
| `2026-11-13` | $71,369.90 | $71,429.46 | $67,555.00 | $68,236.54 | 🔴 -4.39% | `16,647.81 BTC` |
| `2026-11-12` | $73,927.63 | $74,123.71 | $71,008.00 | $71,369.90 | 🔴 -3.46% | `10,490.83 BTC` |
| `2026-11-11` | $73,697.88 | $74,737.15 | $73,110.00 | $73,927.63 | 🟢 +0.31% | `8,133.46 BTC` |
| `2026-11-10` | $75,257.77 | $75,340.23 | $72,643.48 | $73,697.87 | 🔴 -2.07% | `10,577.16 BTC` |
| `2026-11-09` | $74,756.52 | $75,500.00 | $73,636.00 | $75,259.28 | 🟢 +0.67% | `10,186.64 BTC` |

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

*Last Telemetry Sync: `2026-11-15 05:25:55 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
