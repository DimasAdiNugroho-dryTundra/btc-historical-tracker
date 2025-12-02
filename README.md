# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-Binance_Spot_API-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-2025--12--02%2014:03%20UTC-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **$91,277.88** | 🟢 `+5.79%` | Real-time Aggregate Spot |
| **24h Price Range** | `$86,184.39 — $92,307.65` | `Spread: $6,123.26` | Intraday Volatility Band |
| **24h Trading Volume** | `$2.52 B` | `28,210.23 BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `$1.81 T` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
| **24 Hours** | `2025-12-01` | $86,286.01 | `+$4,991.87` | 🟢 +5.79% | Intraday Shift |
| **7 Days** | `2025-11-25` | $87,369.96 | `+$3,907.92` | 🟢 +4.47% | Weekly Momentum |
| **30 Days (1M)** | `2025-11-02` | $110,540.68 | `-$19,262.80` | 🔴 -17.43% | Monthly Trajectory |
| **90 Days (Quarterly)** | `2025-09-03` | $111,705.71 | `-$20,427.83` | 🔴 -18.29% | Quarterly Baseline |
| **180 Days (Half-Year)** | `2025-06-05` | $101,508.68 | `-$10,230.80` | 🔴 -10.08% | Semi-Annual Cycle |
| **365 Days (1 Year)** | `2024-12-02` | $95,840.62 | `-$4,562.74` | 🔴 -4.76% | Macro Annual Delta |
| **All-Time High (ATH)** | `2025-10-06` | $126,199.63 | `-$34,921.75` | 🔴 `-27.67%` | Peak Drawdown |

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `2025-12-02` | $86,286.01 | $92,307.65 | $86,184.39 | $91,277.88 | 🟢 +5.79% | `28,210.23 BTC` |
| `2025-12-01` | $90,360.01 | $90,417.00 | $83,822.76 | $86,286.01 | 🔴 -4.51% | `34,509.01 BTC` |
| `2025-11-30` | $90,802.44 | $92,000.01 | $90,336.90 | $90,360.00 | 🔴 -0.49% | `9,687.74 BTC` |
| `2025-11-29` | $90,890.71 | $91,165.65 | $90,155.47 | $90,802.44 | 🔴 -0.10% | `7,429.88 BTC` |
| `2025-11-28` | $91,333.94 | $93,092.00 | $90,180.63 | $90,890.70 | 🔴 -0.49% | `18,830.86 BTC` |
| `2025-11-27` | $90,484.01 | $91,950.00 | $90,089.91 | $91,333.95 | 🟢 +0.94% | `16,833.51 BTC` |
| `2025-11-26` | $87,369.97 | $90,656.08 | $86,306.77 | $90,484.02 | 🟢 +3.56% | `21,675.82 BTC` |

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

*Last Telemetry Sync: `2025-12-02 14:03:44 UTC` • Data Feed: `Binance Spot (BTC/USDT)` • Status: `Operational (HTTP 200 OK)`*

</div>
