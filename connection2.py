import mysql.connector

connection = mysql.connector.connect(
    host='localhost', database='bd', user='root', password='')
if connection.is_connected():
    db_info = connection.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)
if connection.is_connected():
    cursor.close()
    connection.close()
    print("Conexão ao MySQL foi encerrada")
