#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - #
import pandas as pd
import numpy  as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt


## carrega o dataset
venda_casas = "house_sales.csv"
dataset_venda_casas = pd.read_csv(venda_casas, sep='\t')
colunas = ['AdjSalePrice', 'SqFtTotLiving', 'SqFtLot', 'Bathrooms',
           'Bedrooms', 'BldgGrade']
print(dataset_venda_casas[colunas].head())

## cria o modelo
preditoras = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms',
              'BldgGrade']
alvo = 'AdjSalePrice'

modelo_casas = LinearRegression()
modelo_casas.fit(dataset_venda_casas[preditoras],
                     dataset_venda_casas[alvo])

print(f'Intercepto: {modelo_casas.intercept_:.3f}')
print('Coeficientes:')
for nome, coef in zip(preditoras, modelo_casas.coef_):
    print(f' {nome}: {coef}')
