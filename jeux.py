import Objets  # Importe le module Objets
import random

# Permet de lancer la partie
if __name__ == "__main__":

    # Création de l'objet grille
    grille = Objets.Grille()

    # Demande le nom du joueur
    nomUtilisateur = input("Veuillez saisir votre nom : ")
    nombreAleatoire = random.choice(["Croix", "Rond"])
    # Création du joueur et association d'une couleur
    joueur = Objets.Joueur(nomUtilisateur,nombreAleatoire)

    # Insertions des objets cases dans la grille
    grille.insertion()

    # Affichage de la grille
    affichageGrille = grille.afficher_grille()

    choix = input("Veuillez Choisir la ou vous voulez jouer : ")
    if not choix.isdigit():
        print("L'entrée n'est pas un entier.")
    else:
        print("Commence")