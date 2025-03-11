USE LaPlateforme;
-- ajout d'une table etudiants
CREATE TABLE etudiants (
     id INT NOT NULL AUTO_INCREMENT,
     nom VARCHAR(255) NOT NULL,
     prenom VARCHAR(25) NOT NULL,
     age INT NOT NULL,
     email VARCHAR(255) NOT NULL,
     PRIMARY KEY (id)
    
);
-- verification de la création de la table
SHOW TABLES;

    