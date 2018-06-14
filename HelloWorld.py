import random
import math


class PiMonteCarlo:
    def __init__(self, iteration):
        self.iteration = iteration

    def computePi(self):

        total = 0

        for i in range(1, self.iteration) :
            x = random.random()
            y = random.random()
            dist = math.sqrt(x * x + y * y)

            if dist <= 1:
                total = total + 1

        pi = total / self.iteration * 4

        return pi


myClass99 = PiMonteCarlo(99)
myClass999 = PiMonteCarlo(999)
pi99 = myClass99.computePi()
pi999 = myClass999.computePi()

print(pi99, pi999)