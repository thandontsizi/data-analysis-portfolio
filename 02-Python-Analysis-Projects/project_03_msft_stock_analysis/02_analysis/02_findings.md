# Dataset Audit Findings and Cleaning Decisions:

## Objective:
The purpose of this document is to record observations from the dataset audit and define how each data-related issue will be handled before analysis.

---

## Dataset Overview:
Dataset Shape (before cleaning): (10072, 23)
- Rows: 10072
- Columns: 23

- Duplicate Rows: 0

---

## Missing Values:
The following columns contain missing values:
- Daily_Return_Pct: 1
- MA_20: 19
- MA_50: 49
- MA_200: 199
- Volatility_20D: 20
- Volume_MA_20: 19
- RSI_14: 14
- BB_Upper: 19
- BB_Lower: 19
- BB_Middle: 19

---

## Observations:
- The dataset includes both raw stock data and pre-calculated technical indicators.
- Technical indicators include moving averages, volatility, RSI, MACD, and Bollinger Bands.
- Missing values are present only in these engineered columns and are expected due to rolling calculations.
- The `Date` column is stored as text and requires conversion to datetime format.
- No duplicate rows are present.
- The dataset spans a long time period (1986–2026), which is broader than required for this analysis.

---

## Cleaning Decisions:
- Engineered columns (e.g. moving averages, RSI, MACD, Bollinger Bands) will be removed/dropped.
- The analysis will use only raw columns:
  - Date
  - Open
  - High
  - Low
  - Close
  - Volume

- Date: convert to datetime format.
- Dataset will be sorted chronologically.
- Dataset will be filtered to a recent time period (e.g. 2015 onwards) to keep the analysis focused.
- No rows will be removed after filtering, as the remaining data is complete and usable.

---

## Notes:
The analysis will be performed using raw data only to ensure that all calculations (e.g. returns, moving averages, volatility) are done independently within the project.
