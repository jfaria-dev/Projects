
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

screens = [
    {
        'name':'User-Home',
        'description':'Home',
        'namespace':'user',
        'url': '',
        'title': 'Home',
        'paragraph': 'Welcome to uServ',
        'active': True        
    },
    {
        'name':'User-Login',
        'description':'Login',
        'namespace':'user',
        'url': 'login',
        'title': 'Login',
        'paragraph': 'Login to uServ',
        'active': True        
    },
    {
        'name':'User-Register',
        'description':'Register',
        'namespace':'user',
        'url': 'register',
        'title': 'Register',
        'paragraph': 'Register to uServ',
        'active': True        
    },
    {
        'name':'User-Add_Service',
        'description':'Add service and schedule',
        'namespace':'user',
        'url': 'add-service',
        'title': 'Add Service',
        'paragraph': 'Add service and schedule',
        'active': True        
    },
    {
        'name':'Supplier-Home',
        'description':'Home supplier',
        'namespace':'supplier',
        'url': 'supplier/',
        'title': 'Cadastre já no <span class="text-purple-500 text-bold">uServ<span>',
        'paragraph': 'Welcome to uServ',
        'active': True        
    },
    {
        'name':'Supplier-Login',
        'description':'Login',
        'namespace':'supplier',
        'url': 'supplier/login',
        'title': 'Login',
        'paragraph': 'Login to uServ',
        'active': True        
    },
    {
        'name':'Supplier-Register',
        'description':'Register',
        'namespace':'supplier',
        'url': 'supplier/register',
        'title': 'Bora pro <span class="text-purple-500 text-bold">uServ<span> logo ',
        'paragraph': 'Registre no uServ',
        'active': True        
    },
    {
        'name':'Supplier-Details',
        'description':'Register Details of Store in App',
        'namespace':'supplier',
        'url': 'supplier/register/<int:supplier>',
        'title': 'Informações da Empresa',
        'paragraph': 'Informe seus Dados para o <span class="text-purple-500 text-bold">uServ<span>',
        'active': True        
    },
    {
        'name':'Supplier-Address',
        'description':'Register Address',
        'namespace':'supplier',
        'url': 'supplier/register/<int:supplier>/address',
        'title': 'Endereço',
        'paragraph': 'Register to uServ',
        'active': True        
    },
]

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
            'url': 'supplier/register',
            'active': True
       },
       {
            'name':'Supplier-Register',
            'description':'Register step-2 supplier - rest of fields', 
            'url': 'supplier/register/<int:supplier>',
            'active': True
       },
       {
            'name':'Supplier-Address',
            'description':'Register step-2 supplier - rest of fields', 
            'url': 'supplier/register/<int:supplier>/address',
            'active': True
       },
        {
            'name':'Supplier-Plan',
            'description':'Register step-2 supplier - rest of fields', 
            'url': 'supplier/register/<int:supplier>/plan',
            'active': True
       },
       {
            'name':'Supplier-Login',
            'description':'Login supplier', 
            'url': 'supplier/login',
            'active': True
        },]
# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
try:

    # Criar cursor
    cursor = conn.cursor()   
        
    # Inserir dados 
    for p in screens:        
        base_query = "INSERT INTO db_userv.web_screen (name, description, namespace, url, title, paragraph, active, created_by_id, created_on) "
        values_query = f"VALUES ('{p['name']}', '{p['description']}', '{p['namespace']}', '{p['url']}', '{p['title']}', '{p['paragraph']}', True, 1, '{datetime.now()}')"
        cursor.execute(base_query + values_query)
    
    # for p in menus:        
    #     cursor.execute(f'INSERT INTO db_userv.web_menu (name, description, action, active, created_on) VALUES ("{p['name']}", "{p['description']}", "{p['url']}", {p['active']}, "2024-01-21")')

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



