# Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.

# Orden ascendente de la tupla

numeros = []

while True:
    numero = int(input('Introduce un número: '))
    if (len(numeros) == 9):
        break
    numeros.append(numero)

numeros.sort()
tupla = ()


for i in numeros:
    tupla = tupla + (int(i),)

print(tupla)