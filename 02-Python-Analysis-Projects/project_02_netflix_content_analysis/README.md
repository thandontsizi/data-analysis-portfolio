
# Netflix Content Analysis:

## Project Overview:
This project explores Netflix's catalog of movies and TV shows to identify patterns in content production, distribution, and platform growth. The analysis investigates how content varies by type, country, genre, and release year.

The goal of the project is to demonstrate a practical data analysis workflow using SQL and Python on a real-world dataset.

---

## Dataset:
- **Source:** Netflix Titles Dataset
- **Link:** https://www.kaggle.com/datasets/shivamb/netflix-shows

The dataset contains metadata about Netflix content including:
- title
- content type (Movie or TV Show)
- director
- cast
- country
- date added
- release year
- rating
- duration
- genre
- description

---

## Tools Used:
The analysis uses the following tools:
- PostgreSQL (SQL analysis)
- Python
- pandas
- GNU nano
- Git
- GitHub

---

## Workflow:
The project follows a structured analysis workflow:
1. Inspect the dataset structure: 'python/01_dataset_audit.py'.
2. Document findings from the audit: 'python/02_findings.md'.
3. Perform Python analysis: 'python/03_python_analysis.py'.
4. Perform SQL analysis: 'sql/01_sql_analysis.sql'.
5. Communicate insights: 'results/insights.md'

---

## Project Structure:
```bash
project_02_netflix_content_analysis
├── 01_data
│   ├── cleaned_dataset.csv
│   ├── netflix_titles.csv
│   └── netflix_titles.csv:Zone.Identifier
├── 02_python
│   ├── 01_dataset_audit.py
│   ├── 02_findings.md
│   ├── 03_dataset_cleaning.py
│   └── 04_python_analysis.py
├── 03_sql
│   └── 01_sql_analysis.sql
├── 04_results
│   └── insights.md
└── README.md
```

---

## Objective:
The objective of this project is to demonstrate the ability to:
- inspect unfamiliar data.
- identify and document data quality issues.
- prepare datasets for analysis.
- analyse data using SQL and Python.
- Communicate findings clearly.
