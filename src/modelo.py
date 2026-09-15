import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def treinar_e_prever(dias_futuros=30):
    # Carregar dados
    df = pd.read_csv('data/dados_vendas.csv')
    df['data'] = pd.to_datetime(df['data'])
    
    # Engenharia de atributos (Features) baseadas em tempo
    df['dias_desde_inicio'] = (df['data'] - df['data'].min()).dt.days
    df['dia_semana'] = df['data'].dt.dayofweek
    df['mes'] = df['data'].dt.month
    
    X = df[['dias_desde_inicio', 'dia_semana', 'mes']]
    y = df['vendas']
    
    # Treinamento do Modelo
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    # Criar datas futuras para previsão
    ultima_data = df['data'].max()
    datas_futuras = [ultima_data + timedelta(days=i) for i in range(1, dias_futuros + 1)]
    
    df_futuro = pd.DataFrame({'data': datas_futuras})
    df_futuro['dias_desde_inicio'] = (df_futuro['data'] - df['data'].min()).dt.days
    df_futuro['dia_semana'] = df_futuro['data'].dt.dayofweek
    df_futuro['mes'] = df_futuro['data'].dt.month
    
    X_futuro = df_futuro[['dias_desde_inicio', 'dia_semana', 'mes']]
    df_futuro['vendas_previstas'] = modelo.predict(X_futuro).round(2)
    
    return df, df_futuro[['data', 'vendas_previstas']]