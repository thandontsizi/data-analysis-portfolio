-- Customer Sales Analysis Queries:

-- 1. Total Revenue:
SELECT
	SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id;

-- 2. Top Products by Quantity Sold:
SELECT
	p.product_name,
	SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;

-- 3. Top Customers by Total Spent:
SELECT
	c.customer_name,
	SUM(o.quantity * p.price) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent;

-- 4. Revenue by Date:
SELECT
	o.order_date,
	SUM(o.quantity * p.price) AS daily_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY o.order_date
ORDER BY o.order_date;
