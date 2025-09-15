CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC(10,2)
);

INSERT INTO users (name) VALUES ('Ram'), ('Naresh'), ('Jia');
INSERT INTO products (name, price) VALUES ('Laptop', 1200.50), ('Phone', 799.99);
