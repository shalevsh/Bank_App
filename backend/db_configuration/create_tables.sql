CREATE DATABASE IF NOT EXISTS bank_app;

USE bank_app;
CREATE TABLE IF NOT EXISTS bank_transaction(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    amount INT NOT NULL,
    is_depoist BOOLEAN NOT NULL
);
CREATE TABLE IF NOT EXISTS category( 
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    vendor VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS transaction_category(
    transaction_id INT NOT NULL ,
    category_id INT NOT NULL ,
    PRIMARY KEY (transaction_id,category_id),
    FOREIGN KEY (transaction_id) REFERENCES bank_transaction(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

