# Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla el mes corresponent al número indicat per l’usuari. El programa finalitza només quan l’usuari posa 0.
meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

while True:
    numero = int(input('Introduce un número entre el 0 y el 12: '))
    if numero == 0:
        break
    print(meses[numero-1])

print('Fin del programa')