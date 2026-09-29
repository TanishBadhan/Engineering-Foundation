-- Views

CREATE OR REPLACE VIEW customer_order_summary AS SELECT c_id,COUNT(*) AS order_count FROM orders GROUP BY c_id;
SELECT * FROM customer_order_summary;
DROP VIEW customer_order_summary;

-- Challenge
-- Extend the example using earlier concepts and verify the result.