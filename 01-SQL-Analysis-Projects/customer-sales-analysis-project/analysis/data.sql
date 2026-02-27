-- Sample Data Inserts:

--- Customers Table Data Insertion:
INSERT INTO customers (customer_name, email) VALUES
('Alice M.', 'alice@example.com'),
('Brian K.', 'brian@example.com'),
('Chris N.', 'chris@example.com'),
('Dineo S.', 'dineo@example.com'),
('Ethan P.', 'ethan@example.com');

--- Products Table Data Insertion:
INSERT INTO products (product_name, price) VALUES
('Laptop', 12000.00),
('Monitor', 3500.00),
('Keyboard', 600.00),
('Mouse', 250.00),
('USB-C Cable', 150.00);

--- Orders Table Data Insertion:
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, '2026-02-01'),
(1, 4, 2, '2026-02-01'),
(2, 2, 1, '2026-02-02'),
(2, 5, 3, '2026-02-03'),
(3, 3, 1, '2026-02-04'),
(3, 4, 1, '2026-02-04'),
(4, 2, 2, '2026-02-10'),
(4, 5, 1, '2026-02-11'),
(5, 4, 4, '2026-02-12');
