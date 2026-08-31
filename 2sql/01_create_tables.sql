use project;
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) not null,
    email VARCHAR(100) not null,
    gender ENUM('Male', 'Female', 'Other'),
    contact VARCHAR(100),
    relation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)not null,
    category VARCHAR(100) not null,
    price INT,
    stock INT
);
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id2 INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_completed TINYINT(1) DEFAULT 0,
    FOREIGN KEY (customer_id2) REFERENCES customers(customer_id)
);
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id2 INT,
    product_id2 INT,
    quantity INT,
    price INT,
    FOREIGN KEY (order_id2) REFERENCES orders(order_id),
    FOREIGN KEY (product_id2) REFERENCES products(product_id)
);
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id3 INT,
    amount INT,
    payment_date DATE,
    payment_method ENUM('Cash', 'Card', 'Online'),
    FOREIGN KEY (order_id3) REFERENCES orders(order_id)
);
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id3 INT,
    product_id3 INT,
    rating ENUM('1','2','3','4','5'),
    comment VARCHAR(200),
    FOREIGN KEY (customer_id3) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id3) REFERENCES products(product_id)
);




