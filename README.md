[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://previsao-vendas-executivo-woyvhnmfssimmntutrhvuz.streamlit.app/)

Sistema de Previsão de Demanda e Dashboard Executivo

Sistema inteligente de suporte à decisão voltado para análise de séries temporais de vendas e projeção de cenários futuros, integrando engenharia de dados, modelagem preditiva e visualização executiva.



Sobre o Projeto
Este projeto foi desenvolvido para resolver um problema comum em empresas de comércio e varejo: a falta de previsibilidade sobre o faturamento futuro, que costuma gerar excesso de estoque ou ruptura de produtos. 

A solução automatiza a leitura do histórico de vendas, treina um modelo preditivo baseado em machine learning e disponibiliza um painel executivo (Dashboard) interativo em tempo real para gestores.



Tecnologias Utilizadas
O projeto foi construído utilizando uma stack moderna focada em Python:
Python 3.10+**: Linguagem principal do projeto.
Pandas & NumPy**: Manipulação, limpeza e engenharia de atributos (feature engineering).
Scikit-Learn**: Treinamento do modelo preditivo de Regressão Linear baseado em sazonalidade e tendência temporal.
Streamlit**: Construção do painel web interativo para exibição dos KPIs e gráficos executivos.



Estrutura do Repositório
text
previsao-vendas-executivo/
│
├── data/
│   └── dados_vendas.csv     # Dataset histórico simulado
├── src/
│   ├── __init__.py
│   ├── gerador_dados.py     # Script gerador de dados de vendas realistas
│   └── modelo.py            # Lógica de engenharia de dados e treinamento do modelo
├── app.py                   # Aplicação principal do Dashboard (Streamlit)
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto


Como Executar o Projeto Localmente
Siga os passos abaixo para rodar o projeto na sua máquina:

1. Clone o repositório:
git clone [https://github.com/weidiner-44/previsao-vendas-executivo.git](https://github.com/weidiner-44/previsao-vendas-executivo.git)
cd previsao-vendas-executivo

cd previsao-vendas-executivo

2. Instale as dependências:
pip install -r requirements.txt

3. Gere o dataset simulado:
python src/gerador_dados.py

4. Inicie o Dashboard:
streamlit run app.py

O painel abrirá automaticamente no seu navegador padrão (geralmente em http://localhost:8501).


Funcionalidades do Dashboard
KPIs Executivos: Visão rápida da média diária histórica, faturamento acumulado e projeção total para os próximos 30 dias.

Gráfico Dinâmico: Linha do tempo unindo o histórico real de vendas com a projeção gerada por Machine Learning.

Demonstração do Dashboard

Aqui está a visualização final do painel executivo integrado ao SQL Server em modo *Dark Tech*:

![Dashboard Executivo Power BI](images/dashboard-vendas.png)

