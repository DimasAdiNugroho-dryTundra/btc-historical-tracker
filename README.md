# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Coinbase_Exchange_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2026--11--19%2006:28%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$63,466.45** | 🟢 `+0.77%` | Real-time Aggregate Spot |
| **24h Price Range** | `$62,322.12 — $63,683.25` | `Spread: $1,361.13` | Intraday Volatility Band |
| **24h Trading Volume** | `$154.22 M` | `2,429.96 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.26 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2026-11-18` | $62,981.71 | `+$484.74` | 🟢 +0.77% | Intraday Shift |
| **7 Days** | `2026-11-12` | $71,369.90 | `-$7,903.45` | 🔴 -11.07% | Weekly Momentum |
| **30 Days (1M)** | `2026-10-20` | $82,938.26 | `-$19,471.81` | 🔴 -23.48% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2026-08-21` | $78,325.54 | `-$14,859.09` | 🔴 -18.97% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2026-05-23` | $76,650.00 | `-$13,183.55` | 🔴 -17.20% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2025-12-05` | $89,345.29 | `-$25,878.84` | 🔴 -28.96% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-01-20` | $108,900.00 | `-$45,433.55` | 🔴 `-41.72%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19` | $62,981.71 | $63,683.25 | $62,322.12 | $63,466.45 | 🟢 +0.77% | `2,429.96 BTC` |
| `2026-11-18` | $64,873.18 | $64,933.39 | $62,000.00 | $62,981.71 | 🔴 -2.92% | `12,482.68 BTC` |
| `2026-11-17` | $64,816.79 | $65,383.29 | $63,256.75 | $64,873.18 | 🟢 +0.09% | `11,768.55 BTC` |
| `2026-11-16` | $65,315.35 | $65,626.98 | $63,833.47 | $64,816.79 | 🔴 -0.76% | `13,678.70 BTC` |
| `2026-11-15` | $64,118.86 | $66,100.00 | $61,946.17 | $65,315.35 | 🟢 +1.87% | `15,513.94 BTC` |
| `2026-11-14` | $68,236.54 | $68,380.00 | $63,270.00 | $64,118.79 | 🔴 -6.03% | `16,354.54 BTC` |
| `2026-11-13` | $71,369.90 | $71,429.46 | $67,555.00 | $68,236.54 | 🔴 -4.39% | `16,647.81 BTC` |

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

*Last Telemetry Sync: `2026-11-19 06:28:27 UTC` • Data Feed: `Coinbase Exchange API (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
