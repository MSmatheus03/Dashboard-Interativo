import streamlit as st
import pandas as pd

tabela = pd.read_excel("vendas.xlsx")

# titulo
st.title('dashboard de vendas')

# campo de seleção e filtro dos dados
regioes = st.multiselect('selecione as regiões',tabela['Região'].unique())

if regioes:
    tabela = tabela[tabela['Região'].isin(regioes)]


# 2 métricas
# faturamento total
st.metric('Faturamento Total',f'r${tabela['Valor Venda'].sum()}')

# ticket médio
st.metric('Ticket Médio',f'r${tabela['Valor Venda'].mean()}')

# gráfico faturamento por região
st.bar_chart(tabela.groupby('Região')['Valor Venda'].sum())


# gráfico faturamento por produto
st.bar_chart(tabela.groupby('Produto')['Valor Venda'].sum())