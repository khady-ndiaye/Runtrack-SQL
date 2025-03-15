CREATE DATABASE store;

USE store;

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price INT,
    quantity INT,
    id_category INT,
    FOREIGN KEY (id_category) REFERENCES category(id) ON DELETE CASCADE
);

-- Insertion des catégories
INSERT INTO category (name) VALUES ('Electronics'), ('Clothing'), ('Food');

-- Insertion des produits
INSERT INTO product (name, description, price, quantity, id_category) 
VALUES ('Smartphone', 'A high-end smartphone', 699, 50, 1),
       ('T-shirt', 'Cotton T-shirt', 20, 100, 2),
       ('Apple', 'Fresh apple', 2, 200, 3);
