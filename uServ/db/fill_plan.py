
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'db_userv'
}

plans=[
        {
            'name':'Basico',
            'description':'loremipsong', 
            'price': 1 
        },
       {
            'name': 'Premium',
            'description': 'loremipsong',
            'price': 2  
       }]
# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
try:

    # Criar cursor
    cursor = conn.cursor()   
        
    # Inserir dados 
    for p in plans:        
        cursor.execute(f'INSERT INTO db_userv.plan (name, description, price, active) VALUES ("{p['name']}", "{p['description']}", {p['price']}, True)')

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



