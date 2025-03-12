import mysql.connector

class ZooManager:
    def __init__(self):
        """Connexion à la base de données"""
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="ton_mot_de_passe",
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def ajouter_cage(self, superficie, capacite_max):
        """Ajoute une nouvelle cage"""
        sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.cursor.execute(sql, (superficie, capacite_max))
        self.conn.commit()
        print(" Cage ajoutée avec succès.")

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        """Ajoute un nouvel animal"""
        sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (nom, race, id_cage, date_naissance, pays_origine))
        self.conn.commit()
        print(f"Animal {nom} ajouté avec succès.")

    def supprimer_animal(self, id_animal):
        """Supprime un animal"""
        sql = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(sql, (id_animal,))
        self.conn.commit()
        print(" Animal supprimé avec succès.")

    def modifier_animal(self, id_animal, nouveau_nom):
        """Modifie le nom d'un animal"""
        sql = "UPDATE animal SET nom = %s WHERE id = %s"
        self.cursor.execute(sql, (nouveau_nom, id_animal))
        self.conn.commit()
        print(" Nom de l'animal mis à jour.")

    def afficher_animaux(self):
        """Affiche tous les animaux du zoo"""
        self.cursor.execute("SELECT * FROM animal")
        animaux = self.cursor.fetchall()
        if not animaux:
            print(" Aucun animal trouvé.")
        else:
            for animal in animaux:
                print(animal)

    def afficher_animaux_par_cage(self):
        """Affiche les animaux présents dans chaque cage"""
        sql = """
        SELECT a.nom, a.race, c.id AS cage_id 
        FROM animal a
        LEFT JOIN cage c ON a.id_cage = c.id
        ORDER BY c.id;
        """
        self.cursor.execute(sql)
        animaux = self.cursor.fetchall()
        if not animaux:
            print(" Aucun animal trouvé.")
        else:
            for animal in animaux:
                print(f"Animal: {animal[0]}, Race: {animal[1]}, Cage: {animal[2]}")

    def calculer_superficie_totale(self):
        """Calcule et affiche la superficie totale des cages"""
        self.cursor.execute("SELECT SUM(superficie) FROM cage;")
        result = self.cursor.fetchone()
        superficie_totale = result[0] if result[0] else 0
        print(f" La superficie totale des cages est de {superficie_totale} m².")

    def fermer_connexion(self):
        """Ferme la connexion à la base de données"""
        self.cursor.close()
        self.conn.close()
        print("🔌 Connexion fermée.")

#  Interface utilisateur
def menu():
    zoo = ZooManager()
    
    while True:
        print("\n--- Gestion du Zoo ---")
        print("1. Ajouter une cage")
        print("2. Ajouter un animal")
        print("3. Supprimer un animal")
        print("4. Modifier un animal")
        print("5. Afficher tous les animaux")
        print("6. Afficher les animaux par cage")
        print("7. Calculer la superficie totale des cages")
        print("8. Quitter")

        choix = input(" Choisissez une option : ")

        if choix == "1":
            superficie = float(input("Superficie de la cage (m²) : "))
            capacite_max = int(input("Capacité max de la cage : "))
            zoo.ajouter_cage(superficie, capacite_max)
        
        elif choix == "2":
            nom = input("Nom de l'animal : ")
            race = input("Race de l'animal : ")
            id_cage = input("ID de la cage (laisser vide si pas de cage) : ")
            id_cage = int(id_cage) if id_cage else None
            date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
            pays_origine = input("Pays d'origine : ")
            zoo.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)

        elif choix == "3":
            id_animal = int(input("ID de l'animal à supprimer : "))
            zoo.supprimer_animal(id_animal)

        elif choix == "4":
            id_animal = int(input("ID de l'animal à modifier : "))
            nouveau_nom = input("Nouveau nom : ")
            zoo.modifier_animal(id_animal, nouveau_nom)

        elif choix == "5":
            zoo.afficher_animaux()

        elif choix == "6":
            zoo.afficher_animaux_par_cage()

        elif choix == "7":
            zoo.calculer_superficie_totale()

        elif choix == "8":
            zoo.fermer_connexion()
            break

        else:
            print(" Option invalide, veuillez réessayer.")

# Exécution du menu
menu()
