CREATE DATABASE IF NOT EXISTS bank_app;

USE bank_app;

-- CREATE TABLE IF NOT EXISTS bank_transaction(
--     id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     amount INT UNSIGNED NOT NULL,
--     is_depoist BOOLEAN NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS category( 
--     id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     category VARCHAR(50) NOT NULL,
--     vendor VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS transaction_category(
--     transaction_id INT UNSIGNED NOT NULL ,
--     category_id INT UNSIGNED  NOT NULL ,
--     PRIMARY KEY (transaction_id,category_id),
--     FOREIGN KEY (transaction_id) REFERENCES bank_transaction(id),
--     FOREIGN KEY (category_id) REFERENCES category(id)
-- );

-- -- drop table transaction_category;

-- -- drop table bank_transaction;
-- -- drop table category;

-- SELECT Bank_Transaction.id, Bank_Transaction.amount, Category.id, Category.vendor, Category.category
-- FROM Bank_Transaction JOIN Transaction_Category 
-- ON Bank_Transaction.id = Transaction_Category.transaction_id 
-- JOIN Category
-- ON Category.id = Transaction_Category.category_id;

DELETE FROM Bank_Transaction WHERE id= 1;
