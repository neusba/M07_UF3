# En este archivo veremos la ejecución de todo el CRUD

import psycopg2     # Adaptador de postgreSQL para Python
import connection   # Conexión a la bbdd
import create_table # Query para crear la tabla PETS
import create       # C: crea una instancia para la tabla PETS
import read         # R: lee uno o más datos de la bbdd
import update       # U: actualiza una instancia 
import delete       # D: borra una instancia 

try:
    print('Bienvenido al CRUD. Vamos a comenzar creando la tabla PETS en caso de que aun no exista...')
    create_table.createTable()

    print('Pausita para mirar que la tabla se ha creado correctamente en la bbdd. Pulsa Enter para continuar.')
    usuario = input('Enter: \n')
    
    # Ahora insertamos datos por defecto en la tabla
    create.create()
    print('Datos insertados correctamente. \n')

    # Leemos los datos que acabamos de insertar
    print('---------------------------------------------- DATOS -------------------------------------------------:')
    read.read()
    print('----------------------------------------------------------------------------------------------------:\n')

    print('Momento para comprobar los datos insertados en la base de datos. Enter para actualizar.')
    usuario = input('Enter: \n')

    # Actualizamos algunos de los datos que ya tenemos y comprobamos que han cambiado
    update.update()
    print('---------------------------------------- DATOS ACTUALIZADOS ------------------------------------------:')
    read.read() # Mostramos lo que acabamos de actualizar
    print('----------------------------------------------------------------------------------------------------:\n')

    print('Miramos la base de datos y vemos que efectivamente algún dato ha cambiado. Enter y pasamos a DELETE.')
    usuario = input('Enter: \n')

    # Eliminados alguna instancia y comprobamos que ya no aparece
    delete.delete()
    print('---------------------------------------- DATOS SIN LOS ELIMINADOS --------------------------------------:')
    read.read()
    print('----------------------------------------------------------------------------------------------------:\n')

    print('Vemos que ya ha eliminado una instancia en la base de datos.')
    print('Como úlitmo paso se elimina la tabla PETS para poder repetir el proceso sin problema. Pulsa Enter para eliminarla y finalizar.\n')
    usuario = input('Enter: \n')

    # Limpiar base de datos para reestablecer
    sql = ''' DROP TABLE IF EXISTS pets '''
    connection.connection.execute(sql)
    connection.conn.commit()


except (Exception, psycopg2.Error) as error:
    print('Error', error)

finally:
    print('Cerrando conexión con la base de datos...')
    connection.conn.close()
    print('GOODBYE')


