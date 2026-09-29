-- Triggers

CREATE TABLE employee_audit(audit_id SERIAL PRIMARY KEY,emp_id INT,changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE OR REPLACE FUNCTION audit_employee_update() RETURNS TRIGGER LANGUAGE plpgsql AS $$ BEGIN INSERT INTO employee_audit(emp_id) VALUES(NEW.emp_id); RETURN NEW; END; $$;
CREATE TRIGGER employee_update_audit AFTER UPDATE ON employees FOR EACH ROW EXECUTE FUNCTION audit_employee_update();

-- Challenge
-- Extend the example using earlier concepts and verify the result.