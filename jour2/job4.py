import mysql.connector

# Connexion à la base de données
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",  # (localhost)
        user="root",  
        password="Papito1989*",   # mot de passe
        database="LaPlateforme"  # Base de données
    )

    if conn.is_connected():
        print(" Connexion réussie à la base de données 'LaPlateforme' !")

        # Création du curseur pour exécuter la requête
        cursor = conn.cursor()

        # Exécution de la requête SQL
        cursor.execute("SELECT nom, capacite FROM salle;")

        # Récupération des résultats
        salles = cursor.fetchall()

        print("\n Liste des salles :")
        for salle in salles:
            print(f" {salle[0]} - Capacité : {salle[1]} personnes")

        # Fermeture du curseur et de la connexion
        cursor.close()
        conn.close()
        print("\n🔌 Connexion fermée.")

except mysql.connector.Error as err:
    print(f" Erreur : {err}")
