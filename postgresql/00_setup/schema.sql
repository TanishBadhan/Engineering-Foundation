CREATE TYPE department AS ENUM ('engineering','sales','hr','finance','marketing');

CREATE TABLE customers (
 c_id SERIAL PRIMARY KEY,
 c_name VARCHAR(100) NOT NULL,
 c_mail VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE products (
 p_id SERIAL PRIMARY KEY,
 p_name VARCHAR(100) NOT NULL,
 price NUMERIC(12,2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE orders (
 o_id SERIAL PRIMARY KEY,
 c_id INT NOT NULL REFERENCES customers(c_id),
 o_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE order_items (
 o_id INT NOT NULL REFERENCES orders(o_id) ON DELETE CASCADE,
 p_id INT NOT NULL REFERENCES products(p_id),
 quantity INT NOT NULL CHECK (quantity > 0),
 PRIMARY KEY (o_id,p_id)
);

CREATE TABLE departments (
 dept_id SERIAL PRIMARY KEY,
 dept_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE employees (
 emp_id SERIAL PRIMARY KEY,
 fname VARCHAR(50) NOT NULL,
 lname VARCHAR(50) NOT NULL,
 email VARCHAR(150) UNIQUE NOT NULL,
 dept department NOT NULL,
 salary NUMERIC(12,2) NOT NULL CHECK (salary >= 0)
);