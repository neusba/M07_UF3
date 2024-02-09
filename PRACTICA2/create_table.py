import connection
import psycopg2

try:

    # Archivo para crear la tabla de la BBDD (6 campos)
    sql = '''CREATE TABLE PETS(
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

except (Exception, psycopg2.Error) as error:
    print("Error:", error)
finally:
    print('GOODBYE')
    connection.conn.close()