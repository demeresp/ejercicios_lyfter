-- Relationships
-- 1. Shopping Cart 1:N Cart Items
-- 2. Products 1:N Cart Items
-- 3. Invoices 1:N Products Per Invoice
-- 4. Products 1:N Products Per Invoice
-- 5. Products N:N Shopping Cart (through Cart Items)
-- 6. Products N:N Invoices (through Products Per Invoice)
-- Shopping Cart and Invoices are not related: the cart is temporary, the invoice is permanent.

CREATE TABLE `Products`(
    `Code` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(10,2) NOT NULL,
    `Entry Date` DATE NOT NULL,
    `Brand` VARCHAR(100) NOT NULL,
    `Stock Available` INT UNSIGNED NOT NULL
);

CREATE TABLE `Shopping Cart`(
    `Buyer Email` VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE `Cart Items`(
    `Buyer Email` VARCHAR(255) NOT NULL,
    `Product Code` BIGINT UNSIGNED NOT NULL,
    `Quantity` INT UNSIGNED NOT NULL,
    PRIMARY KEY(`Buyer Email`, `Product Code`),
    -- 1:N Shopping Cart -> Cart Items
    FOREIGN KEY(`Buyer Email`) REFERENCES `Shopping Cart`(`Buyer Email`),
    -- 1:N Products -> Cart Items
    FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`)
);

CREATE TABLE `Invoices`(
    `Invoice Number` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase Date` DATE NOT NULL,
    `Buyer Email` VARCHAR(255) NOT NULL,
    `Total Amount` DECIMAL(10,2) NOT NULL
);

CREATE TABLE `Products Per Invoice`(
    `Invoice Number` BIGINT UNSIGNED NOT NULL,
    `Product Code` BIGINT UNSIGNED NOT NULL,
    `Quantity` INT UNSIGNED NOT NULL,
    `Total Amount` DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(`Invoice Number`, `Product Code`),
    -- 1:N Invoices -> Products Per Invoice
    FOREIGN KEY(`Invoice Number`) REFERENCES `Invoices`(`Invoice Number`),
    -- 1:N Products -> Products Per Invoice
    FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`)
);
