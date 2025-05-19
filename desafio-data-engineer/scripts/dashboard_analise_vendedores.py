import sqlite3

import pandas         as pd
import streamlit      as st
import plotly.express as px


## Carregamento dos dados
vendas_tempo = pd.read_csv('../data/processado/analise_vendedores.csv')


## Computa o volume de vendas, número de venda, tempo de entrega médio e
## avaliação média dos vendedores
vendas_agg = vendas_tempo.groupby('seller_id').agg(
    total_vendas=('price', 'sum'),
    n_vendas=('price', 'count'),
    avg_tempo_entrega=('tempo_entrega', 'mean'),
    avg_review=('review_score', 'mean')
).reset_index()


## Computa uma pontuação baseada na avaliação média da duas vendas,
## do tempo de entrega (é computado como 1/tempo, pois quanto maior
## o tempo pior é o score) e o número de vendas em relação ao maior
## número de vendas (dentre todos os vendedores)
vendas_agg['pontuacao'] = (
    vendas_agg['avg_review'] +
    (1 / vendas_agg['avg_tempo_entrega']) +
    (vendas_agg['n_vendas'] / vendas_agg['n_vendas'].max())
)

## Configuração do streamlit
st.title("Dashboard da análise dos vendedores (sellers)")


## Filtros do streamlit
filtro_vendedor = st.multiselect(
    "Filtrar por vendedores:",
    options=vendas_agg['seller_id'].unique(),
    default=None
)


vendas_filtrado = vendas_agg.copy()

if filtro_vendedor:
    vendas_filtrado = vendas_filtrado[vendas_filtrado['seller_id'].isin(filtro_vendedor)]


## Criação dos gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("Volume de Vendas")
    fig1 = px.bar(vendas_filtrado,
                  x='seller_id',
                  y='n_vendas',
                  color='n_vendas',
                  text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Média de Avaliação")
    fig2 = px.bar(vendas_filtrado,
                  x='seller_id',
                  y='avg_review',
                  color='avg_review',
                  range_y=[0,5])
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Tempo Médio de Entrega")
    fig3 = px.bar(vendas_filtrado,
                  x='seller_id',
                  y='avg_tempo_entrega',
                  color='avg_tempo_entrega')
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Ranking por Desempenho")
    fig4 = px.bar(vendas_filtrado.sort_values('pontuacao', ascending=False),
                  x='seller_id',
                  y='pontuacao',
                  color='pontuacao')
    st.plotly_chart(fig4, use_container_width=True)
