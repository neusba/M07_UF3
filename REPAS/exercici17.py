# Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits i mostrar el contingut de la tupla. Exemple: Usuari indica la paula caracteristica. Es mostra per pantalla carteis.

frase = input('Escribe una frase: ')
fraseUnida = []
letrasUsadas = []

for i in frase:
    if not(i.isspace()):
        if (letrasUsadas.count(i) == 0):
            fraseUnida.append(i)
            letrasUsadas.append(i)

print(tuple(fraseUnida))
