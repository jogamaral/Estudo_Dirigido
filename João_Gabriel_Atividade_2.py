#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns


# Criação de interface com usuário para upload de arquivo csv.

# In[2]:


df = pd.read_csv ('D:/Documentos/Estudo Dirigido/Dados2.csv',sep=';',index_col='Amostra',decimal= ',')


# Leitura do Arquivo csv, definição de ";" como separador, definição da coluna "Amostra" como index e definição de "," como separador decimal.

# In[3]:


df = pd.read_csv(io.StringIO(uploaded[list(uploaded.keys())[0]].decode('utf-8')),sep=';',index_col='Amostra',decimal= ',')
df.head()


# Criação de dataframe "df_dados" para facilitar a escrita e compreensão.

# In[ ]:


df_dados = df[['Obs1','Obs2','Obs3','Obs4','Obs5','Obs6']]


# Criação da coluna "Media" com a média de cada linha.

# In[ ]:


df['Media'] = df_dados.mean(axis=1)


# Criação da coluna "Amplitude" com a diferença do máximo e mínimo de cada linha.

# In[ ]:


df['Amplitude'] = df_dados.max(axis=1) - df_dados.min(axis=1)


# Criação da coluna "Desvio Padrao" com o desvio padrão de cada linha.

# In[ ]:


df['Desvio Padrao'] = df_dados.std(axis=1)


# In[8]:


df.head()


# Cálculo da média das médias.

# In[9]:


med_media = df['Media'].mean(axis = 0)
med_media


# Cálculo da média dos desvios.

# In[10]:


med_desvio = df['Desvio Padrao'].mean(axis = 0)
med_desvio


# Cálculo da linha superior e inferior de controle.

# In[ ]:


LSC = med_media + 3 * med_desvio
LIC = med_media - 3 * med_desvio


# Criação do gráfico de controle de médias.

# In[21]:


# Definição do tamanho da figura e seu título
plt.figure(figsize = (10,6))
plt.title('Gráfico de controle de médias')

# Plota os dados e linhas de controle
sns.scatterplot(data = df_dados, markers = ['o']*df_dados.shape[1], s = 50)
plt.axhline(med_media, color = 'black', linestyle = 'dashed', linewidth = 2,label= 'LM',alpha = 0.5)
plt.axhline(LSC, color = 'r', linestyle = 'dashed', linewidth = 2,label = 'LSC')
plt.axhline(LIC, color = 'b', linestyle = 'dashed', linewidth = 2,label = 'LIC')

# Cria a legenda e coloca-a do lado exterior da figura
plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))

