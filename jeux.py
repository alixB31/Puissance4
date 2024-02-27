import Objets # Importe le module Objets
import random
import copy
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

def compter_lignes_autour(grille, ligne, colonne, symbole):
    count = 0
    for delta_colonne in range(-3, 1):
        if colonne + delta_colonne >= 0 and colonne + delta_colonne + 3 < grille.getNbColonnes():
            if grille.getCaseSpecifique(ligne, colonne + delta_colonne).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne, colonne + delta_colonne).getCouleurCase() == "" and \
               grille.getCaseSpecifique(ligne, colonne + delta_colonne + 1).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne, colonne + delta_colonne + 1).getCouleurCase() == "" and \
               grille.getCaseSpecifique(ligne, colonne + delta_colonne + 2).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne, colonne + delta_colonne + 2).getCouleurCase() == "" and \
               grille.getCaseSpecifique(ligne, colonne + delta_colonne + 3).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne, colonne + delta_colonne + 3).getCouleurCase() == "":
                count += 1
    return count

def compter_colonnes_autour(grille, ligne, colonne, symbole):
    count = 0
    for delta_ligne in range(-3, 1):
        if ligne + delta_ligne >= 0 and ligne + delta_ligne + 3 < grille.getNbLignes():
            if grille.getCaseSpecifique(ligne + delta_ligne, colonne).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta_ligne, colonne).getCouleurCase() == "" and \
               grille.getCaseSpecifique(ligne + delta_ligne + 1, colonne).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta_ligne + 1, colonne).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta_ligne + 2, colonne).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta_ligne + 2, colonne).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta_ligne + 3, colonne).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta_ligne + 3, colonne).getCouleurCase() =="":
                count += 1
    return count

def compter_diagonales_autour(grille, ligne, colonne, symbole):
    count = 0
    for delta in range(-3, 1):
        if colonne + delta >= 0 and colonne + delta + 3 < grille.getNbColonnes() \
                and ligne + delta >= 0 and ligne + delta + 3 < grille.getNbLignes():
            if grille.getCaseSpecifique(ligne + delta, colonne + delta).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta, colonne + delta).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta + 1, colonne + delta + 1).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta + 1, colonne + delta + 1).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta + 2, colonne + delta + 2).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta + 2, colonne + delta + 2).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta + 3, colonne + delta + 3).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta + 3, colonne + delta + 3).getCouleurCase() == "" :
                count += 1
    return count

def compter_diagonales_inverse_autour(grille, ligne, colonne, symbole):
    count = 0
    for delta in range(-3, 1):
        if colonne - delta >= 0 and colonne - delta + 3 < grille.getNbColonnes() \
                and ligne + delta >= 0 and ligne + delta + 3 < grille.getNbLignes():
            if grille.getCaseSpecifique(ligne + delta, colonne - delta).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta, colonne - delta).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta + 1, colonne - delta + 1).getCouleurCase() == symbole or  grille.getCaseSpecifique(ligne + delta + 1, colonne - delta + 1).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta + 2, colonne - delta + 2).getCouleurCase() == symbole or  grille.getCaseSpecifique(ligne + delta + 2, colonne - delta + 2).getCouleurCase() =="" and \
               grille.getCaseSpecifique(ligne + delta + 3, colonne - delta + 3).getCouleurCase() == symbole or grille.getCaseSpecifique(ligne + delta + 3, colonne - delta + 3).getCouleurCase() == "":
                count += 1
    return count

def compter_possibilites_autour(grille, ligne, colonne, symbole):
    # Initialisation du compteur de possibilités
    possibilites = 0
    # Recherche de puissance 4 horizontalement
    possibilites += compter_lignes_autour(grille, ligne, colonne, symbole)
    # Recherche de puissance 4 verticalement
    possibilites += compter_colonnes_autour(grille, ligne, colonne, symbole)
    # Recherche de puissance 4 en diagonale (/)
    possibilites += compter_diagonales_autour(grille, ligne, colonne, symbole)
    # Recherche de puissance 4 en diagonale (\)
    possibilites += compter_diagonales_inverse_autour(grille, ligne, colonne, symbole)
    return possibilites

    
