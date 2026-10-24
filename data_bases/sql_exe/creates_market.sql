-- SQLite
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    entry_date DATE NOT NULL,
    brand VARCHAR(100) NOT NULL,
    stock_available INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Shopping_Cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Cart_Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Shopping_Cart(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

CREATE TABLE IF NOT EXISTS Invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date DATE NOT NULL,
    buyer_email VARCHAR(255) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Products_Per_Invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES Invoices(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);