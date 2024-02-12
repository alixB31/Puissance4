import Objets  # Importe le module Objets
import random

# Fonction pour que l'IA joue de manière aléatoire
def jouer_IA_aleatoire(grille, symbole):
    while True:
        choix_IA = random.randint(1, 7)  # Choix aléatoire de la colonne
        colonne = choix_IA - 1  # Convertir en indice de colonne (0-indexed)
        numLigne = 0
        while not grille.getCaseSpecifique(numLigne, colonne).getEstVide() and numLigne < 5:
            numLigne += 1
            if numLigne == 5:
                continue  # La colonne est remplie, essayer une autre colonne
        case = grille.getCaseSpecifique(numLigne, colonne)
        case.setEstVideFalse()
        case.setCouleurCase(symbole)
        break

# Permet de lancer la partie
if __name__ == "__main__":

    # Création de l'objet grille
    grille = Objets.Grille()


    # Demande le nom du joueur
    nomUtilisateur = input("Veuillez saisir votre nom : ")
    symboleJoueur = "O"
    # Création du joueur et association d'une couleur
    joueur = Objets.Joueur(nomUtilisateur,symboleJoueur)
    print("\n Le symbole " + symboleJoueur + " vous a été assigné")

    # Insertions des objets cases dans la grille
    grille.insertion()

    quitter = False  # Initialisez une variable pour suivre si le joueur veut quitter


    while not quitter:
        # Affichage de la grille
        grille.afficher_grille()
        
        choix = input("Veuillez choisir l'endroit où vous voulez jouer, ou taper 'q' pour quitter : ")

        if choix.lower() == 'q':
            quitter = True 
        else:
            while not choix.isdigit() or int(choix) < 1 or int(choix) > 7:
                if not choix.isdigit():
                    print("L'entrée n'est pas un entier.")
                    choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")
                elif int(choix) < 1 or int(choix) > 7:
                    print("L'entier n'est pas entre 1 et 7.")
                    choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")
        if not quitter:
            choix = int(choix)  # Convertir choix en entier après la boucle pour une utilisation ultérieure
            choix -= 1 #-1 car les tableaux vont de 0 à 6 en python
            numLigne = 0
            while not grille.getCaseSpecifique(numLigne,choix).getEstVide() and numLigne < 5:
                numLigne += 1
                if numLigne == 5:
                    print ("La colonne est remplie, jouez autre part")
            case = grille.getCaseSpecifique(numLigne,choix)
            case.setEstVideFalse()  
            case.setCouleurCase(symboleJoueur)

            # Si le jeu n'est pas terminé et ce n'est pas le tour de l'IA
            if not quitter and symboleJoueur != "X":
                jouer_IA_aleatoire(grille, "X")  # L'IA joue avec le symbole "X"
                # Affichage de la grille après le coup de l'IA
                grille.afficher_grille() 
                # Vérifier si la grille est pleine après le coup du joueur
                if grille.grille_pleine():
                    print("La grille est pleine. La partie est terminée.")
                    break
                    
            # Vérifier si la grille est pleine après le coup de l'IA
            if grille.grille_pleine():
                print("La grille est pleine. La partie est terminée.")
                break 




    def evaluation_etat_jeu(grille):
        # Vérifier s'il y a un gagnant
        gagnant = rechercher_gagnant(grille)
        if gagnant:
            return gagnant


    def rechercher_gagnant(grille):
        for ligne in range(grille.getNbLignes()):
            for colonne in range(grille.getNbColonnes()):
                couleur = grille.getCaseSpecifique(ligne, colonne).getCouleurCase()
                if couleur != "":  # Si la case n'est pas vide
                    # Vérifier l'horizontal
                    if colonne <= grille.getNbColonnes() - 4:
                        if grille.getCaseSpecifique(ligne, colonne + 1).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne, colonne + 2).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne, colonne + 3).getCouleurCase() == couleur:
                            return couleur
                    # Vérifier la verticale
                    if ligne <= grille.getNbLignes() - 4:
                        if grille.getCaseSpecifique(ligne + 1, colonne).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne + 2, colonne).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne + 3, colonne).getCouleurCase() == couleur:
                            return couleur
                    # Vérifier la diagonale (/)
                    if colonne <= grille.getNbColonnes() - 4 and ligne >= 3:
                        if grille.getCaseSpecifique(ligne - 1, colonne + 1).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne - 2, colonne + 2).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne - 3, colonne + 3).getCouleurCase() == couleur:
                            return couleur
                    # Vérifier la diagonale (\)
                    if colonne >= 3 and ligne >= 3:
                        if grille.getCaseSpecifique(ligne - 1, colonne - 1).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne - 2, colonne - 2).getCouleurCase() == couleur and \
                                grille.getCaseSpecifique(ligne - 3, colonne - 3).getCouleurCase() == couleur:
                            return couleur
        return None  # Aucun gagnant trouvé