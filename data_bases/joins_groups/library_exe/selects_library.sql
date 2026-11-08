-- SQLite

SELECT 
    Books.name, --Columnas.filas
    Authors.name
FROM Books
LEFT JOIN Authors ON Books.author = Authors.id;

SELECT name
FROM Books
WHERE author IS NULL;

SELECT Authors.name
FROM Authors --tabla de la izq
LEFT JOIN Books ON Authors.id = Books.author
--tomar la tabla de la izq/ ON - pegar info de / donde el ID de authos sea author de books(caso especifico) 
WHERE Books.author IS NULL;

SELECT Books.name
FROM Books
INNER JOIN Rents ON Books.id = Rents.book_id;

SELECT Books.name
FROM Books
LEFT JOIN Rents ON Books.id = Rents.book_id
WHERE Rents.book_id IS NULL;

SELECT Customers.name
FROM Customers
LEFT JOIN Rents ON Customers.id = Rents.customer_id
WHERE Rents.customer_id IS NULL;

SELECT Books.id
FROM Books
INNER JOIN Rents ON Books.id = Rents.book_id
WHERE Rents.state = 'Overdue';





