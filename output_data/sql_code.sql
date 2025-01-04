SELECT p.product_name, s.quantity 
FROM BikeStores.production.products AS p 
JOIN BikeStores.production.stocks AS s ON p.product_id = s.product_id 
WHERE s.quantity <= 5;