# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--17%2007:01%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$64,493.88** | 🔴 `-0.50%` | Real-time Aggregate Spot |
| **24h Price Range** | `$64,228.41 — $65,150.00` | `Spread: $921.59` | Intraday Volatility Band |
| **24h Trading Volume** | `$152.87 M` | `2,370.37 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.28 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-11-16` | $64,816.79 | `-$322.91` | 🔴 -0.50% | Intraday Shift |
| **7 Days** | `2026-11-10` | $73,697.87 | `-$9,203.99` | 🔴 -12.49% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-18` | $82,006.85 | `-$17,512.97` | 🔴 -21.36% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-19` | $69,300.01 | `-$4,806.13` | 🔴 -6.94% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-21` | $77,547.62 | `-$13,053.74` | 🔴 -16.83% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-03` | $93,453.84 | `-$28,959.96` | 🔴 -30.99% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$44,406.12` | 🔴 `-40.78%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17` | $64,816.79 | $65,150.00 | $64,228.41 | $64,493.88 | 🔴 -0.50% | `2,370.37 BTC` |
| `2026-11-16` | $65,315.35 | $65,626.98 | $63,833.47 | $64,816.79 | 🔴 -0.76% | `13,678.70 BTC` |
| `2026-11-15` | $64,118.86 | $66,100.00 | $61,946.17 | $65,315.35 | 🟢 +1.87% | `15,513.94 BTC` |
| `2026-11-14` | $68,236.54 | $68,380.00 | $63,270.00 | $64,118.79 | 🔴 -6.03% | `16,354.54 BTC` |
| `2026-11-13` | $71,369.90 | $71,429.46 | $67,555.00 | $68,236.54 | 🔴 -4.39% | `16,647.81 BTC` |
| `2026-11-12` | $73,927.63 | $74,123.71 | $71,008.00 | $71,369.90 | 🔴 -3.46% | `10,490.83 BTC` |
| `2026-11-11` | $73,697.88 | $74,737.15 | $73,110.00 | $73,927.63 | 🟢 +0.31% | `8,133.46 BTC` |

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

*Last Telemetry Sync: `2026-11-17 07:01:58 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
