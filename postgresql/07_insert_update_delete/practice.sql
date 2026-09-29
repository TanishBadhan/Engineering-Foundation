-- INSERT UPDATE DELETE

INSERT INTO customers(c_name,c_mail) VALUES ('Practice User','practice@example.com');
UPDATE customers SET c_name='Practice Customer' WHERE c_mail='practice@example.com';
DELETE FROM customers WHERE c_mail='practice@example.com';

-- Challenge
-- Extend the example using earlier concepts and verify the result.