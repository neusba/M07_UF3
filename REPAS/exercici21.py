# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista. Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.
# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:

numeros = input("Introduce 10 números separados por espacios: ")
listaNumeros = list(numeros.split(" "))

print("Números: ", listaNumeros)

suma = 0
for i in listaNumeros:
    suma += int(i)

print("Suma total:", suma)
print("Mediana:", suma/len(listaNumeros))
