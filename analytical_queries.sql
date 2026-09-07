-- Query 1: Peak Hourly Rush Windows (Staff Optimization)
SELECT 
    EXTRACT(HOUR FROM order_timestamp) AS hour_of_day,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(subtotal_aud) AS total_revenue_aud
FROM order_details od
JOIN orders o ON od.order_id = o.order_id
GROUP BY hour_of_day
ORDER BY total_orders DESC;

-- Query 2: Menu Profitability Matrix (Identification of Low-Margin Drivers)
SELECT 
    m.item_name,
    m.category,
    SUM(od.quantity) AS total_units_sold,
    SUM(od.subtotal_aud) AS total_revenue_aud,
    SUM(od.gross_profit_aud) AS total_profit_aud,
    ROUND((SUM(od.gross_profit_aud) / NULLIF(SUM(od.subtotal_aud), 0)) * 100, 2) AS gross_margin_pct
FROM order_details od
JOIN menu_items m ON od.item_id = m.item_id
GROUP BY m.item_name, m.category
ORDER BY total_profit_aud DESC;

-- Query 3: Revenue & Volume Breakdown by Sales Channel
SELECT 
    o.order_type AS channel,
    COUNT(DISTINCT o.order_id) AS order_count,
    SUM(od.subtotal_aud) AS total_revenue_aud,
    ROUND(AVG(od.subtotal_aud), 2) AS avg_order_value_aud
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
GROUP BY o.order_type
ORDER BY total_revenue_aud DESC;