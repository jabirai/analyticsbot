SELECT TOP 5 p.product_name, SUM(oi.quantity) AS total_units_sold 
FROM BikeStores.sales.order_items AS oi 
JOIN BikeStores.production.products AS p ON oi.product_id = p.product_id 
GROUP BY p.product_name 
ORDER BY total_units_sold DESC;