-- récuperer la liste des étudiants de moins de 18 ans
USE LaPlateforme;  -- utilisation de la base de données LaPlateforme
SELECT * FROM etudiants WHERE age < 18;
--  affiche les étudiants de moins de 18 ans