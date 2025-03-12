-- Création de la base de données
CREATE DATABASE zoo;
USE zoo;

-- Création de la table "cage"
CREATE TABLE cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie DECIMAL(10,2) NOT NULL,
    capacite_max INT NOT NULL
);

-- Création de la table "animal"
CREATE TABLE animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    race VARCHAR(255) NOT NULL,
    id_cage INT,
    date_naissance DATE NOT NULL,
    pays_origine VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_cage) REFERENCES cage(id) ON DELETE SET NULL
);
