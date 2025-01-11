SELECT TOP 10 p.product_id, p.product_name, s.quantity FROM BikeStores.production.products p JOIN BikeStores.production.stocks s ON p.product_id = s.product_id WHERE s.quantity < 5;