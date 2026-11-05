-- SQLite

SELECT 
    Books.name,
    Authors.name
FROM Books
LEFT JOIN Authors ON Books.author = Authors.id;


SELECT name
FROM Books
WHERE author IS NULL;


SELECT author
FROM Books
WHERE id iS NULL;


SELECT BookID
FROM Rents
WHERE state IS NOT NULL;

SELECT CustomerID
FROM Rents
WHERE State iS NULL; ??




