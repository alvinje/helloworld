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


def inArray(val):
    table = [1, 2, 3, 4, 8]
    for i in table:
        if i == val:
            print('La variable', i, 'est dans le tableau')
    print('La variable', i, "n'est pas dans le tableau")


inArray(5)

# input = int(input("Donnez un entier : "))
# addition(input)

# N = int(input("Entrer le maximum de la suite : "))
# fibonnaci(N)