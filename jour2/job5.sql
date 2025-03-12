--calcul la superficie totale de la plateforme
SELECT CONCAT('La superficie de La Plateforme est de ', SUM(superficie), ' m2') AS message 
FROM etage;
