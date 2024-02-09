import psycopg2
import connection
 
try:
    
    sql = "select * from pets"
 
    connection.connection.execute(sql)

    datos_pets = connection.connection.fetchall()
 
    print("DATOS:")

    for i in datos_pets:
        print("ID: ", i[0], )
        print("Name: ", i[1])
        print("Surname: ", i[2])
        print("Age: ", i[3])
        print("Tipo: ", i[4])
        print("Color: ", i[5])


except (Exception, psycopg2.Error) as error:
    print("Error al intentar leer los datos", error)
 
finally:
    if connection:
        connection.conn.close()
        print("GOODBYE")