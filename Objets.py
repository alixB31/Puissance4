class Joueur:
    # Initalisation
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleurJoueur = couleur
        
class Grille:
    # Initalisation
    def __init__(self):
        self.hauteur = 6
        self.largeur = 7
        self.grille = []

class Case:
    # Initalisation
    def __init__(self):
        self.estVide = True
        self.couleurCase = ""

    # Getter
    @property
    def getEstVide(self):
        return self.__estVide

    # Getter
    @property
    def getCouleurCase(self):
        return self.__couleurCase

class Pion:
    # Initalisation
    def __init__(self, couleur):
        self.couleurPion = couleur # False = Croix ; True = Rond


