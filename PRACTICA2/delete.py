# Archivo que borra una instancia de la tabla PETS

import connection

def delete():

    sql = '''DELETE FROM pets
             WHERE pet_type = 'Dog'
             '''
    
    # Estas a punto de elimimar: x, x, x

    connection.connection.execute(sql)
    connection.conn.commit()