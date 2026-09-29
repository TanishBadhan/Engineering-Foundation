-- CTEs

WITH customer_orders AS (SELECT c_id,COUNT(*) AS order_count FROM orders GROUP BY c_id)
SELECT c.c_name,COALESCE(co.order_count,0) FROM customers c LEFT JOIN customer_orders co ON co.c_id=c.c_id;

-- Challenge
-- Extend the example using earlier concepts and verify the result.