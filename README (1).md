# 📊 Stock Market Analytics Dashboard

An end-to-end stock market analytics project that pulls live stock data, processes it through a database pipeline, and visualizes it in an interactive Power BI dashboard — including advanced technical indicators and multi-stock comparison.

---

## 🚀 Project Overview

This project tracks and analyzes stock performance for **RELIANCE.NS** and **TCS.NS** (NSE-listed stocks), combining a full data engineering pipeline with financial analytics and interactive BI visualization.

**Key highlights:**
- Automated data extraction using Python (`yfinance`)
- Structured storage in a MySQL database
- Advanced DAX-based financial metrics in Power BI
- Multi-stock comparison view for relative performance analysis

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Data Extraction | Python (`yfinance`, `pandas`) |
| Data Storage | MySQL |
| Data Transformation | Python (rolling averages, % change) + Power Query |
| Visualization & Analytics | Power BI (DAX) |

---

## 🔄 Data Pipeline

1. **Extract** — Stock price data (Open, High, Low, Close, Volume) fetched via `yfinance` for the last 3 months.
2. **Transform** — 7-day Moving Average and Daily Return (%) calculated in Python using `pandas`.
3. **Load** — Cleaned data inserted into a MySQL table (`stock_prices`), with a `ticker` column identifying each stock — enabling multi-stock storage in a single table.
4. **Visualize** — Power BI connects directly to MySQL and refreshes to reflect the latest data.

---

## 📈 Dashboard Features

### Page 1 — Single Stock Deep Dive
- KPI cards: Average Daily Return, Max/Min Close Price, Total Volume
- Close Price vs 7-Day Moving Average trend chart
- Daily Returns chart with conditional color formatting (green = gain, red = loss)
- Trading Volume over time
- **Advanced DAX metrics:**
  - **Cumulative Return %** — total return over the selected period
  - **Volatility** — measure of price fluctuation risk
  - **RSI (Relative Strength Index)** — momentum indicator (0–100 scale)
- Interactive Date Range and Ticker slicers

### Page 2 — Stock Comparison
- Overlaid Close Price trend for both stocks
- Cumulative Return % comparison bar chart
- Ticker toggle buttons for filtering

---

## 💡 Key Insights

- TCS.NS delivered a higher cumulative return than RELIANCE.NS over the analyzed period, despite trading at a significantly higher price point.
- Volatility and RSI metrics provide a quick read on risk and momentum without needing to manually inspect price charts.

---

## 📌 Future Improvements

- Add more stocks for broader sector comparison
- Automate the Python data refresh on a schedule
- Add sector-level aggregation and benchmarking against a market index

---

## 📷 Screenshots

*(Add dashboard screenshots here)*

---

## 🙋 About This Project

Built as a hands-on project to practice the full analytics pipeline — from raw data extraction to business-ready dashboards — combining Python, SQL, and Power BI/DAX skills.
