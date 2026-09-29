-- Stored Procedures

CREATE OR REPLACE PROCEDURE add_employee(p_fname VARCHAR,p_lname VARCHAR,p_email VARCHAR,p_dept department,p_salary NUMERIC)
LANGUAGE plpgsql AS $$ BEGIN INSERT INTO employees(fname,lname,email,dept,salary) VALUES(p_fname,p_lname,p_email,p_dept,p_salary); END; $$;
CALL add_employee('Nikhil','Rao','nikhil@example.com','engineering',75000);

-- Challenge
-- Extend the example using earlier concepts and verify the result.