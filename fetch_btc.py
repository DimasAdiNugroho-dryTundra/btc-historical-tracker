#!/usr/bin/env python3
"""
Bitcoin & Crypto Historical Tracker
Standalone Daily Telemetry & Dashboard Generator
Resilient 4-Tier Multi-Exchange Fallback (Binance -> Coinbase -> Kraken -> CoinGecko)
"""

import os
import sys
import json
import datetime
import urllib.request
import urllib.error

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
CIRCULATING_SUPPLY = 19_850_000.0


def fetch_json(url: str, timeout: int = 15) -> dict | list:
    """Fetch JSON from remote endpoint with proper User-Agent."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def format_usd(val: float) -> str:
    return f"${val:,.2f}"


def format_compact_usd(val: float) -> str:
    if val >= 1_000_000_000_000:
        return f"${val / 1_000_000_000_000:.2f} T"
    elif val >= 1_000_000_000:
        return f"${val / 1_000_000_000:.2f} B"
    elif val >= 1_000_000:
        return f"${val / 1_000_000:.2f} M"
    return f"${val:,.2f}"


def format_change(pct: float) -> str:
    if pct > 0.001:
        return f"🟢 +{pct:.2f}%"
    elif pct < -0.001:
        return f"🔴 {pct:.2f}%"
    return "🟡 0.00%"


def get_trend_icon(pct: float) -> str:
    if pct > 0.001:
        return "🟢"
    elif pct < -0.001:
        return "🔴"
    return "🟡"


# ==========================================
# Multi-Exchange Data Ingestion (4 Tiers)
# ==========================================

def fetch_binance_data() -> dict:
    """Tier 1: Binance Spot REST API."""
    klines_url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=450"
    ticker_url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"

    klines_raw = fetch_json(klines_url)
    ticker_raw = fetch_json(ticker_url)

    candles = []
    for k in klines_raw:
        candles.append({
            "timestamp": int(k[0]),
            "date": datetime.datetime.fromtimestamp(k[0] / 1000, tz=datetime.timezone.utc).strftime("%Y-%m-%d"),
            "open": float(k[1]),
            "high": float(k[2]),
            "low": float(k[3]),
            "close": float(k[4]),
            "vol_btc": float(k[5]),
            "vol_usd": float(k[7]),
        })

    current_price = float(ticker_raw.get("lastPrice", candles[-1]["close"]))
    high_24h = float(ticker_raw.get("highPrice", candles[-1]["high"]))
    low_24h = float(ticker_raw.get("lowPrice", candles[-1]["low"]))
    chg_24h = float(ticker_raw.get("priceChangePercent", 0.0))
    vol_btc_24h = float(ticker_raw.get("volume", candles[-1]["vol_btc"]))
    vol_usd_24h = float(ticker_raw.get("quoteVolume", candles[-1]["vol_usd"]))

    return {
        "source": "Binance Spot API",
        "current_price": current_price,
        "high_24h": high_24h,
        "low_24h": low_24h,
        "chg_24h": chg_24h,
        "vol_btc_24h": vol_btc_24h,
        "vol_usd_24h": vol_usd_24h,
        "candles": candles,
    }


def fetch_coinbase_data() -> dict:
    """Tier 2: Coinbase Exchange REST API (US Datacenter Native)."""
    candles_url = "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=86400"
    raw = fetch_json(candles_url)
    # Format: [time, low, high, open, close, volume]
    candles = []
    for k in reversed(raw):
        candles.append({
            "timestamp": int(k[0]) * 1000,
            "date": datetime.datetime.fromtimestamp(k[0], tz=datetime.timezone.utc).strftime("%Y-%m-%d"),
            "low": float(k[1]),
            "high": float(k[2]),
            "open": float(k[3]),
            "close": float(k[4]),
            "vol_btc": float(k[5]),
            "vol_usd": float(k[5]) * float(k[4]),
        })

    latest = candles[-1]
    curr_price = latest["close"]
    chg_24h = ((curr_price - latest["open"]) / latest["open"]) * 100 if latest["open"] > 0 else 0.0

    return {
        "source": "Coinbase Exchange API",
        "current_price": curr_price,
        "high_24h": latest["high"],
        "low_24h": latest["low"],
        "chg_24h": chg_24h,
        "vol_btc_24h": latest["vol_btc"],
        "vol_usd_24h": latest["vol_usd"],
        "candles": candles,
    }


def fetch_kraken_data() -> dict:
    """Tier 3: Kraken Public REST API."""
    ohlc_url = "https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440"
    ticker_url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"

    ohlc_raw = fetch_json(ohlc_url)
    ticker_raw = fetch_json(ticker_url)

    candles_list = ohlc_raw.get("result", {}).get("XXBTZUSD", [])
    candles = []
    for k in candles_list:
        candles.append({
            "timestamp": int(k[0]) * 1000,
            "date": datetime.datetime.fromtimestamp(k[0], tz=datetime.timezone.utc).strftime("%Y-%m-%d"),
            "open": float(k[1]),
            "high": float(k[2]),
            "low": float(k[3]),
            "close": float(k[4]),
            "vol_btc": float(k[6]),
            "vol_usd": float(k[6]) * float(k[4]),
        })

    t_data = ticker_raw.get("result", {}).get("XXBTZUSD", {})
    curr = float(t_data["c"][0]) if "c" in t_data else candles[-1]["close"]
    high = float(t_data["h"][1]) if "h" in t_data else candles[-1]["high"]
    low = float(t_data["l"][1]) if "l" in t_data else candles[-1]["low"]
    open_p = float(t_data["o"]) if "o" in t_data else candles[-1]["open"]
    chg = ((curr - open_p) / open_p) * 100 if open_p > 0 else 0.0
    vol_btc = float(t_data["v"][1]) if "v" in t_data else candles[-1]["vol_btc"]

    return {
        "source": "Kraken Public API",
        "current_price": curr,
        "high_24h": high,
        "low_24h": low,
        "chg_24h": chg,
        "vol_btc_24h": vol_btc,
        "vol_usd_24h": vol_btc * curr,
        "candles": candles,
    }


def fetch_coingecko_data() -> dict:
    """Tier 4: CoinGecko Public REST API."""
    chart_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=450&interval=daily"
    price_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_vol=true&include_24hr_change=true&include_market_cap=true"

    chart_raw = fetch_json(chart_url)
    price_raw = fetch_json(price_url)

    btc_info = price_raw.get("bitcoin", {})
    current_price = float(btc_info.get("usd", 0.0))
    chg_24h = float(btc_info.get("usd_24h_change", 0.0))
    vol_usd_24h = float(btc_info.get("usd_24h_vol", 0.0))
    vol_btc_24h = vol_usd_24h / current_price if current_price > 0 else 0.0

    prices_list = chart_raw.get("prices", [])
    vols_list = chart_raw.get("total_volumes", [])

    candles = []
    for i, p_item in enumerate(prices_list):
        ts = int(p_item[0])
        p_val = float(p_item[1])
        v_val = float(vols_list[i][1]) if i < len(vols_list) else 0.0
        dt_str = datetime.datetime.fromtimestamp(ts / 1000, tz=datetime.timezone.utc).strftime("%Y-%m-%d")
        candles.append({
            "timestamp": ts,
            "date": dt_str,
            "open": p_val,
            "high": p_val * 1.015,
            "low": p_val * 0.985,
            "close": p_val,
            "vol_btc": v_val / p_val if p_val > 0 else 0.0,
            "vol_usd": v_val,
        })

    return {
        "source": "CoinGecko API",
        "current_price": current_price,
        "high_24h": current_price * 1.015,
        "low_24h": current_price * 0.985,
        "chg_24h": chg_24h,
        "vol_btc_24h": vol_btc_24h,
        "vol_usd_24h": vol_usd_24h,
        "candles": candles,
    }


def get_market_data() -> dict:
    """Cascading fallback across 4 exchange providers."""
    providers = [
        ("Binance Spot API", fetch_binance_data),
        ("Coinbase Exchange API", fetch_coinbase_data),
        ("Kraken Public API", fetch_kraken_data),
        ("CoinGecko API", fetch_coingecko_data),
    ]

    for name, fetcher in providers:
        try:
            print(f"[+] Querying {name}...")
            data = fetcher()
            if data and data.get("candles"):
                print(f"[✓] {name} online: Current BTC at {format_usd(data['current_price'])}")
                return data
        except Exception as e:
            print(f"[!] {name} failed: {e}. Trying next provider...")

    raise RuntimeError("All market data providers exhausted.")


# ==========================================
# Rendering Engines (SVG & Markdown)
# ==========================================

def generate_svg_chart(candles_30d: list[dict], width: int = 800, height: int = 320) -> str:
    """Generate high-resolution dark-mode SVG area trend chart."""
    prices = [c["close"] for c in candles_30d]
    if not prices:
        return ""

    min_p = min(prices)
    max_p = max(prices)
    spread = max_p - min_p if max_p != min_p else 1.0

    padding_left = 75
    padding_right = 35
    padding_top = 45
    padding_bottom = 45

    chart_w = width - padding_left - padding_right
    chart_h = height - padding_top - padding_bottom

    points = []
    n = len(prices)
    for i, p in enumerate(prices):
        x = padding_left + (i / (n - 1)) * chart_w if n > 1 else padding_left
        y = padding_top + (1.0 - (p - min_p) / spread) * chart_h
        points.append((x, y))

    path_d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    area_d = f"{path_d} L {points[-1][0]:.1f},{height - padding_bottom:.1f} L {points[0][0]:.1f},{height - padding_bottom:.1f} Z"

    is_positive = prices[-1] >= prices[0]
    stroke_color = "#00E676" if is_positive else "#FF5252"
    grad_stop_top = "rgba(0, 230, 118, 0.35)" if is_positive else "rgba(255, 82, 82, 0.35)"
    grad_stop_bot = "rgba(0, 230, 118, 0.0)" if is_positive else "rgba(255, 82, 82, 0.0)"

    pct_chg = ((prices[-1] - prices[0]) / prices[0]) * 100 if prices[0] > 0 else 0.0
    sign = "+" if pct_chg >= 0 else ""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#0d1117;border-radius:12px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;">
  <defs>
    <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{grad_stop_top}"/>
      <stop offset="100%" stop-color="{grad_stop_bot}"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Card Border -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="11" fill="none" stroke="#30363d" stroke-width="1.5"/>

  <!-- Title & Current Price Badge -->
  <text x="{padding_left}" y="28" fill="#8b949e" font-size="12" font-weight="600" letter-spacing="0.8">BITCOIN 30-DAY ROLLING SPOT TREND (USD)</text>
  <text x="{width - padding_right}" y="28" text-anchor="end" fill="{stroke_color}" font-size="14" font-weight="700">${prices[-1]:,.2f} ({sign}{pct_chg:.2f}%)</text>

  <!-- Horizontal Gridlines & Price Labels -->
  <line x1="{padding_left}" y1="{padding_top}" x2="{width - padding_right}" y2="{padding_top}" stroke="#21262d" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="{padding_left - 10}" y="{padding_top + 4}" text-anchor="end" fill="#8b949e" font-size="11">${max_p:,.0f}</text>

  <line x1="{padding_left}" y1="{padding_top + chart_h / 2:.1f}" x2="{width - padding_right}" y2="{padding_top + chart_h / 2:.1f}" stroke="#21262d" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="{padding_left - 10}" y="{padding_top + chart_h / 2 + 4:.1f}" text-anchor="end" fill="#8b949e" font-size="11">${(min_p + spread / 2):,.0f}</text>

  <line x1="{padding_left}" y1="{height - padding_bottom}" x2="{width - padding_right}" y2="{height - padding_bottom}" stroke="#21262d" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="{padding_left - 10}" y="{height - padding_bottom + 4}" text-anchor="end" fill="#8b949e" font-size="11">${min_p:,.0f}</text>

  <!-- Area Fill & Trend Curve -->
  <path d="{area_d}" fill="url(#areaGrad)" />
  <path d="{path_d}" fill="none" stroke="{stroke_color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)"/>

  <!-- Last Point Indicator -->
  <circle cx="{points[-1][0]:.1f}" cy="{points[-1][1]:.1f}" r="4.5" fill="#ffffff" stroke="{stroke_color}" stroke-width="2.5"/>

  <!-- Date Axis Labels -->
  <text x="{points[0][0]:.1f}" y="{height - 15}" fill="#8b949e" font-size="11" text-anchor="start">{candles_30d[0]['date']}</text>
  <text x="{points[len(points) // 2][0]:.1f}" y="{height - 15}" fill="#8b949e" font-size="11" text-anchor="middle">{candles_30d[len(candles_30d) // 2]['date']}</text>
  <text x="{points[-1][0]:.1f}" y="{height - 15}" fill="#8b949e" font-size="11" text-anchor="end">{candles_30d[-1]['date']}</text>
</svg>"""
    return svg


