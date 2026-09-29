-- User-Defined Functions

CREATE OR REPLACE FUNCTION add_tax(p_price NUMERIC,p_rate NUMERIC) RETURNS NUMERIC LANGUAGE plpgsql AS $$ BEGIN RETURN p_price*(1+p_rate); END; $$;
SELECT add_tax(1000,0.18);

-- Challenge
-- Extend the example using earlier concepts and verify the result.