import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'db_userv'
}
conn = mysql.connector.connect(**config)

# Carregar a planilha
caminho_da_planilha = r'C:\Users\jacks\My Drive\uServ\cidades.xlsx'
# Se sua planilha estiver em formato CSV, você pode usar caminho_da_planilha = 'caminho/para/sua/planilha.csv'
dataframe = pd.read_excel(caminho_da_planilha, sheet_name="DTB_2022_Municipio")

cities = dataframe.city
# categorias = dataframe.Categoria.drop_duplicates()
states = dataframe.state
# unidades = dataframe['Unidades de Medida'].drop_duplicates()

print(f'Inserindo estados...')
try:
    cursor = conn.cursor()
    for i, row in dataframe.iterrows():
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO state (state, name, code) VALUES ("{row.sigla}", "{row.state}", "{row.code_state}")')
        cursor.execute('SELECT LAST_INSERT_ID()')
        state_id = cursor.fetchone()[0]
        cursor.execute(f'INSERT INTO city (city, code, state_id) VALUES ("{row.city}", "{row.code_city}", {state_id})')
        
    conn.commit()
    conn.close()    

except Error as e:
    # Rollback em caso de erro
    conn.rollback()
    print("Erro ao inserir:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL foi encerrada.")


