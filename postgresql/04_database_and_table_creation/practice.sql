-- database and table creation

CREATE TABLE demo(id SERIAL PRIMARY KEY,name TEXT NOT NULL);
INSERT INTO demo(name) VALUES ('example');
SELECT * FROM demo;
DROP TABLE demo;

-- Challenge
-- Extend the example using earlier concepts and verify the result.