import random
import math


class Singe:
    def __init__(self, prenom):
        self.prenom = prenom

    def mange(self):
        if self.prenom == "Pierre":
            result = self.prenom + ' mange une banane jaune'
        elif self.prenom == "Marie":
            result = self.prenom + ' mange une banane verte'
        else:
            result = 'Autre banane'

        return result


prenoms = ["Pierre", "Marie"]

for val in prenoms:
    myClass = Singe(val)
    print(myClass.mange())
