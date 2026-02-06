# SQL Analysis Self-Test:
This test is designed to assess understanding of SQL concepts used in data analysis. 
All questions should be answered without looking up solutions.

## Section 1: Basic Querying.
1. Write an SQL query to select all columns from a table called 'employees'.
2. Write an SQL query to select only the 'name' and 'salary' columns from the 'employees' table.
3. Why is it better to select specific columns instead of using 'SELECT *' in analysis queries?
-----------------------------------------------------------------------------------------------

## Section 2: Filtering Data.
1. Write an SQL query to return all records from a 'customers' table where the country is 'South Africa'.
2. Write an SQL query to return all orders with an amount greater that 1000.
3. Explain the difference between using '=' and '!=' in a 'WHERE' clause.
-------------------------------------------------------------------------

## Section 3: Sorting Results.
1. Write an SQL query to sort employees by salary in descending order.
2. What is the default sorting order when using 'ORDER BY' without specifying 'ASC' or 'DESC'?
----------------------------------------------------------------------------------------------

## Section 4: Aggregation.
1. Write an SQL query to count the total number of rows in a table called 'sales'.
2. Write an SQL query to calculate the average sales amount from the 'sales' table.
3. What is the difference between 'COUNT(*)' and 'COUNT(column_name)'?
----------------------------------------------------------------------

## Section 5: Grouping Data.
1. Write an SQL query to count the number of employees in each department.
2. Why is 'GROUP BY' required when using aggregate functions with non-aggregated columns?
-----------------------------------------------------------------------------------------

## Section 6: Filtering Aggregated Results.
1. Write an SQL query to return departments with more than 5 employees.
2. Explain why 'HAVING' is used instead of 'WHERE' in aggregate queries.
------------------------------------------------------------------------

## Section 7: Joining Tables.
1. Explain the difference between an 'INNER JOIN' and a 'LEFT JOIN'.
2. Write an SQL query to return all customers and their orders including cutomers who have not placed any orders.
-----------------------------------------------------------------------------------------------------------------

## Section 8: Aliases and Readability.
1. Write an SQL query that renames the column 'total_amount' as "TotalSales' in the result output.
2. Why are aliases useful in complex SQL queries.
-------------------------------------------------

## Section 9: Limiting and Cleaning Data.
1. Write an SQL query to return only the first 10 rows from a table.
2. Write an SQL query to find unique values in a column called 'city'.
3. Write an SQL query to return all rows where the 'email' fiels is missing.
----------------------------------------------------------------------------

## Section 10: Practical Scenarios.
1. You are given a table called 'orders' containing customer purchases. 
The table includes the order ID, customer ID, order date, and the order amount (all column names with underscores e.g. customer_id, etc).

Describe how you would write an SQL query to:
- Find the total amount spent by each customer.
- Return only customers who have spent more than 5000.

2. A dataset contains duplicate customer records.

Explain how you would:
- Identify duplicate values using SQL.
- Return a list of unique customers.

3. You are analysing employee salaries across departments.

Describe how you would:
- Calculate the average salary per department.
- Sort the results fromo highest to lowest average salary.

4. You have two tables:
- 'customers'
- 'orders'

Not all customers have placed orders. 
Explain:
- Which type of JOIN you would use.
- Why this JOIN is appropriate.
- What result you expect from the query.

5. A manager asks for a quick preview of a very large table.

Explain:
- Which SQL clause you would use.
- Why it is useful in this situation.
