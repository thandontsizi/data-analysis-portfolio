# SQL Commands Reference:
This document lists commonly used SQL commands for data analysis. 
Each command is presented with its purpose and syntax for clarity and consistency.

## 1. Basic Querying:
### 1.1. SELECT:
- Command: SELECT
- Explanation: Retrieves data from one or more columns in the table.
- Syntax:
```sql
SELECT column1, column2 FROM table_name;
--------------------------------------------------------------------

## 2. Filtering Data:
### 2.1. WHERE:
- Command: WHERE
- Explanation: Filters rows based on specified conditions.
- Syntax:
SELECT *
FROM table_name
WHERE condition;

### 2.2. Comparison Operators:
- Syntax: =, !=, >, >=, <, <=
- Explanation: Used to compare values in filtering conditions.
--------------------------------------------------------------

## 3. Sorting Results:
### 3.1. ORDER BY:
- Command: ORDER BY
- Explanation: Sorts query results in ascending or descending order.
- Syntax: 
SELECT *
FROM table_name
ORDER BY column_name ASC|DESC;
--------------------------------------------------------------------

## 4. Aggregation Functions:
### 4.1. COUNT:
- Command: COUNT
- Explanation: Counts the number of rows returned by a query.
- Syntax:
SELECT COUNT(*)
FROM table_name;

### 4.2. SUM:
- Command: SUM
- Explanation: Calculates the total values in a numeric column.
- Syntax:
SELECT SUM(column_name)
FROM table_name;

### 4.3. AVG:
- Command: AVG
- Explanation: Calculates the average value of a numeric column.
- Syntax:
SELECT AVG(column_name)
FROM table_name;

### 4.4. MIN:
- Command: MIN
- Explanation: Returns the smallest value in a numeric column.
- Syntax:
SELECT MIN(column_name)
FROM table_name;

### 4.4. MAX:
- Command: MAX
- Explanation: Returns the largest value in a numeric column.
- Syntax:
SELECT MAX(column_name)
FROM table_name;
-------------------------------------------------------------

## 5. Grouping Data:
### 5.1. GROUP BY:
- Command: GROUP BY
- Explanation: Groups rows that share the same values and applies aggregate functions.
- Syntax: 
SELECT column_name, Aggregate-Function(*)
FROM table_name
GROUP BY column_name;

### 5.2. HAVING:
- Command: HAVING
- Explanation: Filters grouped data after aggregation is applied.
- Syntax:
SELECT column_name, Aggregate-Function(*)
FROM table_name
GROUP BY column_name
HAVING Aggregate-Function(*) > 5;
-----------------------------------------------------------------

## 6. Joining Tables:
### 6.1. INNER JOIN:
- Command: INNER JOIN
- Explanation: Returns rows where there is a match in both tables.
- Syntax:
SELECT *
FROM table1
INNER JOIN table2
ON table1.id = table2.id;

### 6.2. LEFT JOIN:
- Command: LEFT JOIN
- Explanation: Returns all rows from the left table and matching rows from the right table.
- Syntax: 
SELECT * 
FROM table1
LEFT JOIN table2 
ON table1.id = table2.id;
-------------------------------------------------------------------------------------------

## 7. Aliases:
### 7.1. AS:
- Command: AS
- Explanation: Renames columns or tables to improve readability.
- Syntax:
SELECT column_name 
AS alias_name 
FROM table_name;
----------------------------------------------------------------

## 8. Limiting Results:
### 8.1. LIMIT:
- Command: LIMIT
- Explanation: Restricts the number of rows returned by a query.
- Syntax: 
SELECT * 
FROM table_name
LIMIT number;
----------------------------------------------------------------

## 9. Data Cleaning:
### 9.1. DISTINCT:
- Command: DISTINCT
- Explanation: Returns only unique values from a column.
- Syntax: 
SELECT DISTINCT column_name
FROM table_name;

### 9.2. NULL:
- Command: NULL
- Explanation: Identifies rows with missing values in a column.
- Syntax:
SELECT * 
FROM table_name 
WHERE column_name IS NULL;
---------------------------------------------------------------

## 10. Comments:
- Syntax: -- This is a comment.
- Explanation: Adds notes or explanations within SQL queries.
