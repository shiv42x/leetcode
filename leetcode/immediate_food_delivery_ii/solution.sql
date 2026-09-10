WITH sorted_orders AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS nth_delivery
    FROM
        delivery
),
first_order AS (
    SELECT
        delivery_id,
        customer_id,
        order_date,
        customer_pref_delivery_date
    FROM
        sorted_orders
    WHERE
        nth_delivery = 1
)
SELECT
    ROUND(SUM(CASE WHEN DATE(order_date) = DATE(customer_pref_delivery_date) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0) * 100, 2)AS immediate_percentage
FROM 
    first_order;