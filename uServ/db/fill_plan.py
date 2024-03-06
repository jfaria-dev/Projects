
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Configurações do banco de dados
config = {
    'host': 'monorail.proxy.rlwy.net',
    'user': 'root',
    'password': 'hBH4bDeAdFFabC-ABgb-B4C2D1bgh4Ff',
    'database': 'db_userv',
    'port': '28310'
}

plans=[
        {
            'name':'Basico',
            'description':'loremipsong', 
            'price': 1 ,
            'created_at': datetime.now()
        },
       {
            'name': 'Premium',
            'description': 'loremipsong',
            'price': 2  ,
            'created_at': datetime.now()
       }]
# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
try:

    # Criar cursor
    cursor = conn.cursor()   
        
    # Inserir dados 
    for p in plans:        
        cursor.execute(f'INSERT INTO db_userv.plan (name, description, price, duration, created_at, is_active) VALUES ("{p['name']}", "{p['description']}", {p['price']}, 12, "{p['created_at']}", True)')

    # Commitar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

except Error as e:
    # Rollback em caso de erro
    conn.rollback()
    print("Erro ao inserir os planos:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL foi encerrada.")



