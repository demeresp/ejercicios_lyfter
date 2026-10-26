-- SQLite

DELETE FROM Products
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Products
    GROUP BY name
);

DELETE FROM Products;