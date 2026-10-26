-- SQLite
INSERT OR IGNORE INTO Category (name) VALUES ('FOOD');
INSERT OR IGNORE INTO Category (name) VALUES ('SPORTS');
INSERT OR IGNORE INTO Category (name) VALUES ('MUSIC');

INSERT OR IGNORE INTO `Invoices` (purchase_date, buyer_email, total_amount, buyer_phone_number, employee_id)
    VALUES ('2026-10-20', 'vanessa@gmail.com', 45000, '8624-7375', 'EMP-001');

INSERT OR IGNORE INTO `Invoices` (purchase_date, buyer_email, total_amount, buyer_phone_number, employee_id)
    VALUES('2026-12-20', 'espinozaemer29@gmail.com', 3000, '8740-4545', 'EMP-002');

INSERT OR IGNORE INTO `Invoices` (purchase_date, buyer_email, total_amount, buyer_phone_number, employee_id)
    VALUES('2026-12-21', 'jegg@gmail.com', 20000, '8500-3560', 'EMP-003');

INSERT INTO Products_Per_Invoice(invoice_id, product_id, quantity, total_amount)
    VALUES(1, 1, 3, 75);

INSERT INTO Products_Per_Invoice(invoice_id, product_id, quantity, total_amount)
    VALUES(2, 4, 4, 10000);

INSERT INTO Products_Per_Invoice(invoice_id, product_id, quantity, total_amount)
    VALUES(3, 5, 2, 100000);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('PASTA', 15, '2026-10-24', 'ROMA', 51, 1);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('FOOTBALL BALL', 20000, '2025-12-23', 'UMBRO', 20, 2);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('GUITAR', 300000, '2023-09-10', 'YAMAHA', 100, 3);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('BASKETBALL BALL', 2500, '2024-11-15', 'NIKE', 30, 4);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('DRUM SET', 50000, '2025-01-05', 'PEARL', 10, 5);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('TENNIS RACKET', 150000, '2024-08-20', 'HEAD', 15, 6);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('VIOLIN', 400000, '2023-07-12', 'STRADIVARIUS', 5, 7);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('BOWLING BALL', 800, '2025-03-18', 'STORM', 25, 8);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('SAXOPHONE', 600000, '2024-05-30', 'YAMAHA', 8, 9);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('BASKETBALL SHOES', 120000, '2023-11-22', 'ADIDAS', 40, 10);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('TRUMPET', 350000, '2025-02-14', 'BACH', 12, 11);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('SOCCER JERSEY', 900, '2024-09-05', 'NIKE', 60, 12);

INSERT OR IGNORE INTO Products (name, price, entry_date, brand, stock_available, category_id)
VALUES ('FLUTE', 250000, '2023-10-28', 'YAMAHA', 18, 13);

