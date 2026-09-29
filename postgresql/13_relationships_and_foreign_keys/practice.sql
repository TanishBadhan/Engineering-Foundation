-- Relationships and Foreign Keys

SELECT c.c_name,o.o_id FROM customers c JOIN orders o ON o.c_id=c.c_id ORDER BY c.c_id,o.o_id;

-- Challenge
-- Extend the example using earlier concepts and verify the result.