-- SQLite
ALTER TABLE `Invoices`
    ADD `buyer_phone_number` VARCHAR(20) NOT NULL DEFAULT '0';

ALTER TABLE `Invoices`
    ADD `employee_id` VARCHAR(255) NOT NULL DEFAULT '0';