-- JOINs

SELECT c.c_name,o.o_id FROM customers c JOIN orders o ON o.c_id=c.c_id;
SELECT p.p_name,oi.quantity FROM products p LEFT JOIN order_items oi ON oi.p_id=p.p_id;

-- Challenge
-- Extend the example using earlier concepts and verify the result.