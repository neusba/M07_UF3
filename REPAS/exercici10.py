# Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100. Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran fins que encerti i el missatge haurà d’indicar que ha encertat. Indicar també el número d’intents.
import random

misterioso = random.randint(1, 100)
numero = int(input('Introduce un número: '))

while numero != misterioso:
    numero = int(input('Introduce un número: '))

print('Has acertado! El número era el', misterioso)