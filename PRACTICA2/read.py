# Archivo para leer la información de la base de datos

import connection
 
def read():
    
    sql = "SELECT * FROM PETS"
 
    connection.connection.execute(sql)

    datos_pets = connection.connection.fetchall()
 
    for i in datos_pets:
        print("ID: ", i[0], )
        print("Name: ", i[1])
        print("Surname: ", i[2])
        print("Age: ", i[3])
        print("Type: ", i[4])
        print("Color: ", i[5])

