# En este archivo crearemos la query para crear la tabla PETS y se la enviaremos a la base de datos

import connection

def createTable():

    sql = '''CREATE TABLE IF NOT EXISTS PETS(
                pet_id SERIAL PRIMARY KEY,
                pet_name VARCHAR(255) NOT NULL,
                pet_surname VARCHAR(255) NOT NULL,
                pet_age BIGINT NOT NULL,
                pet_type VARCHAR(255) NOT NULL,
                pet_color VARCHAR(255) NOT NULL
    )'''

    print(sql)


    # Usamos el método execute() para enviar la query
    connection.connection.execute(sql)
    # Método para hacer efectivos los cambios en la BBDD
    connection.conn.commit()
