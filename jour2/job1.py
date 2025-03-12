import mysql.connector

# Connexion à la base de données
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",  # Localhost (MySQL tourne sur 127.0.0.1:3306)
        user="root",  # nom d'utilisateur  "root"
        password="mot de passe*",  # mot de passe MySQL
        database="LaPlateforme"  # Nom de la base de données
    )

    if conn.is_connected():
        print(" Connexion réussie à la base de données 'LaPlateforme' !")

        # Création d'un curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()

        # Récupérer la liste des tables
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        print(" Tables disponibles dans 'LaPlateforme' :")
        for table in tables:
            print("-", table[0])

        # Fermer le curseur et la connexion
        cursor.close()
        conn.close()
        print(" Connexion fermée.")

except mysql.connector.Error as err:
    print(f" Erreur : {err}")
