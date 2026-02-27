# Customer Sales Analysis:

## Problem Statement:
The goal of this project is to analyse customer sales data to understand revenue performance, customer value, and product sales patterns.

The analysis focuses on answering practical business questions such as:
- How much revenue is being generated?
- Which products and customers contribute the most to sales?
- Are there high-volume products that generate relatively low revenue?

## Dataset:
The dataset represents a simplified sales system and consists of the following tables:

- customers: Customer identifiers and names.
- products: Product details and pricing.
- orders: Individual sales transactions including quantities and dates.

The data structure reflects a typical transactional sales database used in many real-world systems.

## Approach:
The analysis was performed using SQL and follows a question-driven approach:
1. Understand the structure of the data and relationships between tables.
2. Define clear analytical questions before writing queries.
3. Use JOINs to combine customer, product, and order data.
4. Aggregate and group data to calculate revenue and sales metrics.
5. Validate results to ensure accuracy and consistency.

Each query is written to answer a specific question and is documented for clarity,

## Tools Used:
- PostgreSQL.
- SQL.

## Key Questions:
- What is the total revenue generated from sales?
- Which products sell the most by quantity?
- Which customers contribute the highest total revenue?
- How does revenue change over time?
- Which products sell frequently but generate relatively low revenue?

## Project Folder Structure:
- 'analysis/'
Contains all SQL scripts: schema creation (schema.sql), sample data inserts (data.sql), and analytical queries (queries,sql).

- 'results/': 
Summarises the findings in plain language (results.md). Screenshots or tables from query outputs are included as supporrting evidence in 'images/'.

- 'lessons-learned,md': Short reflection on what was learned and insights gained from the analysis.


## How to Run This Project (psql):
1. Connect to your database:
- 'psql -U your_username -d database_name' ('psql -U thando -d customer_sales')

2. Create tables:
- '\i analysis/schema.sql'

3. Insert sample data:
- '\i analysis/data.sql'

4. Run analysis queries:
- '\i analysis/queries.sql'
