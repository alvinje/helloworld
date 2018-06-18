import random
import math

class Singe:
    def __init__(self, prenom):
        self.prenom = prenom

    def mange(self, banane):
        if self.prenom == "Pierre":
            result = self.prenom + ' mange une banane ' + banane.couleur
        elif self.prenom == "Marie":
            result = self.prenom + ' mange une banane ' + banane.couleur
        else:
            result = 'Autre banane'

        print(result)

    def sereproduit(self, tchoin, enfant):
        enfantclass = Singe(enfant)
        print(self.prenom + " s'est reproduit avec " + tchoin.prenom + " et on appeler leur enfant " + enfant)
        return enfantclass


class Banane:
    def __init__(self, couleur):
        self.couleur = couleur


class Graph:

    def __init__(self):
        self.noeud = []
        self.arrete = []

    def ajouternoeud(self, noeud):
        self.noeud.append(noeud)
        print(noeud + " est ajoute ")

    def ajouterarete(self, noeud1, noeud2):
        self.arrete.append(noeud1 + ':' + noeud2)
        print("Arrete ajoutee entre " + noeud1 + " et " + noeud2)

    def existarrete(self, noeud1, noeud2):

        for i in self.arrete:
            if i == noeud1 + ':' + noeud2:
                return True
            return False


pierre = Singe("Pierre")
marie = Singe("Marie")

bananeVerte = Banane("verte")
bananeJaune = Banane("jaune")

pierre.mange(bananeJaune)
marie.mange(bananeVerte)

robert = pierre.sereproduit(marie, "robert")


myGraph = Graph()
myGraph.ajouternoeud('noeud1')
myGraph.ajouternoeud('noeud2')
myGraph.ajouterarete('noeud1', 'noeud2')
print(myGraph.existarrete('noeud1', 'noeud2'))

