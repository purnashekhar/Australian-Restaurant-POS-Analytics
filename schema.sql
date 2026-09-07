-- Schema Definition for Australian Restaurant POS Analytics

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE menu_items (
    item_id VARCHAR(10) PRIMARY KEY,
    item_name VARCHAR(100),
    category VARCHAR(50),
    cost_price_aud DECIMAL(10,2),
    selling_price_aud DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    order_timestamp TIMESTAMP,
    order_type VARCHAR(20),
    payment_method VARCHAR(20),
    table_number INT NULL
);

CREATE TABLE order_details (
    order_detail_id SERIAL PRIMARY KEY,
    order_id VARCHAR(20) REFERENCES orders(order_id),
    item_id VARCHAR(10) REFERENCES menu_items(item_id),
    quantity INT,
    subtotal_aud DECIMAL(10,2),
    gross_profit_aud DECIMAL(10,2)
);