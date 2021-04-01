import random

def sortearNumeros(lista):
    for i in range(1, 7):
        y = 0

        while y == 0:
            x = random.randint(1, 60)
            if x in lista:
                y = 0
            else:
                y = 1
        lista.append(x)
    return lista


def ordenar(lista):
    n = len(lista)

    for i in range(0, n):
        index_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

print("NUMEROS DA MEGA SENA: ")
numeros = []
sortearNumeros(numeros)
print(numeros)

ordenar(numeros)
print('\n',numeros, '\n')
