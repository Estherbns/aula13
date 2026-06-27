import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando o arquivo Excel
df = pd.read_excel('Vendas_empresas.xlsx')

# Visualizando os dados
print(df.head())
print("\nInformações do DataFrame:")
print(df.info())

# Gráfico de linha mostrando a evolução dos salários
df.plot(x='ID_Funcionario', y='Salario', kind='line', figsize=(10, 5), marker='o', color='blue', linewidth=2)
plt.title('Salários dos Funcionários por ID', fontsize=14)
plt.xlabel('ID do Funcionário')
plt.ylabel('Salário (R$)')
plt.grid(True, alpha=0.3)
plt.show()

# Gráfico de barras mostrando vendas por funcionário
df.plot(x='Nome', y='Vendas_Mes', kind='bar', figsize=(12, 6), color='green', edgecolor='black')
plt.title('Vendas por Funcionário', fontsize=14)
plt.xlabel('Funcionário')
plt.ylabel('Vendas do Mês (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Barras horizontais
df.plot(x='Nome', y='Idade', kind='barh', 
        figsize=(10, 6), color='orange')
plt.title('Idade dos Funcionários', fontsize=14)
plt.xlabel('Idade')
plt.ylabel('Funcionário')
plt.tight_layout()
plt.show()

# Histograma mostrando a distribuição dos salários
df['Salario'].plot(kind='hist', bins=15, figsize=(10, 5), 
                   color='purple', alpha=0.7, edgecolor='black')
plt.title('Distribuição dos Salários', fontsize=14)
plt.xlabel('Salário (R$)')
plt.ylabel('Frequência')
plt.grid(True, alpha=0.3)
plt.show()




#Join, cont e merge de Dataframes

import pandas as pd

df = pd.read_excel("Vendas_empresas.xlsx")
df2 = df[["Salario", "Vendas_Mes"]].copy()
df2["idadeDobro"] = df["Idade"]*2

df.sort_values('Salario')
df.sort_values('Salario', ascending=False)
df.sort_values(["Salario", "Vendas_Mes"]) 


pd.concat([df, df2], axis=1) # comando sem inplace=True não altera o dataframe
pd.merge([df, df2], on="Vendas_Mes")

print(pd.merge(df, df2, on="Vendas_Mes"))
