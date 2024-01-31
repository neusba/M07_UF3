# Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100. Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran fins que encerti i el missatge haurà d’indicar que ha encertat. Indicar també el número d’intents.
import random

intentos = 0
misterioso = random.randint(1, 100)
numero = int(input('Introduce un número entre el 1 y el 100: '))

while numero != misterioso:
    intentos += 1
    print('El número a adivinar es más pequeño') if numero > misterioso else print('El número a adivinar es más grande')
    numero = int(input('Introduce un número entre el 1 y el 100: '))

print('Has encertado!')
print('Intentos:', intentos, '\nEl número era', misterioso)