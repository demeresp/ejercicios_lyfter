-- SQLite
--all products in storage

Select * FROM Products;

--all products for more than 50000
Select * FROM Products
WHERE price > 50000;

--all buys from the same product_id

Select * FROM Products_Per_Invoice
WHERE product_id = 1;

--all buys from the same product group

Select product_id,
    SUM(quantity) as total_amount
    FROM Products_Per_Invoice
GROUP BY product_id;

--all invoices from the same buyer

Select * FROM Invoices
WHERE buyer_email = espinozaemer29@gmail.com;

--invoices ordered by the total amount in descending order
Select * FROM Invoices
ORDER BY total_amount DESC;

--invoices from one invoice per invoice number
Select * FROM Invoices
WHERE id = 3;