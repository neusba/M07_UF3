# Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i mostrar per pantalla quantes vegades apareix cada lletra.

palabras = input('Introduce dos palabras: ')
tupla = ()
letras = []

while True:
    if (len(palabras.split(' ')) != 2):
        palabras = input('Dos palabras!: ')

    break

for i in palabras:
    if not(i.isspace()):
        letras.append(i)
        if (tupla.count(i) == 0):
            tupla = tupla + (i,)

for x in tupla:
    print('La letra', x, 'aparece', letras.count(x), 'veces')
    