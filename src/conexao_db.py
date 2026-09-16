import pandas as pd
from sqlalchemy import create_engine

# String de Conexão com o SQL Server (Autenticação do Windows)
# Se usar usuário e senha, a string muda para: 'mssql+pyodbc://usuario:senha@servidor/PrevisaoVendasDB?driver=ODBC+Driver+17+for+SQL+Server'
SERVER = 'localhost\\SQLEXPRESS' # Ajuste para o nome do seu servidor
DATABASE = 'PrevisaoVendasDB'

def obter_conexao_str():
    return f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

def salvar_dados_no_sql(df, nome_tabela):
    engine = create_engine(obter_conexao_str())
    # Salva o DataFrame como uma tabela no SQL Server
    df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)
    print(f"Dados salvos com sucesso na tabela '{nome_tabela}' do SQL Server!")

def ler_dados_do_sql(nome_tabela):
    engine = create_engine(obter_conexao_str())
    return pd.read_sql(f"SELECT * FROM {nome_tabela}", con=engine)