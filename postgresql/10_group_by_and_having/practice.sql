-- GROUP BY and HAVING

SELECT c_id,COUNT(*) AS order_count FROM orders GROUP BY c_id HAVING COUNT(*)>=2 ORDER BY order_count DESC;

-- Challenge
-- Extend the example using earlier concepts and verify the result.