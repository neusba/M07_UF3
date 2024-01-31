# Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.

# Orden ascendente de la tupla

numeros = input('Introduce 10 números separados por un espacio cada uno: ')
numerosArray = numeros.split(' ')
numerosArray.sort()
tupla = ()

for i in numerosArray:
    tupla = tupla + (int(i),)

print(tupla)


