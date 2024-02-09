# Archivo en el que insertamos datos de prueba para comprobar que aparecen posteriormente en la base de datos seleccionada
import connection

def create():

    sql = '''INSERT INTO pets(pet_id, pet_name, pet_surname, pet_age, pet_type, pet_color) VALUES (%s,%s,%s,%s,%s,%s)'''
    
    datos = [(1, 'Hamlet', 'Bravo', 3, 'Cat', 'Grey/White'),
             (2, 'Peanut', 'Bravo', 2, 'Cat', 'Orange'),
             (3, 'Jaggy', 'Bravo', 1, 'Cat', 'White'),
             (4, 'Coco', 'Channel', 3, 'Dog', 'White/Brown'),
             (5, 'Rayo', 'Macuin', 4, 'Dog', 'Black/Brown')]
    
    print('Insertando datos...')
    for i in datos:
        connection.connection.execute(sql, i)
        connection.conn.commit()
