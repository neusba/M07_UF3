# Demanar a l’usuari que posi dues paraules. Al executar el programa, mostrarà per pantalla les dues paraules amb els dos primers caràcters de cada paraula intercanviats. Exemple: Quatre Camins passaria a Caatre Qumins.
palabra1 = input('Introduce una palabra: ')
palabra2 = input('Introduce otra palabra: ')

caracter1 = palabra1[0]
caracter2 = palabra2[0]

palabra1 = palabra1.replace(palabra1[0], caracter2)
palabra2 = palabra2.replace(palabra2[0], caracter1)

print(palabra1, palabra2)




