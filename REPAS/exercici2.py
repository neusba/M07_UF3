# Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que introdueixi el IVA a aplicar-hi (4%, 10% o 21%) i finalment mostrar, per pantalla, el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit
valor = input('Introduce un valor en €')
iva = input('Introduce el IVA a aplicar entre los siguientes: 4%, 10%, 21%')

total = (int(valor) * int(iva)) / 100

print('El valor introducido por el usuario es: ', valor)
print('El IVA aplicado es:', iva)
print('El precio total es: ' , total)


