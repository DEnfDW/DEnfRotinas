#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:



df = pd.read_csv("RJ2017.txt", sep=';', encoding='latin1')


# In[12]:


df.head()


# In[13]:


# Conta o número de observações não nulas em cada coluna
contagem_por_coluna = df.count()

# Exibe a contagem por coluna
print(contagem_por_coluna)


# In[14]:


# Lê o arquivo CSV
df = pd.read_csv("RJ2017.txt", sep=';', encoding='latin1', dtype={'CBO Ocupação 2002': str})

# Exibe o DataFrame
print(df)


# In[15]:


# Leitura do arquivo CSV com especificação de tipo para a coluna 'CBO Ocupação 2002'
df = pd.read_csv("RJ2017.txt", sep=';', encoding='latin1', dtype={'CBO Ocupação 2002': str})

# Lista dos códigos CBO desejados
codigos_desejados = [
    '223505', '223510', '223515', '223520', '223525', '223530', '223535', '223540',
    '223545', '223550', '223555', '223560', '223565', '233125', '234415', '322205',
    '322210', '322215', '322220', '322230', '322235', '322245', '322250', '322245', '322250'
]

# Filtrar o DataFrame
RAIS_filtrada = df[df['CBO Ocupação 2002'].isin(codigos_desejados)]

# Filtrar valores ausentes (NaN) em outras colunas, se necessário
RAIS_filtrada = RAIS_filtrada.dropna()

# Exibir o DataFrame filtrado
print(RAIS_filtrada)


# In[16]:


descritivas = RAIS_filtrada
descritivas.describe(include = "all").T


# In[17]:


# Percentual de dados ausentes para cada coluna
percentual_ausentes = (RAIS_filtrada.isnull().sum() / len(RAIS_filtrada)) * 100
print("Percentual de dados ausentes:")
print(percentual_ausentes)


# In[18]:


# Agrupar por município e contar o número de profissionais de enfermagem em cada município
contagem_municipio = RAIS_filtrada.groupby('Município')['CBO Ocupação 2002'].count().reset_index()

# Exibir a lista de profissionais de enfermagem por município
print(contagem_municipio)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(contagem_municipio)


# In[19]:


import matplotlib.pyplot as plt
import seaborn as sns

# Configurar o estilo do seaborn para plotagens mais bonitas
sns.set(style="whitegrid")

# Criar o histograma
plt.figure(figsize=(10, 6))
sns.histplot(RAIS_filtrada['Idade'], bins=20, kde=False, color='blue')

# Configurar rótulos e título
plt.title('Histograma de Idade dos Profissionais de Enfermagem')
plt.xlabel('Idade')
plt.ylabel('Número de Profissionais')

# Exibir o histograma
plt.show()


# In[20]:


# Contagem de valores de Raça Cor
contagem_raca_cor = RAIS_filtrada['Raça Cor'].value_counts().reset_index()

# Renomear as colunas
contagem_raca_cor.columns = ['Raça Cor', 'Número de Profissionais']

# Exibir a lista de contagem
print(contagem_raca_cor)


# In[21]:


# Criar histograma da coluna "Raça Cor" para os dados filtrados
plt.figure(figsize=(10, 6))
sns.countplot(x='Raça Cor', data=RAIS_filtrada, palette='pastel', edgecolor='black')

# Adicione rótulos e título
plt.title('Distribuição da Amostra por Raça Cor para Profissionais de Enfermagem')
plt.xlabel('Raça Cor')
plt.ylabel('Contagem de Profissionais')

# Exiba o histograma
plt.show()

# Verifique a distribuição dos valores na coluna "Raça Cor"
print(RAIS_filtrada['Raça Cor'].value_counts())


# In[39]:


# Gráfico de Dispersão para 'Raça Cor'
plt.figure(figsize=(12, 8))
sns.scatterplot(data=RAIS_filtrada, x='Idade', y='Vl Remun Média (SM)', hue='Raça Cor', palette='pastel')
plt.title('Gráfico de Dispersão entre Idade e Remuneração Média por Raça Cor')
plt.xlabel('Idade')
plt.ylabel('Remuneração Média (SM)')
plt.show()

# Gráfico de Dispersão para 'Sexo'
plt.figure(figsize=(12, 8))
sns.scatterplot(data=RAIS_filtrada, x='Idade', y='Vl Remun Média (SM)', hue='Sexo Trabalhador', palette='pastel')
plt.title('Gráfico de Dispersão entre Idade e Remuneração Média por Sexo')
plt.xlabel('Idade')
plt.ylabel('Remuneração Média (SM)')
plt.show()


# In[23]:


# Análise de Moda para 'Raça Cor'
moda_raca_cor = RAIS_filtrada['Raça Cor'].mode()

# Análise de Moda para 'Sexo'
moda_sexo = RAIS_filtrada['Sexo Trabalhador'].mode()

