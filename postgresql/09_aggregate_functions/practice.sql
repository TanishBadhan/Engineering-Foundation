-- Aggregate Functions

SELECT COUNT(*) FROM customers;
SELECT SUM(quantity) FROM order_items;
SELECT AVG(price),MIN(price),MAX(price) FROM products;

-- Challenge
-- Extend the example using earlier concepts and verify the result.