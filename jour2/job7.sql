-- Création de la base de données
CREATE DATABASE entreprise;
USE entreprise;

-- Création de la table "service"
CREATE TABLE service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

-- Création de la table "employe"
CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    salaire DECIMAL(10,2) NOT NULL,
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES service(id) ON DELETE SET NULL
);
--insertion des données dans la table service
INSERT INTO service (nom) VALUES 
('Informatique'),
('Ressources Humaines'),
('Comptabilité'),
('Marketing');

--insertion des données dans la table employe
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Dupont', 'Jean', 3500.00, 1),
('Martin', 'Sophie', 2800.00, 2),
('Lemoine', 'Pierre', 4000.00, 1),
('Durand', 'Alice', 3200.00, 3),
('Bernard', 'Luc', 2900.00, 4),
('Moreau', 'Claire', 5000.00, 2);

--sélection des employés ayant un salaire supérieur à 3000
SELECT * FROM employe WHERE salaire > 3000;

--sélection des employés travaillant dans le service "Informatique"
SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service
FROM employe
LEFT JOIN service ON employe.id_service = service.id;