# Exibir os resultados
print(f"Moda para Raça Cor: {moda_raca_cor.values}")
print(f"Moda para Sexo: {moda_sexo.values}")


# In[24]:


# Criar histograma da coluna "Sexo" para os dados filtrados
plt.figure(figsize=(10, 6))
sns.countplot(x='Sexo Trabalhador', data=RAIS_filtrada, palette='pastel', edgecolor='black')

# Adicione rótulos e título
plt.title('Distribuição da Amostra por Sexo para Profissionais de Enfermagem')
plt.xlabel('Sexo')
plt.ylabel('Contagem de Profissionais')

# Exiba o histograma
plt.show()

# Verifique a distribuição dos valores na coluna "Sexo"
print(RAIS_filtrada['Sexo Trabalhador'].value_counts())


# In[25]:




# Criar um boxplot para idade e sexo
plt.figure(figsize=(12, 8))
sns.boxplot(x='Sexo Trabalhador', y='Idade', data=RAIS_filtrada, palette='pastel')
plt.title('Boxplot da Idade por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Idade')

# Exibir o boxplot
plt.show()

# Criar um boxplot para idade e raça cor
plt.figure(figsize=(12, 8))
sns.boxplot(x='Raça Cor', y='Idade', data=RAIS_filtrada, palette='pastel')
plt.title('Boxplot da Idade por Raça Cor')
plt.xlabel('Raça Cor')
plt.ylabel('Idade')

# Exibir o boxplot
plt.show()


# In[26]:


# Criar histograma da coluna "Nacionalidade" para os dados filtrados
plt.figure(figsize=(10, 6))
sns.countplot(x='Nacionalidade', data=RAIS_filtrada, palette='pastel', edgecolor='black')

# Adicione rótulos e título
plt.title('Distribuição da Amostra por Nacionalidade para Profissionais de Enfermagem')
plt.xlabel('Nacionalidade')
plt.ylabel('Contagem de Profissionais')

# Exiba o histograma
plt.show()

# Verifique a distribuição dos valores na coluna "Nacionalidade"
print(RAIS_filtrada['Nacionalidade'].value_counts())


# In[27]:


# Criar histograma da coluna "Vl Remun Média" para os dados filtrados
#plt.figure(figsize=(10, 6))
#sns.histplot(RAIS_filtrada['Vl Remun Média (SM)'], bins=20, kde=False, color='blue')

# Adicione rótulos e título
#plt.title('Histograma de Remuneração Média para Profissionais de Enfermagem')
#plt.xlabel('Remuneração Média')
#plt.ylabel('Número de Profissionais')

# Exiba o histograma
#plt.show()

# Remover caracteres não numéricos e converter para float
RAIS_filtrada['Vl Remun Média (SM)'] = RAIS_filtrada['Vl Remun Média (SM)'].replace('[\$,]', '', regex=True).astype(float)

# Criar histograma
plt.figure(figsize=(10, 6))
sns.histplot(RAIS_filtrada['Vl Remun Média (SM)'].dropna(), bins=20, kde=True, color='skyblue', edgecolor='black')

# Adicionar rótulos e título
plt.title('Histograma de Remuneração Média para Profissionais de Enfermagem')
plt.xlabel('Remuneração Média (SM)')
plt.ylabel('Contagem de Profissionais')

# Exibir o histograma
plt.show()


# In[28]:


# Remover caracteres não numéricos e converter para float
RAIS_filtrada['Vl Remun Média (SM)'] = RAIS_filtrada['Vl Remun Média (SM)'].replace('[\$,]', '', regex=True).astype(float)

# Boxplot para 'Vl Remun Média (SM)'
plt.figure(figsize=(10, 6))
sns.boxplot(x=RAIS_filtrada['Vl Remun Média (SM)'], color='skyblue')
plt.title('Boxplot de Vl Remun Média (SM)')
plt.xlabel('Vl Remun Média (SM)')

# Exibir o boxplot
plt.show()


# In[29]:


# Remover caracteres não numéricos (vírgula) e converter para float
RAIS_filtrada['Vl Remun Dezembro Nom'] = RAIS_filtrada['Vl Remun Dezembro Nom'].str.replace(',', '').astype(float)

# Criar histograma da coluna "Vl Remun Média" para os dados filtrados
plt.figure(figsize=(10, 6))
sns.histplot(RAIS_filtrada['Vl Remun Dezembro Nom'], bins=20, kde=False, color='blue')

# Adicionar rótulos e título
plt.title('Histograma de Remuneração Média para Profissionais de Enfermagem')
plt.xlabel('Remuneração Média')
plt.ylabel('Número de Profissionais')

# Exibir o histograma
plt.show()


# In[30]:


