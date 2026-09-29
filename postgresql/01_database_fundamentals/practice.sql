-- Database Fundamentals

SELECT current_database();
SELECT current_schema();
SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name;

-- Challenge
-- Extend the example using earlier concepts and verify the result.