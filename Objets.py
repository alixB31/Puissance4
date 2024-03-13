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
        compteurLigne = 6
        # Crée le bord supérieur de la grille
        print("\n+" + "--" * 13 + "-+")
        for ligne in grille:
            compteurLigne -= 1
            compteurColonne = -1
            # Crée le début de chaque ligne avec une barre verticale
            print("|", end="")
            for _ in ligne:
                compteurColonne += 1 
                caseActuelle = self.getCaseSpecifique(compteurLigne, compteurColonne)
                if caseActuelle.getEstVide():
                    print("   |", end='')
                else:
                    print(f" {caseActuelle.getCouleurCase()} |", end='')
            print("\n+" + "---+" * 7)
        # Affiche les indices des colonnes en bas de la grille
        print ("  1"+ "   2"+ "   3"+"   4"+"   5"+"   6"+"   7")
    
    # Méthode pour vérifier si la grille est pleine
    def grille_pleine(self):
        for ligne in self.grille:
            for case in ligne:
                if case.getEstVide():
                    return False  # S'il y a au moins une case vide, la grille n'est pas pleine
        return True  # Si aucune case vide n'est trouvée, la grille est pleine

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
    
    def setCouleurCase(self,couleur):
        self.couleurCase = couleur

    def setEstVideFalse(self):
        self.estVide = False
