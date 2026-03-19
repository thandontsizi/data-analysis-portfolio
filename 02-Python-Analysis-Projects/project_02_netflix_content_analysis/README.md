
# Netflix Content Analysis:

## Project Overview:
This project explores Netflix's catalog of movies and TV shows to identify patterns in content production, distribution, and platform growth. The analysis focuses on how content varies by type, country, genre, and time using a structured workflow that combines Python and SQL.

---

## Objective:
The objective of this project is to demonstrate the ability to:
- Inspect and understand unfamiliar datasets.
- Identify and document data quality issues.
- Clean and prepare data for analysis.
- Perform analysis using both Python and SQL.
- Communicate insights clearly and effectively.

---

## Dataset:
- **Source:** Netflix Titles Dataset
- **Link:** https://www.kaggle.com/datasets/shivamb/netflix-shows

The dataset contains metadata about Netflix content, including:
- Title
- Content type (Movie or TV Show)
- Director
- Cast
- Country
- Date added
- Release year
- Rating
- Duration
- Genre
- Description

---

## Tools Used:
The analysis uses the following tools:
- Python (pandas).
- SQL (PostgreSQL).
- Git & GitHub.

---

## Workflow:
The project follows a structured, end-to-end data analysis workflow:
1. Data inspection:
	- '02_python/01_dataset_audit.py'.
2. Data quality assessment and documentation:
	- '02_python/02_findings.md'.
3. Data cleaning and preparation:
	- '02_python/03_data_cleaning.py'
4. Data analysis (Python):
	- '02_python/04_python_analysis.py'
5. Data analysis (SQL): 
	- '03_sql/01_sql_analysis.sql'.
6. Insights and reporting:
	- '04_results/insights.md'

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

## Key Insights:
- Movies dominate the Netflix catalog (~70%).
- Content growth accelerated after 2015.
- The United States leads in content production.
- Drama and international genres are most common.
- TV Shows are growing but remain fewer than Movies.

---

## What This Project Demonstrates:
- Ability to work with real-world, imperfect data.
- Strong data cleaning and preprocessing skills.
- Consistent analysis across multiple tools (Python and SQL).
- Understanding of reproducible data workflows.
- Clear communication of analytical findings.
