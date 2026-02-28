# Lessons Learned: Customer Sales Analysis.

## 1. Schema Design Matters:
- Keeping the databse structure minimal (customers, products, orders) made the analysis clearer and easier to reason about. 
Adding unnecessary tables introduces complexity without analytical benefit.

## 2. JOINs Require Careful Thinking:
- Revenue could not be calculated from the orders table alone. Understanding how foreign keys connect tables is essential when working with relational databases.

## 3. Aggregation Requires Structure:
- Using SUM together with GROUP BY reinforced the importance of defining the correct level of aggregation. Without proper grouping, SQL either throws an error or produces misleading results.

## 4. Data Interpretation Is Different From Data Retrieval:
- Writing queries produces numbers. Interpreting those numbers produces insights. Communicating concentration risk and revenue distribution was just as important as calculating totals.

## 5. Execution Environment Matters:
- Running the queries in a real PostgreSQL environment (instead of just writing SQL statically) highlighted practical issues such as permissions, database roles, and execution order.
