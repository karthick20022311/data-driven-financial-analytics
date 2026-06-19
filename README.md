# 📈 Data-Driven Financial Analytics

A data-driven financial analytics project that collects, processes, analyzes, and visualizes stock market data to identify performance trends across companies and sectors.

## Overview

This project analyzes historical stock price data to surface performance insights — such as which stocks delivered the highest returns over time — and presents the results through an interactive Streamlit dashboard backed by exploratory analysis in Jupyter notebooks.

## Features

- **Stock Data Analysis** — Computes returns for each stock symbol based on historical closing prices.
- **Top Gainers Ranking** — Automatically ranks and displays the top 10 best-performing stocks by return.
- **Interactive Dashboard** — Built with Streamlit, showing:
  - A sortable table of top-performing stocks
  - A bar chart visualizing returns across the top gainers
- **Exploratory Analysis** — Jupyter notebooks (`financial_analysis.ipynb`) for deeper, ad-hoc exploration of the dataset.

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python (Jupyter Notebook + script) |
| Data Handling | Pandas |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |

## Project Structure

```
data-driven-financial-analytics/
├── streamlit_app.py           # Main Streamlit dashboard application
├── financial_analysis.ipynb   # Exploratory data analysis notebook
├── Untitled.ipynb              # Supplementary/working notebook
├── master_stock_data.csv      # Core stock market dataset (date, symbol, close, etc.)
├── requirements.txt           # Python dependencies
└── .devcontainer/             # Dev container configuration
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/karthick20022311/data-driven-financial-analytics.git
   cd data-driven-financial-analytics
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Launch the dashboard
```bash
streamlit run streamlit_app.py
```
Open the local URL shown in your terminal (typically `http://localhost:8501`) to view:
- A table of the **Top 10 Gainers** by yearly return
- A bar chart comparing returns across those top-performing stocks

### Explore further in the notebook
```bash
jupyter notebook financial_analysis.ipynb
```

## Dataset

`master_stock_data.csv` is expected to contain at least the following columns:
- `date` — trading date
- `symbol` — stock ticker/company symbol
- `close` — closing price

Yearly return per symbol is calculated as:

```
(last_close - first_close) / first_close
```

## License

This project is open-source and available for educational and personal use.

## Author

**Karthick** — [GitHub Profile](https://github.com/karthick20022311)