# KDE para 'Sexo'
plt.figure(figsize=(12, 8))
sns.kdeplot(data=RAIS_filtrada, x='Vl Remun Média (SM)', hue='Sexo Trabalhador', fill=True, common_norm=False, palette='pastel')
plt.title('Densidade de Remuneração Média por Sexo')
plt.xlabel('Remuneração Média (SM)')
plt.show()


# In[31]:


# KDE (Kernel Density Estimate) para 'Raça Cor'
plt.figure(figsize=(12, 8))
sns.kdeplot(data=RAIS_filtrada, x='Vl Remun Média (SM)', hue='Raça Cor', fill=True, common_norm=False, palette='pastel')
plt.title('Densidade de Remuneração Média por Raça Cor')
plt.xlabel('Remuneração Média (SM)')
plt.show()


# In[32]:


# Matriz de Correlação para atributos numéricos
correlation_matrix = RAIS_filtrada[['Idade', 'Vl Remun Média (SM)']].corr()

# Heatmap da Matriz de Correlação
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=1)
plt.title('Matriz de Correlação entre Idade e Remuneração Média')
plt.show()


# In[33]:


# Análise de Média, Mediana e Variância para 'Raça Cor'
media_raca_cor = RAIS_filtrada.groupby('Raça Cor')['Vl Remun Média (SM)'].mean()
mediana_raca_cor = RAIS_filtrada.groupby('Raça Cor')['Vl Remun Média (SM)'].median()
variancia_raca_cor = RAIS_filtrada.groupby('Raça Cor')['Vl Remun Média (SM)'].var()

# Análise de Média, Mediana e Variância para 'Sexo'
media_sexo = RAIS_filtrada.groupby('Sexo Trabalhador')['Vl Remun Média (SM)'].mean()
mediana_sexo = RAIS_filtrada.groupby('Sexo Trabalhador')['Vl Remun Média (SM)'].median()
variancia_sexo = RAIS_filtrada.groupby('Sexo Trabalhador')['Vl Remun Média (SM)'].var()

# Exibir os resultados
print("Análise para Raça Cor:")
print(f"Média:\n{media_raca_cor}\n\nMediana:\n{mediana_raca_cor}\n\nVariância:\n{variancia_raca_cor}\n")

print("Análise para Sexo:")
print(f"Média:\n{media_sexo}\n\nMediana:\n{mediana_sexo}\n\nVariância:\n{variancia_sexo}\n")


# In[ ]:





# In[34]:


print(RAIS_filtrada['Vl Remun Média (SM)'].describe())
print(RAIS_filtrada['Vl Remun Média (SM)'].unique())


# In[35]:


# Contar observações onde 'Mun Trab' é diferente de 'Município'
diferencas_municipio = RAIS_filtrada[RAIS_filtrada['Mun Trab'] != RAIS_filtrada['Município']]

# Obter a contagem de observações diferentes
contagem_diferencas = len(diferencas_municipio)

# Exibir a contagem
print(f'Número de observações onde "Mun Trab" é diferente de "Município": {contagem_diferencas}')


# In[36]:


# Identificar observações onde 'Mun Trab' é diferente de 'Município'
diferencas_municipio = RAIS_filtrada[RAIS_filtrada['Mun Trab'] != RAIS_filtrada['Município']]

# Agrupar por CBO e contar observações diferentes para cada CBO
contagem_por_cbo = diferencas_municipio.groupby('CBO Ocupação 2002').size().reset_index(name='Contagem')

# Exibir a contagem por CBO
print(contagem_por_cbo)

#


# In[37]:


# Criar uma coluna para armazenar as diferenças entre 'Mês Admissão' e 'Mês Desligamento'
RAIS_filtrada['Diferença Meses'] = RAIS_filtrada['Mês Desligamento'] - RAIS_filtrada['Mês Admissão']

# Filtrar as linhas onde a diferença é diferente de zero
diferencas_meses = RAIS_filtrada[RAIS_filtrada['Diferença Meses'] != 0]

# Exibir as linhas onde 'Mês Admissão' é diferente de 'Mês Desligamento'
print("Linhas onde 'Mês Admissão' é diferente de 'Mês Desligamento':")
print(diferencas_meses[['Mês Admissão', 'Mês Desligamento', 'Diferença Meses']])


# In[38]:


# Contagem de ocorrências para 'Mês Admissão'
contagem_mes_admissao = RAIS_filtrada['Mês Admissão'].value_counts().reset_index()
contagem_mes_admissao.columns = ['Mês Admissão', 'Contagem']

# Contagem de ocorrências para 'Mês Desligamento'
contagem_mes_desligamento = RAIS_filtrada['Mês Desligamento'].value_counts().reset_index()
contagem_mes_desligamento.columns = ['Mês Desligamento', 'Contagem']

# Exibir as contagens
print("Contagem de 'Mês Admissão':")
print(contagem_mes_admissao)

print("\nContagem de 'Mês Desligamento':")
print(contagem_mes_desligamento)


# In[ ]:




