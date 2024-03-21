import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'db_userv',
}
conn = mysql.connector.connect(**config)

# Carregar a planilha
caminho_da_planilha = r'Servicos.xlsx'
# Se sua planilha estiver em formato CSV, você pode usar caminho_da_planilha = 'caminho/para/sua/planilha.csv'
dataframe = pd.read_excel(caminho_da_planilha, sheet_name="Planilha4")

segmentos = dataframe.Segmento.drop_duplicates()
# categorias = dataframe.Categoria.drop_duplicates()
servicos = dataframe.Serviço.drop_duplicates()
# unidades = dataframe['Unidades de Medida'].drop_duplicates()

try:
    # Criar cursor
    cursor = conn.cursor()           
    # Inserir dados 
    for segmento in segmentos:    
        print(f'Inserindo segmento: {segmento}...')    
        cursor.execute(f'INSERT INTO category (name, active) VALUES ("{segmento}", True)')   
        cursor.execute('SELECT LAST_INSERT_ID()')
        ultimo_segmento = cursor.fetchone()[0]
        for categoria in dataframe.query(f'Segmento == "{segmento}"').Categoria.drop_duplicates():
            print(f'Inserindo categoria: {categoria}...')
            cursor.execute(f'INSERT INTO category (name, active, parent_id) VALUES ("{categoria}", True, {ultimo_segmento})')
            cursor.execute('SELECT LAST_INSERT_ID()')
            ultima_categoria = cursor.fetchone()[0]
            for servico in dataframe.query(f'Segmento == "{segmento}" and Categoria == "{categoria}"').Serviço.drop_duplicates():
                print(f'Inserindo serviço: {servico}...')
                cursor.execute(f'INSERT INTO general_service (description, category_id) VALUES ("{servico}", {ultima_categoria})')
                cursor.execute('SELECT LAST_INSERT_ID()')
                ultimo_servico = cursor.fetchone()[0]
                for unidade in dataframe.query(f'Segmento == "{segmento}" and Categoria == "{categoria}" and Serviço == "{servico}"')['Unidades de Medida'].drop_duplicates():
                    print(f'Inserindo unidade: {unidade}...')
                    cursor.execute(f'INSERT INTO unit_for_service (name, active, general_service_id) VALUES ("{unidade}", True, {ultimo_servico})') 

    # Commitar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

except Error as e:
    # Rollback em caso de erro
    conn.rollback()
    print("Erro ao inserir os serviços:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL foi encerrada.")


