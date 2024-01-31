# Demanar a l’usuari un nùmero entre 1 i 100.
# Posar els números a una tupla desde 1 fins al número indicat per l’usuari.
# Exemple: usuari indica 34
# Es crea una tupla i es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).

numero = int(input('Introduce un número entre el 1 y el 100: '))
tupla = ()

for i in range(numero + 1):
    tupla = tupla + (i,)

print(tupla)