# Fonction pour que l'IA joue de manière aléatoire
def evaluation(grille, symbole):
    meilleurCoup = 0
    valeurCoup = 0 
    grilleTest = copy.deepcopy(grille)
    for numeroCoupTeste in range(grille.getNbColonnes()):
        valeurCoupTeste = 0
        # On recupere la ligne ou on pourrais théoriquement jouer 
        numLigne = 0
        while not grilleTest.getCaseSpecifique(numLigne, numeroCoupTeste).getEstVide() and numLigne < 5:
            numLigne += 1
        if not grilleTest.getCaseSpecifique(5, numeroCoupTeste).getEstVide():
            continue
        else:
            case = grilleTest.getCaseSpecifique(numLigne, numeroCoupTeste)
            # Regarde si l'adversaire peut gagner en jouant la 
            case.setCouleurCase("O")
            if rechercher_gagnant(grilleTest) == "O":
                valeurCoupTeste +=900
            # Regarde si l'ia peut gagner en jouant la 
            case.setCouleurCase(symbole)
            if rechercher_gagnant(grilleTest) == symbole:  # Si le coup permet à l'IA de gagner
                valeurCoupTeste +=1000
            # Reset la case
            case.setCouleurCase("")
            valeurCoupTeste += compter_possibilites_autour(grilleTest,numLigne,numeroCoupTeste, symbole)
            print ("valeur actuelle")
            print(valeurCoupTeste)
            if valeurCoupTeste > valeurCoup :
                valeurCoup = valeurCoupTeste
                meilleurCoup = numeroCoupTeste
    
    return meilleurCoup

# Fonction pour que l'IA joue de manière aléatoire
def jouer_IA(grille, symbole):
    while True:
        choix_IA = evaluation(grille, symbole)  # Choix aléatoire de la colonne
        colonne = choix_IA  
        numLigne = 0
        while not grille.getCaseSpecifique(numLigne, colonne).getEstVide() and numLigne < 5:
            numLigne += 1
            if numLigne == 5:
                continue  # La colonne est remplie, essayer une autre colonne
        case = grille.getCaseSpecifique(numLigne, colonne)
        case.setEstVideFalse()
        case.setCouleurCase(symbole)
        break



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
    return False  # Aucun gagnant trouvé

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

     # Affichage de la grille
    grille.afficher_grille()
    while not quitter:
        
        choix = input("Veuillez choisir l'endroit où vous voulez jouer, ou tapez 'q' pour quitter : ")
        if choix.lower() == 'q':
            quitter = True 
        else:
            while not choix.isdigit() or int(choix) < 1 or int(choix) > 7 or not grille.getCaseSpecifique(5,int(choix)-1).getEstVide():
                if not choix.isdigit():
                    print("L'entrée n'est pas un entier.")
                    choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")
                elif int(choix) < 1 or int(choix) > 7:
                    print("L'entier n'est pas entre 1 et 7.")
                    choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")
                elif not grille.getCaseSpecifique(5,int(choix)-1).getEstVide():
                    print ("La colonne est remplie, jouez autre part")
                    choix = input("Veuillez choisir l'endroit où vous voulez jouer : ")
        if not quitter:
            choix = int(choix)  # Convertir choix en entier après la boucle pour une utilisation ultérieure
            choix -= 1 #-1 car les tableaux vont de 0 à 6 en python
            numLigne = 0
            while not grille.getCaseSpecifique(numLigne,choix).getEstVide() and numLigne < 5:
                numLigne += 1
                
            case = grille.getCaseSpecifique(numLigne,choix)
            case.setEstVideFalse()  
            case.setCouleurCase(symboleJoueur)
        
            # Si le jeu n'est pas terminé et ce n'est pas le tour de l'IA
            if not quitter and symboleJoueur != "X":
                jouer_IA(grille, "X")  # L'IA joue avec le symbole "X"
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
        if rechercher_gagnant(grille) != False :
            print(rechercher_gagnant(grille) + " a gagné")
            quitter = True
