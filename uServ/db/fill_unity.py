
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'db_userv'
}



unities=[
    'Minutos',
    'Horas',
    'Dias',
    'Semanas',
    'Meses',
]
# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
try:

    # Criar cursor
    cursor = conn.cursor()   
        
    # Inserir dados 
    for p in unities:        
        cursor.execute(f'INSERT INTO db_userv.unit_of_execution (name, active) VALUES ("{p}", True)')

    # Commitar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

except Error as e:
    # Rollback em caso de erro
    conn.rollback()
    print("Erro ao inserir os unidades:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL foi encerrada.")



