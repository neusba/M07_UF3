import psycopg2

# Datos para la conexión con la base de datos
conn = psycopg2.connect(
    database="practica2",
    user='neus2',
    password='neus1234',
    host='localhost',
    port='5432'
)

# Método cursor() para hacer la conexión
connection = conn.cursor()
print(connection)
    