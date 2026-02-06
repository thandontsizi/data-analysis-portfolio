-- ============================================================================================================
-- Customer Sales Analysis:
-- ============================================================================================================
-- This file contains SQL queries used to analyse the  purchasing behaviour of customers and sales performance.
-- Each section answers a specific business question.
-- ============================================================================================================


-- ------------------------------------------------------------------------------------------------------------
-- Assumed table structure:
-- ------------------------------------------------------------------------------------------------------------
-- Table name: customer_sales
--
-- Columns:
-- sales_id		INTEGER
-- customer_id		INTEGER
-- customer_name	TEXT/VARCHAR(50)
-- product		TEXT/VARCHAR(50)
-- quantity		INTEGER
-- price		DECIMAL
-- sale_date		DATE
-- ------------------------------------------------------------------------------------------------------------

-- 1. View all records in the sales table:
-- Purpose: Understand the raw data.
SELECT *
FROM sales

-- 2. Count total number of sales records:
-- Purpose: Determine dataset size.
SELECT COUNT(*) AS total_sales
FROM sales;

-- 3. Calculate total revenue:
-- Purpose: Measure overall sales performance.
SELECT SUM(quantity * price) AS total_revenue
FROM sales;

-- 4. Calculate average sale value:
-- Purpose: Understand typical transaction size.
SELECT AVG(quantity * price) AS average_sale_value
FROM sales;

-- 5. Total revenue per customer:
-- Purpose: Identify high-value customers.
SELECT
	customer_id,
	customer_name,
	SUM(quantity * price) AS customer_total_spent
FROM sales;
GROUP BY customer_id, customer_name
ORDER BY customer_total_spent DESC;

-- 6. Number of purchases per customer:
-- Purpose: Identify repeat customers.
SELECT
	customer_id,
	customer_name,
	COUNT(sale_id) AS total_purchases
FROM sales
GROUP BY customer_id, customer_name
ORDER BY total_purchases DESC;

-- 7. Best selling products by revenue:
-- Purpose: Identify top-performing products.
SELECT
	product,
	SUM(quantity * price) AS product_revenue
FROM sales
GROUP BY product
ORDER BY product_revenue DESC;

-- 8. Sales grouped  by date:
-- Purpose: Analyse daily sales trends.
SELECT
	sale_date,
	SUM(quantity * price) AS daily_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

-- 9. Customers who spent more than a specific amount:
-- Purpose: Filter high-value customers.
SELECT
	customer_id,
	customer_name,
	SUM(quantity * price) AS total_spent
FROM sales
GROUP BY customer_id, customer_name
HAVING SUM(quantity * price) > 1000
ORDER BY total_spent DESC;

-- 10. Top 5 customers by total spending:
-- Purpose: Quickly identify key customers.
SELECT
	customer_id,
	customer_name,
	SUM(quantity * price) AS total_spent
FROM sales
GROUP BY customer_id, customer_name
ORDER BY total_spent DESC
LIMIT 5;
