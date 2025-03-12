-- inserer un étudiant da la table etudiants
INSERT INTO etudiant (nom, prenom, age, email)
VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');
-- récupperer les membres de la meme famille 
SELECT * FROM etudiant WHERE nom = 'Dupuis';
-- --  affiche les membres avec le meme nom de famille Dupuis