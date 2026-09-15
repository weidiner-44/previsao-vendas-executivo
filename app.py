import streamlit as st
import pandas as pd
from src.modelo import treinar_e_prever

st.set_page_config(page_title="Dashboard Executivo de Previsão", layout="wide")

st.title("📊 Painel Executivo: Previsão de Demanda e Otimização")
st.markdown("Sistema inteligente de suporte à decisão para análise de histórico de vendas e projeção de cenário futuro.")

# Carregar dados e previsões
@st.cache_data
def carregar_dados():
    return treinar_e_prever(dias_futuros=30)

df_historico, df_previsao = carregar_dados()

# Indicadores Principais (KPIs)
st.subheader("Indicações Rápidas de Desempenho")
col1, col2, col3 = st.columns(3)

faturamento_total_historico = df_historico['vendas'].sum()
media_diaria = df_historico['vendas'].mean()
total_previsto_proximo_mes = df_previsao['vendas_previstas'].sum()

col1.metric("Média Diária Histórica", f"R$ {media_diaria:,.2f}")
col2.metric("Projeção Próximos 30 Dias", f"R$ {total_previsto_proximo_mes:,.2f}")
col3.metric("Volume Histórico Total", f"R$ {faturamento_total_historico:,.2f}")

st.divider()

# Gráfico de Histórico + Previsão
st.subheader("📈 Histórico de Vendas e Projeção Futura")

# Unir dados para exibição fluida no gráfico
df_grafico_hist = df_historico.rename(columns={'vendas': 'Valor'})
df_grafico_hist['Tipo'] = 'Histórico Real'

df_grafico_prev = df_previsao.rename(columns={'vendas_previstas': 'Valor'})
df_grafico_prev['Tipo'] = 'Previsão Machine Learning'

df_final = pd.concat([df_grafico_hist, df_grafico_prev])

# Exibição do gráfico nativo do Streamlit
st.line_chart(df_final.set_index('data')['Valor'])

# Seção de Tabela Detalhada
with st.expander("🔍 Ver dados detalhados da projeção para os próximos dias"):
    st.dataframe(df_previsao, use_container_width=True)