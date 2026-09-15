import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_historicos():
    np.random.seed(42)
    dias = 730  # 2 anos de histórico
    data_inicio = datetime.now() - timedelta(days=dias)
    
    datas = [data_inicio + timedelta(days=i) for i in range(dias)]
    
    # Criando tendência de crescimento + sazonalidade semanal + ruído aleatório
    tendencia = np.linspace(1000, 2500, dias)
    sazonalidade_semana = np.sin(np.arange(dias) * (2 * np.pi / 7)) * 300
    ruido = np.random.normal(0, 150, dias)
    
    vendas = np.clip(tendencia + sazonalidade_semana + ruido, 500, None)
    
    df = pd.DataFrame({
        'data': datas,
        'vendas': vendas.round(2)
    })
    
    df.to_csv('data/dados_vendas.csv', index=False)
    print("Dataset gerado com sucesso em 'data/dados_vendas.csv'!")

if __name__ == "__main__":
    gerar_dados_historicos()