# Demanar a l’usuari un número. Indicar si el número inserit per l’usuari és parell o senar.
valor = int(input('Introduce un valor: '))

if valor % 2 == 0:
    print(valor, 'es un número par')
else:
    print(valor, 'es un número impar')
