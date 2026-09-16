import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sqlalchemy import create_engine

print("Gerando dados simulados de vendas...")

# 1. Gerar histórico de datas (últimos 2 anos)
np.random.seed(42)
dias = pd.date_range(start="2024-01-01", end=datetime.today(), freq="D")
n = len(dias)

# 2. Criar valores realistas com tendência de alta e sazonalidade
tendencia = np.linspace(1000, 2500, n)
sazonalidade = 300 * np.sin(np.linspace(0, 3 * np.pi, n))
ruido = np.random.normal(0, 150, n)
vendas = tendencia + sazonalidade + ruido
vendas = np.clip(vendas, 400, None) # Garante valores mínimos positivos

# 3. Montar o DataFrame
df_vendas = pd.DataFrame({
    'DataVenda': dias,
    'ValorTotal': vendas,
    'Quantidade': np.random.randint(1, 15, size=n),
    'Categoria': np.random.choice(['Eletrônicos', 'Móveis', 'Vestuário', 'Acessórios'], size=n)
})

# 4. Conectar ao SQL Server local e salvar na tabela 'Vendas'
print("Conectando ao SQL Server (PrevisaoVendasDB)...")
SERVER = 'localhost'
DATABASE = 'PrevisaoVendasDB'

# String de conexão com autenticação do Windows
connection_string = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(connection_string)

# Salva no banco (substitui a tabela se já existir)
df_vendas.to_sql('Vendas', con=engine, if_exists='replace', index=False)

print(f"Sucesso! {n} registros foram salvos na tabela 'Vendas' do SQL Server.")