-- compte le nombre d'étudiants de moins de 18 ans
SELECT COUNT(*) AS nombre_etudiants_mineurs 
FROM etudiants
WHERE age < 18;
