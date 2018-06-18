def addition(n):
    somme = 0
    for i in range(1, n + 1):
        somme = somme + i
    print(somme)


def fibonnaci(N):
    n2 = 0
    n1 = 1
    for i in range(1, N+1):
        V = n1 + n2
        n2 = n1
        n1 = V
        print(V)


def inArray(table, var):
    isInArray = False
    for i in table:
        if i == var:
            isInArray = True
            print('La variable', var, 'est dans le tableau')

    if isInArray == False:
        print('La variable', var, "n'est pas dans le tableau")

def returnIndice(array, var):
    k = 0
    indice = list()
    for i in array:
        if i == var:
            indice.append(k)
        k += 1
    print(indice)


returnIndice([1, 8, 3, 4, 8], 8)
# inArray([1, 2, 3, 4, 8], 5)
# inArray([1, 2, 3, 4, 8], 2)

# input = int(input("Donnez un entier : "))
# addition(input)

# N = int(input("Entrer le maximum de la suite : "))
# fibonnaci(N)