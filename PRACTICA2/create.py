import psycopg2
import connection

try:

    sql = '''INSERT INTO pets(pet_id, pet_name, pet_surname, pet_age, pet_type, pet_color) VALUES (%s,%s,%s,%s,%s)'''
    
    record_to_insert = [(1, 'Packt', 1950,
                         'chennai', 'books'),
                        (2, 'Springer', 1950,
                         'chennai', 'books'),
                        (3, 'Springer', 1950,
                         'chennai', 'articles'),
                        (4, 'Oxford', 1950,
                         'chennai', 'all'),
                        (5, 'MIT', 1950,
                         'chennai', 'books')]
    
    for i in record_to_insert:
        connection.connection.execute(sql, i)
        connection.conn.commit()

        count = connection.conn.rowcount
        print(count, "Record inserted successfully into publisher table")
 
except (Exception, psycopg2.Error) as error:
    print("Error al insertar en la tabla", error)
 
finally:
    if connection:
        connection.close()
        print("GOODBYE")

