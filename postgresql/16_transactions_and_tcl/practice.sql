-- Transactions and TCL

BEGIN;
UPDATE products SET price=price+10 WHERE p_id=2;
SAVEPOINT s1;
UPDATE products SET price=price+100 WHERE p_id=2;
ROLLBACK TO SAVEPOINT s1;
ROLLBACK;

-- Challenge
-- Extend the example using earlier concepts and verify the result.