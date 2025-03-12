import mysql.connector

class Employe:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Papito1989*",
            database="entreprise"
        )
        self.cursor = self.conn.cursor()

    #  Ajouter un employé
    def ajouter_employe(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nom, prenom, salaire, id_service))
        self.conn.commit()
        print(f" Employé {prenom} {nom} ajouté avec succès.")

    #  Lire tous les employés
    def afficher_employes(self):
        self.cursor.execute("SELECT * FROM employe")
        for row in self.cursor.fetchall():
            print(row)

    #  Mettre à jour un employé
    def mettre_a_jour_employe(self, id, salaire):
        sql = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(sql, (salaire, id))
        self.conn.commit()
        print(f" Salaire de l'employé ID {id} mis à jour.")

    #  Supprimer un employé
    def supprimer_employe(self, id):
        sql = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        print(f" Employé ID {id} supprimé.")

    # 🔹 Fermer la connexion
    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()
        print(" Connexion fermée.")

#  Test de la classe
employe_manager = Employe()
employe_manager.ajouter_employe("Test", "User", 3200, 1)  # Ajout d'un employé
employe_manager.afficher_employes()  # Affichage des employés
employe_manager.mettre_a_jour_employe(1, 3700)  # Mise à jour d'un salaire
employe_manager.supprimer_employe(7)  # Suppression d'un employé
employe_manager.fermer_connexion()  # Fermeture de la connexion
