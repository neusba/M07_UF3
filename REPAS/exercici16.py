# Demanar a l’usuari una frase. El programa eliminarà els espais i s'afegirà a una tupla. Mostrar per pantalla el contingut de la tupla.

frase = input('Escribe una frase: ')
fraseUnida = frase.split(' ')
tupla = ()

for i in fraseUnida:
    tupla = tupla + (i,)

print(tupla)