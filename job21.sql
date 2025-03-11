--compte le nombre d'étudiants de 18 à 25 ans
SELECT COUNT(*) AS nombre_etudiants_18_25 
FROM etudiants
WHERE age BETWEEN 18 AND 25;
