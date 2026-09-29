-- Window Functions

SELECT c_id,o_id,o_date,ROW_NUMBER() OVER(PARTITION BY c_id ORDER BY o_date) AS order_number FROM orders;
SELECT o_id,o_date,LAG(o_date) OVER(ORDER BY o_date) AS previous_order FROM orders;

-- Challenge
-- Extend the example using earlier concepts and verify the result.