-- Schema: Customer Sales Analysis.


--- Creating Customer Information Table:
CREATE TABLE customers (
	customer_id SERIAL PRIMARY KEY,
	customer_name VARCHAR(100),
	email VARCHAR(100)
);

--- Creating Product Information Table:
CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(100),
	price NUMERIC(10,2)
);

--- Creating Order Information Table:
CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(customer_id),
	product_id INT REFERENCES products(product_id),
	quantity INT,
	order_date DATE
);
