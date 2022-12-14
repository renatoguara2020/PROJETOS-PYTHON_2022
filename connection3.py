import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="",
                                     database="bd")

try:
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        bd = cursor.fetchone()
        print("Você está conectado ao banco de dados: ", bd)
except Error as e:
    print("Erro ao conectar ao MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("A conexão MySQL está fechada")
