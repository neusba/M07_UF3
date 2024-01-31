# Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula de multiplicar fins el 10. Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30
numero = int(input('Introduce un número entre el 1 y el 10: '))

for i in range (11):
    print(numero * i)