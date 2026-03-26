# Microsoft (MSFT) Stock Analysis:

## Project Overview:
This project explores Microsoft's historical stock price data to identify trends, patterns, and market behaviour over time. The analysis focuses on price movements, volatility, and trading activity using a structured workflow in Python.

---

## Objective:
The objective of this project is to demonstrate the ability to:
- Inspect and understand time-series financial data.
- Identify and document data quality issues.
- Clean and prepare data for analysis.
- Perform numerical and trend-based analysis using Python.
- Communicate insights clearly and effectively.

---

## Dataset Information:
- **Source:** MSFT Stock Data 1986-2026
- **Link:** https://www.kaggle.com/datasets/omarshahrukh/msft-stock-data-19862026

The dataset contains daily stock market data including:
- Date.
- Open, High, Low, Close prices.
- Volume.
- Derived metrics such as return technical indicators.

---

## Tools Used:
The analysis uses the following tools:
- Python (pandas, NumPy).
- Matplotlib.
- Git & GitHub.
- Linux (WSL).

---

## Workflow:
The project follows a structured, end-to-end data analysis workflow:

1. **Data inspection:**
	- ['02_analysis/01_dataset_audit.py'](02_analysis/01_dataset_audit.py)

2. **Data quality assessment and documentation:**
	- ['02_analysis/02_findings.md'](02_analysis/02_findings.md)

3. **Data cleaning and preparation:**
	- ['02_analysis/03_dataset_cleaning.py'](02_analysis/03_dataset_cleaning.py)
	- Created:
		- Daily Returns.
		- Moving Averages (7-day, 30-day).
		- Rolling Volatility.
		
4. **Data analysis:**
	- ['02_analysis/04_analysis.py'](02_analysis/04_analysis.py)
	
5. **Data visualisation:**
	- ['02_analysis/05_visualisation.py'](02_analysis/05_visualisation.py)
	- Generated plots for:
		- Price trends.
		- Moving averages.
		- Daily returns.
		- Volatility.
		- Yearly averages.

6. **Insights and reporting:**
	- ['03_results/insights.md'](03_results/insights.md)

---

## Project Structure:
```bash
../project_03_msft_stock_analysis
├── 01_data
│   ├── analysed_msft_stock_prices.csv
│   ├── cleaned_msft_stock_prices.csv
│   └── msft_stock_prices.csv
├── 02_analysis
│   ├── 01_dataset_audit.py
│   ├── 02_findings.md
│   ├── 03_dataset_cleaning.py
│   ├── 04_analysis.py
│   └── 05_visualisation.py
├── 03_results
│   ├── insights.md
│   └── plots
│       ├── close_price.png
│       ├── daily_returns.png
│       ├── moving_averages.png
│       ├── volatility.png
│       └── yearly_average.png
└── README.md
```

---

## Analysis Questions:
The analysis focuses on answering the following:
- How has Microsoft's stock price changed over time?
- What overall trends can be observed in the data?
- Are there periods of rapid growth or decline?
- How stable or unstable are price changes over time?
- How do short-term trends compare to longer-term trends?
- How has trading activity (volume) changed over time?

---

## Key Insights:
- Microsoft's stock shows a strong long-term upward trend, with consistent growth in yearly average prices.
- Daily price movements fluctuate frequently, indicating regular short-term volatility despite long-term growth.
- Moving averages (7-day and 30-day) clearly highlight the underlying upward trend by smoothing short-term noise.
- Volatility varies over time, showing periods of both stability and increased market uncertainty.
- Overall, the data reflects sustained growth combined with natural day-by-day variability.
