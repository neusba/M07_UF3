# En este archivo veremos la ejecución de todo el CRUD

import psycopg2     # Adaptador de postgreSQL para Python
import connection   # Conexión a la bbdd
import create_table # Query para crear la tabla PETS
import create       # C: crea una instancia para la tabla PETS
import read         # R: lee uno o más datos de la bbdd
import update       # U: actualiza una instancia 
import delete       # D: borra una instancia 

try:
    print('Bienvenido. Vamos a comenzar creando la tabla PETS en caso de que aun no exista...')
    create_table.createTable()

    # Ahora insertamos datos en la tabla para asegurarnos que podemos leer algo posteriormente
    usuario = int(input('Introduce el número 1 si quieres generar los datos.'))
    while usuario != 1:
        usuario = int(input('Introduce el número 1!!!!!'))
        
    create.create()
    print('Datos insertados correctamente.')
        

    # Leemos los datos que acabamos de insertar
    usuario = int(input('Vuelve a introducir el número 1 si quieres leer los datos que se acaban de insertar.'))
    while usuario != 1:
        usuario = int(input('Introduce el número 1!!!!!'))
        
    print('---------------------------------------------- DATOS -----------------------------------------------:')
    read.read()

    # Actualizamos algunos de los datos que ya tenemos y comprobamos que han cambiado
    usuario = int(input('Introduce otra vez el número 1 si ahora quieres actualizar los datos de la tabla.'))
    while usuario != 1:
        usuario = int(input('Introduce el número 1!!!!!'))

    update.update()
    print('---------------------------------------- DATOS ACTUALIZADOS ----------------------------------------:')
    read.read() # Leemos lo que acabamos de actualizar

    # Eliminados alguna instancia y comprobamos que ya no aparece
    usuario = int(input('Por último introduce el número 1 si quieres quieres eliminar alguna instancia.'))
    while usuario != 1:
        usuario = int(input('Introduce el número 1!!!!!'))
    
    delete.delete()
    read.read()

    # Limpiar base de datos para reestablecer
    usuario = int(input('Por último introduce el número 2 si quieres quieres eliminar la tabla.'))
    while usuario != 1:
        usuario = int(input('Introduce el número 2!!!!!'))
    sql = ''' DROP TABLE IF EXISTS pets '''
    connection.connection.execute(sql)
    connection.conn.commit()


except (Exception, psycopg2.Error) as error:
    print('Error', error)

finally:
    print('Cerrando conexión con la base de datos...')
    connection.conn.close()
    print('GOODBYE')


