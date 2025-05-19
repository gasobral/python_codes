import sqlite3

import pandas         as pd
import streamlit      as st
import plotly.express as px


## Carregamento dos dados
vendas_tempo = pd.read_csv('../data/processado/vendas_tempo.csv')
vendas_tempo.columns = ['order_id',
                        'data_venda',
                        'product_category_name',
                        'customer_state']


## Configuração do streamlit
st.sidebar.title("Filtros")
estados = st.sidebar.multiselect(
    "Selecione os estados:",
    options=sorted(vendas_tempo['customer_state'].unique()),
    default=None
)

categorias = st.sidebar.multiselect(
    "Selecione as categorias:",
    options=sorted(vendas_tempo['product_category_name'].dropna().unique()),
    default=None
)


## Filtragem do data frame
vendas_tempo_filtrado = vendas_tempo.copy()

## utilizei o isin para permitir que seja selecionado mais de um estado
## ou categoria
if estados:
    mascara = vendas_tempo_filtrado['customer_state'].isin(estados)
    vendas_tempo_filtrado = vendas_tempo_filtrado[mascara]

if categorias:
    mascara = vendas_tempo_filtrado['product_category_name'].isin(categorias)
    vendas_tempo_filtrado = vendas_tempo_filtrado[mascara]

## Construção do data frame a ser usado no dashboard
vendas_tempo_agg = vendas_tempo_filtrado.groupby(by=['data_venda'])['order_id'].count()
vendas_tempo_agg = vendas_tempo_agg.reset_index()


## Exibição do data frame
st.title('Dashboard de vendas ao longo do tempo')

fig = px.line(vendas_tempo_agg,
              x='data_venda',
              y='order_id',
              title='Evolução das Vendas',
              markers=True)

fig.update_layout(xaxis_title="Data",
                  yaxis_title="Total de Vendas",
                  template="plotly_white")
st.plotly_chart(fig, use_container_width=True)
