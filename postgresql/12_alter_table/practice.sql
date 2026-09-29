-- ALTER TABLE

CREATE TABLE demo(id SERIAL PRIMARY KEY,name TEXT);
ALTER TABLE demo ADD COLUMN active BOOLEAN DEFAULT TRUE;
ALTER TABLE demo RENAME COLUMN name TO display_name;
DROP TABLE demo;

-- Challenge
-- Extend the example using earlier concepts and verify the result.