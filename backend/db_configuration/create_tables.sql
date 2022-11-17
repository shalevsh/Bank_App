CREATE DATABASE IF NOT EXISTS bank_app;

USE bank_app;

-- CREATE TABLE IF NOT EXISTS bank_transaction(
--     id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     amount INT UNSIGNED NOT NULL,
--     is_deposit BOOLEAN NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS category( 
--     id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     category VARCHAR(50) NOT NULL,
--     vendor VARCHAR(50) NOT NULL
-- );

CREATE TABLE IF NOT EXISTS transaction_category(
    transaction_id INT UNSIGNED NOT NULL ,
    category_id INT UNSIGNED  NOT NULL ,
    PRIMARY KEY (transaction_id,category_id),
    FOREIGN KEY (transaction_id) REFERENCES bank_transaction(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

-- drop table transaction_category;

-- drop table bank_transaction;
-- drop table category;

SELECT Category.category,Bank_Transaction.is_deposit, SUM(Bank_Transaction.amount)
FROM Bank_Transaction 
JOIN Transaction_Category 
ON Bank_Transaction.id = Transaction_Category.transaction_id 
JOIN Category 
ON Category.id = Transaction_Category.category_id 
WHERE Bank_Transaction.is_deposit = '1' ;
GROUP BY Category.category;

