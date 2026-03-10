# Data Inspection Findings:

## Objective:
The objective of this document is to record the results of the dataset inspection. 
It summarises the structure of the dataset, identifies potential data quality issue such as missing values or duplicates, and determines whether any data cleaning is required before analysis.

---

## Dataset Shape:
- Rows: 9800
- Columns: 18

---

## Column Overview:
The dataset contains the following columns:
- Row ID
- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- Customer Name
- Segment
- Country
- City
- State
- Postal Code
- Region
- Product ID
- Category
- Sub-Category
- Product Name
- Sales

---

## Duplicate Rows:
- Duplicate Rows Detected: **0**
- No duplicate transactions were found in the dataset.

---

## Missing Values:
- Missing values detected in the following column:
	- Postal Code: **11**
- No other columns contain missing values.

---

## Data Quality Assessment:
The dataset is generally clean and suitable for analysis.

---

## Observations:
- No duplicate rows were detected.
- Only a small number of missing values were found in the **Postal Code** column.
- Postal codes are not required for the planned analysis of sales performance, product demand, customer behaviour, or regional sales distribution.

---

## Cleaning Decision:
- No data cleaning is required before proceeding with analysis.
- The dataset can be used directly for sales analysis.
