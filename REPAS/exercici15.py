# El mateix que l’anterior exercici, però sense demanar un màxim de números. L’usuari indicarà quan ha acabat posant un 0.

numeros = []

while True:
    numero = int(input('Introduce un número: '))
    if (numero == 0):
        break
    numeros.append(numero)

numeros.sort()
tupla = ()


for i in numeros:
    tupla = tupla + (int(i),)

print(tupla)


