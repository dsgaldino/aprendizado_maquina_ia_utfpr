# -*- coding: utf-8 -*-
"""Modelo de Regressão Linear.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157W5n-cBLBsoO_YZukOKEI3g__UuVG48

# Ajustar um Modelo de Regressão Linear aos dados apresentados

Ajustar um Modelo de Regressão Linear aos dados apresentados:

- Coluna 1 - índice

- Coluna 2 - Entrada

- Coluna 3 - Saída

Entregar o código/parâmetros de regressão do modelo.

arquivo: treino_sinais_vitais_qPA_versus_Gravidade.csv

# Aluno: Diego Soares Galdino

### Importando bibliotecas
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

"""### Lendo o arquivo csv e definindo as colunas"""

# Ler o arquivo CSV sem cabeçalho
df = pd.read_csv('treino_sinais_vitais_qPA_versus_Gravidade.csv', header=None)
df.columns = ['index', 'entrada', 'saída']

"""### Análise exploratória Inicial"""

# Visualizar as primeiras linhas do dataframe
print(df.head())
print("\n")
# Verificar informações estatísticas dos dados
print(df.describe().T)

# Plotar scatter plot da relação entre entrada e saída
plt.scatter(df['entrada'], df['saída'])
plt.xlabel('Entrada')
plt.ylabel('Saída')
plt.title('Relação entre Entrada e Saída')
plt.show()

# Criar figura e eixos para os subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Plotar histograma da coluna "entrada"
axs[0].hist(df['entrada'], bins=10)
axs[0].set_xlabel('Entrada')
axs[0].set_ylabel('Frequência')
axs[0].set_title('Histograma da Entrada')

# Plotar histograma da coluna "saída"
axs[1].hist(df['saída'], bins=10)
axs[1].set_xlabel('Saída')
axs[1].set_ylabel('Frequência')
axs[1].set_title('Histograma da Saída')

# Ajustar espaçamento entre subplots
plt.tight_layout()

# Exibir os subplots
plt.show()

# Calcular e visualizar a matriz de correlação
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Matriz de Correlação')
plt.show()

"""### Regressão Linear"""

# Extrair as colunas de entrada e saída
entrada = df['entrada'].values.reshape(-1, 1)
saida = df['saída'].values

# Criar um objeto de regressão linear
regressao = LinearRegression()

# Ajustar o modelo aos dados
regressao.fit(entrada, saida)

# Parâmetros da regressão
coeficiente_angular = regressao.coef_
intercepto = regressao.intercept_

print("Coeficiente Angular:", coeficiente_angular)
print("Intercepto:", intercepto)

# Plotar os dados com a linha de regressão
plt.scatter(entrada, saida, color='blue', label='Dados')
plt.plot(entrada, regressao.predict(entrada), color='red', label='Regressão Linear')
plt.xlabel('Entrada')
plt.ylabel('Saída')
plt.legend()
plt.title('Regressão Linear')
plt.show()