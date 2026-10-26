-- SQLite
--Update will make changes to the data in the tables(variables) but not to the structure of the tables
UPDATE Products
SET stock_available = 0
WHERE price <= 0;

UPDATE Products
SET price = price + 100
WHERE stock_available < 10;

UPDATE Products
SET stock_available = stock_available - 1
WHERE id = 1;
