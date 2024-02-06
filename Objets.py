class Joueur:
    # Initalisation
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleurJoueur = couleur
        
class Grille:
    # Initalisation
    def __init__(self):
        self.nbLignes = 6
        self.nbColonnes = 7
        self.grille = []

    # Getter
    def getNbColonnes(self):
        return self.nbColonnes

    # Getter
    def getNbLignes(self):
        return self.nbLignes
    
    # Getter
    def getGrille(self):
        return self.grille
    
    def insertion(self):
        nLigne = 0
        nColonne = 0
        for _ in range(self.nbLignes):
            nLigne = nLigne + 1 
            
            ligne = []
            for _ in range(self.nbColonnes):
                nColonne = nColonne + 1
                # Création et ajout d'un objet Case à la ligne
                ligne.append(Case(nLigne,nColonne)) 
            # Ajout de la ligne à la grille
            self.grille.append(ligne) 
            nColonne = 0

    # Accéder à une case spécifique dans la grille
    def getCaseSpecifique(self, ligne, colonne):
        if 0 <= ligne < self.nbLignes and 0 <= colonne < self.nbColonnes:
            return self.grille[ligne][colonne]
        else:
            return None
        
    # Affichage de la grille
    def afficher_grille(self):
        grille = [[' ' for _ in range(self.nbColonnes)] for _ in range(self.nbLignes)]
        # Crée le bord supérieur de la grille
        print("\n+" + "--" * 13 + "-+")
        for ligne in grille:
            # Crée le début de chaque ligne avec une barre verticale
            print("|", end="")
            for _ in ligne:
                print("   |", end='')
            print("\n+" + "---+" * 7)
        # Affiche les indices des colonnes en bas de la grille
        print ("  1"+ "   2"+ "   3"+"   4"+"   5"+"   6"+"   7")

    
class Case:
    # Initalisation
    def __init__(self,ligne,colonne):
        self.ligne = ligne
        self.colonne = colonne
        self.estVide = True
        self.couleurCase = ""

    # Getter
    def getColonne(self):
        return self.colonne
    
    # Getter
    def getLigne(self):
        return self.ligne
    
    # Getter
    def getEstVide(self):
        return self.estVide

    # Getter
    def getCouleurCase(self):
        return self.couleurCase

class Pion:
    # Initalisation
    def __init__(self, couleur):
        self.couleurPion = couleur # False = Croix ; True = Rond


