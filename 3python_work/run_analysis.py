from utils import run_query

queries = {
    "top_products": """
        SELECT p.name, SUM(oi.quantity) AS total_sold
        FROM order_items oi
        JOIN products p ON oi.product_id2 = p.product_id
        GROUP BY p.product_id
        ORDER BY total_sold DESC
        LIMIT 5;
    """,
    "revenue_by_customer": """
        SELECT c.name, SUM(pay.amount) AS total_spent
        FROM payments pay
        JOIN orders o ON pay.order_id3 = o.order_id
        JOIN customers c ON o.customer_id2 = c.customer_id
        GROUP BY c.customer_id
        ORDER BY total_spent DESC;
    """,
    "monthly_revenue": """
        SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month, SUM(pay.amount) AS revenue
        FROM payments pay
        JOIN orders o ON pay.order_id3 = o.order_id
        GROUP BY DATE_FORMAT(o.order_date, '%Y-%m')
        ORDER BY month;
    """,
    "repeat_buyers": """
        SELECT c.name, COUNT(o.order_id) AS total_orders
        FROM orders o
        JOIN customers c ON o.customer_id2 = c.customer_id
        GROUP BY c.customer_id
        HAVING total_orders > 1;
    """,
    "inactive_customers": """
        SELECT c.name
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id2
        WHERE o.order_date IS NULL 
           OR o.order_date < NOW() - INTERVAL 6 MONTH;
    """,
    "average_order_value": """
        SELECT AVG(amount) AS avg_order_value
        FROM payments;
    """,
    "declining_sales": """
        SELECT p.name, DATE_FORMAT(o.order_date, '%Y-%m') AS month, SUM(oi.quantity) AS total_sold
        FROM order_items oi
        JOIN orders o ON oi.order_id2 = o.order_id
        JOIN products p ON oi.product_id2 = p.product_id
        GROUP BY p.product_id, DATE_FORMAT(o.order_date, '%Y-%m')
        ORDER BY p.name, month;
    """,
    "payment_distribution": """
        SELECT payment_method, COUNT(*) AS total_transactions, SUM(amount) AS total_amount
        FROM payments
        GROUP BY payment_method;
    """
}

for name, q in queries.items():
    df = run_query(q, name)
    print(f"{name}:\n", df.head(), "\n")
