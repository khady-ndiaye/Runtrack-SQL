-- mettre à jour l'age de l'étudiant Betty Spaghetti à 20 ans
UPDATE etudiants
SET age = 20
WHERE nom = 'Spaghetti' AND prenom = 'Betty' AND age = 23;

-- verifier que l'age de l'étudiant Betty Spaghetti est bien 20 ans
SELECT * FROM etudiants
WHERE nom = 'Spaghetti' AND prenom = 'Betty';
