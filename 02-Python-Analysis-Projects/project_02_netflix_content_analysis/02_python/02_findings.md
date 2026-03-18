# Dataset Audit Findings and Cleaning Decisions:

## Objective:
The purpose of this document is to record observations from the dataset audit and define how each data quality issue will be handled before analysis.

---

## Dataset Overview:
- Dataset Shape (before cleaning): (8807, 12)
				- Rows: 8807
				- Columns: 12

- Duplicate Rows: 0

---

## Missing Values:
The following columns contain missing values:
- director: 2634
- cast: 825
- country: 831
- date_added: 10
- rating: 4
- duration: 3

---

## Observations:
- Several columns contain missing values, particularly 'director', 'cast', and 'country'.
- The 'date_added' column is stored as text and requires conversion to datetime.
- The 'duration' column contains mixed formats (minutes and seasons).
- No duplicate rows are present.

---

## Cleaning Decisions:
- director: leave as missing.
- cast: leave as missing.
- country: leave as missing.
- date_added: convert to datetime.
- rating: replace missing values with "Unknown".
- duration: leave as missing.

No rows will be removed as all records contain useful information.

---

## Notes:
Missing values will be handled in a way that preserved as much original data as possible while allowing for accurate analysis.
