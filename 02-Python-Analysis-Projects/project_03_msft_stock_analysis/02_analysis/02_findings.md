# Dataset Findings:

## Overview:
The dataset contains historical daily stock price data for Microsoft (MSFT) including price, volume, and several pre-calculated technical indicators.

The goal of this step is to assess the structure, quality, and suitability of the dataset for analysis.

---

## Structure:
- The dataset contains 10,000+ rows and 20+ columns.
- Each row represents a single trading day.
- The dataset includes both raw market data and engineered features.

---

## Key Observations:
### 1. Presence of Engineered Features:
The dataset includes pre-calculated indicators such as:
- Moving averages (MA_20, MA_50, MA_200).
- Volatility measures (Volatility_20D).
- Momentum indicators (RSI, MACD).
- Bollinger Bands (BB_Upper, BB_Lower, BB_Middle).
- Daily returns and ranges.

These features were not generated as part of this project.

---

### 2. Decision to Use Raw Data Only:
To ensure that all analysis is performed independently, only the following raw columns will be used:
- Date
- Open
- High
- Low
- Close
- Volume

All pre-calculated columns will be excluded.

---

### 3. Data Types:
- The 'Date' column is stored as an object and will need to be converted to datetime format.
- Numerical columns (prices and volume) are correctly stored.

---

### 4. Missing Values:
- Missing values are present only in the pre-engineered columns (e.g. moving averages, RSI).
- These are expected due to rolling calculations.

After removing the pre-engineered columns, the dataset is expected to have no missing values.

---

### 5. Duplicates:
- No duplicate rows were found.

---

### 6. Dataset Size and Scope:
- The dataset spans multiple decades (1986-2026).
- For this analysis, the dataset will be filtered to a more recent and relevant time period to keep the scope focused and manageable.

---

## Summary of Actions:
The following steps will be taken during data cleaning:
- Remove all engineered columns.
- Convert 'Date' to datetime format.
- Sort data chronologically.
- Filter dataset to a defined time range (e.g. 2015 onwards).

These steps ensure that the analysis is based on clean, reliable, and independently processed data.
