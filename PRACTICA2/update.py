# Archivo para actualizar los datos que ya tenemos en la tabla y cambiar sus valores

import connection

def update():

    sql = '''UPDATE pets
             SET pet_age = 4, pet_type = 'European cat'
             WHERE pet_id = 1'''
    
    connection.connection.execute(sql)
    connection.conn.commit()