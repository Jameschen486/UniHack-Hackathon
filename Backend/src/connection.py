import mysql.connector
import time

# MySQL Configuration
db_name = 'mydatabase'
db_host = 'localhost'
db_local_host = 'localhost'
db_user = 'root'
db_password = 'password1234'

# Defined exceptions
class DatabaseConnectionException(Exception):
    pass

class DatabaseExistsException(Exception):
    pass

def make_connection():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user= db_user,
            password=db_password,
            database= db_name
        )
        cursor = connection.cursor()
        return connection, cursor
    except:
        raise DatabaseConnectionException("Could not connect to the database")

def make_connection_local():
    try:
        connection = mysql.connector.connect(
            host=db_local_host,
            user= db_user,
            password=db_password,
            database= db_name
        )
        cursor = connection.cursor()
        return connection, cursor
    except:
        raise DatabaseConnectionException("Could not connect to the database")
    

def end_connection(connection, cursor):
    connection.commit()
    if cursor:
        cursor.close()
    if connection:
        connection.close()