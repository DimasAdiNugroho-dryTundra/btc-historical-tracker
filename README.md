# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--16%2005:23%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$64,760.44** | 🔴 `-0.85%` | Real-time Aggregate Spot |
| **24h Price Range** | `$64,488.02 — $65,366.39` | `Spread: $878.37` | Intraday Volatility Band |
| **24h Trading Volume** | `$123.11 M` | `1,901.07 BTC` | 24h Spot Pair Turnover |
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
| **24 Hours** | `2026-11-15` | $65,315.35 | `-$554.91` | 🔴 -0.85% | Intraday Shift |
| **7 Days** | `2026-11-09` | $75,259.28 | `-$10,498.84` | 🔴 -13.95% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-17` | $81,378.21 | `-$16,617.77` | 🔴 -20.42% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-18` | $64,681.33 | `+$79.11` | 🟢 +0.12% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-20` | $77,475.99 | `-$12,715.55` | 🔴 -16.41% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-02` | $91,308.05 | `-$26,547.61` | 🔴 -29.07% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$44,139.56` | 🔴 `-40.53%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16` | $65,315.35 | $65,366.39 | $64,488.02 | $64,760.44 | 🔴 -0.85% | `1,901.07 BTC` |
| `2026-11-15` | $64,118.86 | $66,100.00 | $61,946.17 | $65,315.35 | 🟢 +1.87% | `15,513.94 BTC` |
| `2026-11-14` | $68,236.54 | $68,380.00 | $63,270.00 | $64,118.79 | 🔴 -6.03% | `16,354.54 BTC` |
| `2026-11-13` | $71,369.90 | $71,429.46 | $67,555.00 | $68,236.54 | 🔴 -4.39% | `16,647.81 BTC` |
| `2026-11-12` | $73,927.63 | $74,123.71 | $71,008.00 | $71,369.90 | 🔴 -3.46% | `10,490.83 BTC` |
| `2026-11-11` | $73,697.88 | $74,737.15 | $73,110.00 | $73,927.63 | 🟢 +0.31% | `8,133.46 BTC` |
| `2026-11-10` | $75,257.77 | $75,340.23 | $72,643.48 | $73,697.87 | 🔴 -2.07% | `10,577.16 BTC` |

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

*Last Telemetry Sync: `2026-11-16 05:23:57 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
