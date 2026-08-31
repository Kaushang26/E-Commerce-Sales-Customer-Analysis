use project;

SELECT *
FROM customers
WHERE customer_id NOT IN (
  SELECT t.min_id
  FROM (
    SELECT MIN(customer_id) AS min_id
    FROM customers
    GROUP BY email
  ) AS t
);


UPDATE products
SET stock = 0
WHERE stock IS NULL
  AND product_id > 0;


UPDATE customers
SET contact = REPLACE(contact, '-', '')
WHERE contact LIKE '%-%'
  AND customer_id > 0;


UPDATE payments p
SET p.amount = (
    SELECT SUM(oi.price * oi.quantity)
    FROM order_items oi
    WHERE oi.order_id2 = p.order_id3
)
WHERE p.amount IS NULL
  AND p.payment_id > 0;



UPDATE payments
SET payment_date = CURDATE()
WHERE payment_date IS NULL
  AND payment_id > 0;



