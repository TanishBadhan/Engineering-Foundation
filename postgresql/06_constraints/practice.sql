-- constraint

CREATE TABLE demo(id SERIAL PRIMARY KEY,email TEXT UNIQUE NOT NULL,age INT CHECK(age>=0),active BOOLEAN DEFAULT TRUE);
DROP TABLE demo;

-- Challenge
-- Extend the example using earlier concepts and verify the result.