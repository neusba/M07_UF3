# Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es indicada/es per l’usuari, indicar quants caràcters té i indicar el primer, i l’últim caràcter.
palabras = input('Introduce entre 1 y 3 palabras: ')
arrayPalabras = palabras.split(' ')

if len(arrayPalabras) == 0 or len(arrayPalabras) > 3:
    print('Cantidad de palabras inválida')
else:
    for i in arrayPalabras:
        print(f"La palabra {i} tiene {len(i)} carácteres. El primer carácter es {i[0].upper()} y el último es {i[len(i)-1].upper()}")
    
