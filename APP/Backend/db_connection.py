import mysql.connector
from mysql.connector import Error

def connect():
    """Connect to MySQL Database"""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  # Cambia esto a la dirección del servidor si no es localhost    
            database='api_bank',
            user='root',
            password='12345678'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            print("Conexión exitosa")
            return connection, cursor
    
    except Error as e:
        print("Error al conectar a MySQL", e)
        return None, None

def disconnect(connection, cursor):
    """Disconnect from DB"""
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Desconexión exitosa")

if __name__ == "__main__":
    connection, cursor = connect()
    if connection and cursor:
        # Aquí puedes agregar el código para interactuar con la base de datos
        disconnect(connection, cursor)