def get_benchmark_candle(candles: list[dict], days_ago: int) -> dict:
    latest_dt = datetime.datetime.strptime(candles[-1]["date"], "%Y-%m-%d").date()
    target_dt = latest_dt - datetime.timedelta(days=days_ago)
    target_str = target_dt.strftime("%Y-%m-%d")
    matched = [c for c in candles if c["date"] <= target_str]
    return matched[-1] if matched else candles[0]


def generate_readme_content(data: dict, timestamp: datetime.datetime = None) -> str:
    if timestamp is None:
        timestamp = datetime.datetime.now(datetime.timezone.utc)

    curr_price = data["current_price"]
    chg_24h = data["chg_24h"]
    high_24h = data["high_24h"]
    low_24h = data["low_24h"]
    spread = high_24h - low_24h
    vol_usd = data["vol_usd_24h"]
    vol_btc = data["vol_btc_24h"]
    mcap = curr_price * CIRCULATING_SUPPLY
    candles = data["candles"]

    horizons = [
        ("24 Hours", 1, "Intraday Shift"),
        ("7 Days", 7, "Weekly Momentum"),
        ("30 Days (1M)", 30, "Monthly Trajectory"),
        ("90 Days (Quarterly)", 90, "Quarterly Baseline"),
        ("180 Days (Half-Year)", 180, "Semi-Annual Cycle"),
        ("365 Days (1 Year)", 365, "Macro Annual Delta"),
    ]

    roi_rows = []
    for label, days_back, note in horizons:
        b = get_benchmark_candle(candles, days_back)
        b_price = b["close"]
        delta = curr_price - b_price
        roi = (delta / b_price) * 100 if b_price > 0 else 0.0
        delta_sign = "+" if delta >= 0 else "-"
        row = (
            f"| **{label}** | `{b['date']}` | {format_usd(b_price)} | "
            f"`{delta_sign}{format_usd(abs(delta))}` | {format_change(roi)} | {note} |"
        )
        roi_rows.append(row)

    ath_candle = max(candles, key=lambda c: c["high"]) if candles else None
    peak_high = ath_candle["high"] if ath_candle else 108900.0
    ath_price = max(peak_high, 108900.0)
    ath_date = ath_candle["date"] if ath_candle and peak_high >= 108900.0 else "2025-01-20"
    delta_ath = curr_price - ath_price
    drawdown_ath = (delta_ath / ath_price) * 100
    delta_ath_sign = "+" if delta_ath >= 0 else "-"
    ath_row = (
        f"| **All-Time High (ATH)** | `{ath_date}` | {format_usd(ath_price)} | "
        f"`{delta_ath_sign}{format_usd(abs(delta_ath))}` | {get_trend_icon(drawdown_ath)} `{drawdown_ath:+.2f}%` | Peak Drawdown |"
    )
    roi_rows.append(ath_row)
    performance_matrix_content = "\n".join(roi_rows)

    recent_7 = candles[-7:] if len(candles) >= 7 else candles
    seven_day_rows = []
    for c in reversed(recent_7):
        day_chg = ((c["close"] - c["open"]) / c["open"]) * 100 if c["open"] > 0 else 0.0
        row = (
            f"| `{c['date']}` | {format_usd(c['open'])} | {format_usd(c['high'])} | "
            f"{format_usd(c['low'])} | {format_usd(c['close'])} | {format_change(day_chg)} | "
            f"`{c['vol_btc']:,.2f} BTC` |"
        )
        seven_day_rows.append(row)
    seven_day_table_content = "\n".join(seven_day_rows)

    time_str = timestamp.strftime("%H:%M")
    badge_date_encoded = f"{timestamp.year}--{timestamp.month:02d}--{timestamp.day:02d}%20{time_str}%20UTC"
    full_timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    markdown_template = f"""# 🪙 Bitcoin & Crypto Historical Tracker

<div align="center">

[![Tracker Status](https://img.shields.io/badge/Tracker_Status-Live_Feed-00C853?style=for-the-badge&logo=rss&logoColor=white)](https://github.com)
[![Network](https://img.shields.io/badge/Network-Bitcoin_Mainnet-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://github.com)
[![Automation](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Data Feed](https://img.shields.io/badge/Data_Feed-{data['source'].replace(' ', '_')}-F0B90B?style=for-the-badge&logo=binance&logoColor=black)](https://api.binance.com)
[![Last Updated](https://img.shields.io/badge/Last_Updated-{badge_date_encoded}-212121?style=for-the-badge&logo=clock&logoColor=white)](https://github.com)

</div>

---

### 📊 Executive Market Telemetry

Real-time Bitcoin ($BTC) market tracking telemetry, algorithmic historical benchmarks, and rolling price-action matrix. Fully automated and synced via GitHub Actions CI/CD pipeline with zero external database dependencies.

| Telemetry Metric | Spot Value (USD) | 24h Trend / Spread | Reference Context |
| :--- | :--- | :--- | :--- |
| **Current BTC Price** | **{format_usd(curr_price)}** | {get_trend_icon(chg_24h)} `{chg_24h:+.2f}%` | Real-time Aggregate Spot |
| **24h Price Range** | `{format_usd(low_24h)} — {format_usd(high_24h)}` | `Spread: {format_usd(spread)}` | Intraday Volatility Band |
| **24h Trading Volume** | `{format_compact_usd(vol_usd)}` | `{vol_btc:,.2f} BTC` | 24h Spot Pair Turnover |
| **Estimated Market Cap** | `{format_compact_usd(mcap)}` | `Rank #1` | Circulating Supply: ~19.85M BTC |

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
{performance_matrix_content}

---

### 🗓️ Rolling 7-Day Price Action Log

Detailed historical daily candlestick telemetry for the last 7 trading sessions.

| Date (UTC) | Open (USD) | High (USD) | Low (USD) | Close (USD) | 24h Change | Volume (BTC) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{seven_day_table_content}

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

*Last Telemetry Sync: `{full_timestamp_str} UTC` • Data Feed: `{data['source']} (BTC/USD)` • Status: `Operational (HTTP 200 OK)`*

</div>
"""
    return markdown_template.strip() + "\n"


def main():
    print("=" * 60)
    print("🚀 Running Bitcoin & Crypto Historical Tracker (fetch_btc.py)")
    print("=" * 60)

    try:
        data = get_market_data()
    except Exception as e:
        print(f"[✗] Critical Error: Unable to fetch market data from any source: {e}")
        sys.exit(1)

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    candles_30d = data["candles"][-30:] if len(data["candles"]) >= 30 else data["candles"]
    svg_content = generate_svg_chart(candles_30d)
    svg_path = os.path.join(assets_dir, "btc_trend.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[✓] Generated assets/btc_trend.svg successfully ({len(svg_content)} bytes)")

    readme_content = generate_readme_content(data, now_utc)
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"[✓] Updated README.md successfully at {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
