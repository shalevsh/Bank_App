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
    id_transaction INT NOT NULL ,
    id_category INT NOT NULL ,
    PRIMARY KEY (id_transaction,id_category),
    FOREIGN KEY (id_transaction) REFERENCES bank_transaction(id),
    FOREIGN KEY (id_category) REFERENCES category(id)
);

