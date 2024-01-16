
from datetime import datetime
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'db_userv'
}

menus = [
        {
            'name':'User-Home',
            'description':'Home', 
            'url': '',
            'active': True
        },
        {
            'name':'User-Login',
            'description':'Login', 
            'url': 'login',
            'active': True
        },
        {
            'name':'User-Register',
            'description':'Register', 
            'url': 'register',
            'active': True
        },
        {
            'name':'User-Add_Service',
            'description':'Add service and schedule', 
            'url': 'add-service',
            'active': True
        },
        {
            'name':'Supplier-Home',
            'description':'Home supplier', 
            'url': 'supplier/',
            'active': True
        },
       {
            'name':'Supplier-Register',
            'description':'Register step-1 supplier - name, email, phone', 
            'url': 'supplier/prestador',
            'active': True
       },
       {
            'name':'Supplier-Register',
            'description':'Register step-2 supplier - rest of fields', 
            'url': 'supplier/register',
            'active': True
       },
       {
            'name':'Supplier-Login',
            'description':'Login supplier', 
            'url': 'supplier/login',
            'active': True
        },
       {
            'name':'Supplier-Sign',
            'description':'Sign plan', 
            'url': 'supplier/sign-plan',
            'active': True
        },]
# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
try:

    # Criar cursor
    cursor = conn.cursor()   
        
    # Inserir dados 
    for p in menus:        
        cursor.execute(f'INSERT INTO db_userv.web_menu (name, description, url, active, created_on) VALUES ("{p['name']}", "{p['description']}", "{p['url']}", {p['active']}, "2024-01-12")')

    # Commitar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

except Error as e:
    # Rollback em caso de erro
    conn.rollback()
    print("Erro ao inserir os telas:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL foi encerrada.")



