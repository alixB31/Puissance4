import Objets  # Importe le module Objets
import random

# Permet de lancer la partie
if __name__ == "__main__":

    # Création de l'objet grille
    grille = Objets.Grille()

    # Demande le nom du joueur
    nomUtilisateur = input("Veuillez saisir votre nom : ")
    symboleAleatoire = random.choice(["X", "O"])
    # Création du joueur et association d'une couleur
    joueur = Objets.Joueur(nomUtilisateur,symboleAleatoire)
    print("\n Les " + symboleAleatoire + " vous ont été assigné(e)s")

    # Insertions des objets cases dans la grille
    grille.insertion()

    # Affichage de la grille
    affichageGrille = grille.afficher_grille()

    choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")

    while not choix.isdigit() or int(choix) < 1 or int(choix) > 7:
        if not choix.isdigit():
            print("L'entrée n'est pas un entier.")
            choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")
        else:
            print("L'entier n'est pas entre 1 et 7.")
            choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")

    choix = int(choix)  # Convertir choix en entier après la boucle pour une utilisation ultérieure

    
    grille.setCaseSpecifique(choix,choix,"O")
    print (affichageGrille)
    print("Votre choix à bien été enregisté")        
    