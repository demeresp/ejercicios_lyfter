-- SQLite --AlTER changes structures of the tables

ALTER TABLE `Invoices`
    ADD `buyer_phone_number` VARCHAR(20) DEFAULT NULL;

ALTER TABLE `Invoices`
    ADD `employee_id` VARCHAR(255) DEFAULT NULL;

ALTER TABLE `Products`
    ADD `category_id` INTEGER DEFAULT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS idx_products_name ON Products(name);