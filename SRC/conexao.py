import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'cardoso',
    host = 'localhost',
    password = 'projeto123',
    database = 'projeto_crud'
)
# testando a conexão
if conn.is_connected():
    print("Conectado com MySQL database")
else:
    print("Conexão falhado")