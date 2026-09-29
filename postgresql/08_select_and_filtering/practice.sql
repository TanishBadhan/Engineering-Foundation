-- SELECT and Filtering

SELECT c_id,c_name FROM customers WHERE c_id BETWEEN 1 AND 5 ORDER BY c_id;
SELECT p_name,price FROM products WHERE price>=1000 ORDER BY price DESC LIMIT 5;

-- Challenge
-- Extend the example using earlier concepts and verify the result.