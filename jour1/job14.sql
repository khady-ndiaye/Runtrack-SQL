--récuperer la liste des étudiants dont l'age est compris entre 18 et 25 ans et les afficher par ordre croissant d'âge
SELECT * FROM etudiants
WHERE age BETWEEN 18 AND 25
ORDER BY age ASC;