-- CASE and COALESCE

SELECT p_name,CASE WHEN price>=50000 THEN 'high' WHEN price>=5000 THEN 'medium' ELSE 'low' END AS price_band FROM products;
SELECT COALESCE(c_mail,'missing') FROM customers;

-- Challenge
-- Extend the example using earlier concepts and verify the result.