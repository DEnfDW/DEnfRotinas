#!/usr/bin/env python
# coding: utf-8

# # CAGED 2022.01

# In[7]:


import pandas as pd
import numpy as np


# In[2]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202201.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[3]:


df.head()


# In[4]:


# Conta o número de observações não nulas em cada coluna
contagem_por_coluna = df.count()

# Exibe a contagem por coluna
print(contagem_por_coluna)


# In[5]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202201.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# In[6]:


descritivas = caged_filtrado
descritivas.describe(include = "all").T


# In[8]:


caged_filtrado.describe(include=[np.number]).T


# In[9]:


# Para contar os valores ausentes em cada coluna:
valores_ausentes = caged_filtrado.isna().sum()

# Para exibir a contagem de valores ausentes:
print(valores_ausentes)


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns

# Configurar o estilo do seaborn para plotagens mais bonitas
sns.set(style="whitegrid")

# Criar o histograma
plt.figure(figsize=(10, 6))
sns.histplot(caged_filtrado['idade'], bins=20, kde=False, color='blue')

# Configurar rótulos e título
plt.title('Histograma de Idade dos Profissionais de Enfermagem')
plt.xlabel('Idade')
plt.ylabel('Número de Profissionais')

# Exibir o histograma
plt.show()


# In[9]:


# Contagem de valores de Raça Cor
contagem_raca_cor = caged_filtrado['raçacor'].value_counts().reset_index()

# Renomear as colunas
contagem_raca_cor.columns = ['raçacorr', 'Número de Profissionais']

# Exibir a lista de contagem
print(contagem_raca_cor)


# In[13]:


# Criar histograma da coluna "Sexo" para os dados filtrados
plt.figure(figsize=(10, 6))
sns.countplot(x='sexo', data=caged_filtrado, palette='pastel', edgecolor='black')

# Adicione rótulos e título
plt.title('Distribuição da Amostra por Sexo para Profissionais de Enfermagem')
plt.xlabel('Sexo')
plt.ylabel('Contagem de Profissionais')

# Exiba o histograma
plt.show()

# Verifique a distribuição dos valores na coluna "Sexo"
print(caged_filtrado['sexo'].value_counts())


# In[15]:


# Criar histograma da coluna "Nacionalidade" para os dados filtrados
plt.figure(figsize=(10, 6))
sns.countplot(x='tipodedeficiência', data=caged_filtrado, palette='pastel', edgecolor='black')

# Adicione rótulos e título
plt.title('Distribuição da Amostra PCD')
plt.xlabel('tipodedeficiência')
plt.ylabel('Contagem de Profissionais')

# Exiba o histograma
plt.show()

# Verifique a distribuição dos valores na coluna "Nacionalidade"
print(caged_filtrado['tipodedeficiência'].value_counts())


# # CAGED 2022.02

# In[5]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202202.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[6]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202202.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.03

# In[7]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202203.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[8]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202203.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.04

# In[9]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202204.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[10]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202204.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.05

# In[11]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202205.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[12]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202205.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.06

# In[13]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202206.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[14]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202206.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.07

# In[15]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202207.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[16]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202207.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.08

# In[17]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202208.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[18]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202208.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.09

# In[19]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202209.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[20]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202209.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.10

# In[21]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202210.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[22]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202210.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.11

# In[23]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202211.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[24]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202211.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()

# Exibir o DataFrame filtrado
print(caged_filtrado)


# # CAGED 2022.12

# In[25]:


# Leia o arquivo CSV com a especificação de tipos de dados e codificação correta
df = pd.read_csv("CAGEDMOV202212.txt", sep=';', encoding='utf-8')

# Exiba as primeiras linhas do DataFrame
print(df)


# In[26]:


# Leitura do arquivo TXT
caged = pd.read_csv("CAGEDMOV202212.txt", sep=';', encoding='utf-8')

# Lista dos códigos CBO desejados
codigos_desejados = [
    223505, 223510, 223515, 223520, 223525, 223530, 223535, 223540,
    223545, 223550, 223555, 223560, 223565, 233125, 234415, 322205,
    322210, 322215, 322220, 322230, 322235, 322245, 322250, 322245, 322250
]

# Filtrar o DataFrame
caged_filtrado = caged[caged['cbo2002ocupação'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
caged_filtrado = caged_filtrado.dropna()


# Exibir o DataFrame filtrado
print(caged_filtrado)


# In[27]:


# Conta o número de observações não nulas em cada coluna
contagem_por_coluna = caged_filtrado.count()

# Exibe a contagem por coluna
print(contagem_por_coluna)

