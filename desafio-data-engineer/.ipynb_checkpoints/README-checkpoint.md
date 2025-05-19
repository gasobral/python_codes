# Entrega do desafio
A empresa *Triggo.ai* propôs um desafio para realizar análise sobre
o data set da Olist. Desenvolvemos este projeto para realizar tal
tarefa. Para ver as análises, basta abrir o notebook no diretório
*notebooks*. A execução dele deve realizar as análises propostas
pelo desafio da *Triggo.ai*. Consideramos que os arquivos do data
set da Olist já foram baixados e estão diretório *data/bruto*. Para
visualizar os dashboards, será necessáirio executar partes do notebook
da Seção 4 e os scripts do diretório scripts. É necessaŕio ter as
seguintes bibliotecas:

* numpy
* pandas
* sklearn
* matplotlib
* sqlite3
* streamlit

# Estrutura do diretŕio
O projeto possui a estrutura de diretórios abaixo. No diretório *data*,
os subdiretórios significam:

* bruto: são os dados descompactados diretamente do data set da Olist
* intermediáro: são dados que já passaram por algum tratamento
* processado: são dados tratados que podem ser usados em análises

O diretório *figures* contém uma figura que representa o modelo relacional
exigido no desafio.

```
├── banco_dados
│   ├── ecommerce.db
│   └── query.sql
├── data
│   ├── bruto
│   │   ├── olist_customers_dataset.csv
│   │   ├── olist_geolocation_dataset.csv
│   │   ├── olist_order_items_dataset.csv
│   │   ├── olist_order_payments_dataset.csv
│   │   ├── olist_order_reviews_dataset.csv
│   │   ├── olist_orders_dataset.csv
│   │   ├── olist_products_dataset.csv
│   │   ├── olist_sellers_dataset.csv
│   │   └── product_category_name_translation.csv
│   ├── intermediario
│   └── processado
├── figures
│   └── modelo_relacional.png
├── notebooks
│   └── desafio.ipynb
├── README.md
└── scripts
    ├── dashboard_analise_vendedores.py
    └── dashboard_vendas_tempo.py
```