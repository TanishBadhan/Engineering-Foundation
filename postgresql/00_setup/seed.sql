INSERT INTO customers(c_name,c_mail) VALUES
('Tanish Badhan','tanish@example.com'),('Priya','priya@example.com'),('Ayush','ayush@example.com'),
('Ankush','ankush@example.com'),('Ankit','ankit@example.com'),('Teji','teji@example.com'),
('Vaibhavi','vaibhavi@example.com'),('Surmai','surmai@example.com'),('Aadhya','aadhya@example.com'),
('Namami','namami@example.com'),('Priyankal','priyankal@example.com');

INSERT INTO products(p_name,price) VALUES
('Laptop',55000),('Mouse',500),('Keyboard',800),('Cable',250),('Cream',200),('PowerBank',1000),
('Watch',1800),('Adapter',1250),('Earphones',5000),('Mattress',9000),('TV',80000),('Sofa',11250),
('Chair',200),('Desk',1200),('Tablet',50000),('Iphone',66250);

INSERT INTO orders(c_id,o_date) VALUES
(1,'2026-01-05'),(2,'2026-01-06'),(11,'2026-01-07'),(1,'2026-01-08'),(9,'2026-01-09'),
(11,'2026-01-10'),(2,'2026-01-11'),(2,'2026-01-12'),(5,'2026-01-13'),(6,'2026-01-14'),
(11,'2026-01-15'),(4,'2026-01-16'),(1,'2026-01-17'),(4,'2026-01-18'),(7,'2026-01-19'),
(7,'2026-01-20'),(8,'2026-01-21'),(9,'2026-01-22'),(7,'2026-01-23'),(9,'2026-01-24'),
(8,'2026-01-25'),(10,'2026-01-26'),(10,'2026-01-27'),(3,'2026-01-28'),(3,'2026-01-29'),
(9,'2026-01-30'),(8,'2026-01-31'),(8,'2026-02-01'),(2,'2026-02-02'),(1,'2026-02-03'),(4,'2026-02-04');

INSERT INTO order_items(o_id,p_id,quantity) VALUES
(1,1,1),(2,2,2),(3,5,1),(4,3,1),(5,9,2),(6,6,1),(7,4,3),(8,7,1),
(9,2,2),(10,8,1),(11,11,1),(12,12,1),(13,14,2),(14,13,4),(15,10,1),
(16,15,1),(17,16,1),(18,3,2),(19,6,1),(20,4,2),(21,1,1),(22,8,2),
(23,5,3),(24,7,1),(25,2,5),(26,9,1),(27,13,2),(28,14,1),(29,6,2),(30,15,1),(31,16,1);

INSERT INTO departments(dept_name) VALUES
('Engineering'),('Sales'),('HR'),('Finance'),('Marketing');

INSERT INTO employees(fname,lname,email,dept,salary) VALUES
('Aarav','Sharma','aarav@example.com','engineering',90000),
('Meera','Singh','meera@example.com','sales',70000),
('Rohan','Kumar','rohan@example.com','finance',80000),
('Isha','Gupta','isha@example.com','hr',65000),
('Kabir','Verma','kabir@example.com','marketing',68000);