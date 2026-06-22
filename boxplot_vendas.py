import pandas as pd
import numpy as np

# Carregar arquivo
df = pd.read_excel('Vendas_empresas.xlsx')
serie_salarios = pd.Series(df['Salario'])
serie_venda_mes = pd.Series(df['Vendas_Mes'])
serie_idades = pd.Series(df['Idade'])
serie_hora_extra = pd.Series(df['Horas_Extras'])

# Cálculo dos elementos do boxplot de salarios ------------------------------------------------
Q1 = serie_salarios.quantile(0.25)      # Primeiro quartil (25%)
Q2 = serie_salarios.quantile(0.50)      # Mediana (50%)
Q3 = serie_salarios.quantile(0.75)      # Terceiro quartil (75%)
IQR = Q3 - Q1                   # Amplitude interquartil

# Bigodes (whiskers) - método padrão do matplotlib
limite_inferior = Q1 - (1.5 * IQR)
limite_superior = Q3 + (1.5 * IQR)

# Bigodes reais (menor/maior valor dentro dos limites)
whisker_inferior = serie_salarios[serie_salarios >= limite_inferior].min()
whisker_superior = serie_salarios[serie_salarios <= limite_superior].max()

# Outliers
outliers = serie_salarios[(serie_salarios < limite_inferior) | (serie_salarios > limite_superior)]
#---------------- fim de salario ---------------

# Cálculo dos elementos do boxplot de venda mensal ------------------------------------------------
BQ1 = serie_venda_mes.quantile(0.25)      # Primeiro quartil (25%)
BQ2 = serie_venda_mes.quantile(0.50)      # Mediana (50%)
BQ3 = serie_venda_mes.quantile(0.75)      # Terceiro quartil (75%)
BIQR = BQ3 - BQ1                   # Amplitude interquartil

# Bigodes (whiskers) - método padrão do matplotlib
limite_inferiorB = BQ1 - (1.5 * BIQR)
limite_superiorB = BQ3 + (1.5 * BIQR)

# Bigodes reais (menor/maior valor dentro dos limites)
whisker_inferiorB = serie_venda_mes[serie_venda_mes >= limite_inferiorB].min()
whisker_superiorB = serie_venda_mes[serie_venda_mes <= limite_superiorB].max()

# Outliers
outliersB = serie_salarios[(serie_venda_mes < limite_inferiorB) | (serie_venda_mes > limite_superiorB)]
#---------------- fim de de venda mensal ---------------

# Cálculo dos elementos do boxplot de Idades ------------------------------------------------
CQ1 = serie_idades.quantile(0.25)      # Primeiro quartil (25%)
CQ2 = serie_idades.quantile(0.50)      # Mediana (50%)
CQ3 = serie_idades.quantile(0.75)      # Terceiro quartil (75%)
CIQR = CQ3 - CQ1                   # Amplitude interquartil

# Bigodes (whiskers) - método padrão do matplotlib
limite_inferiorC = CQ1 - (1.5 * CIQR)
limite_superiorC = CQ3 + (1.5 * CIQR)

# Bigodes reais (menor/maior valor dentro dos limites)
whisker_inferiorC = serie_idades[serie_idades >= limite_inferiorC].min()
whisker_superiorC = serie_idades[serie_idades <= limite_superiorC].max()

# Outliers
outliersC = serie_idades[(serie_idades < limite_inferiorC) | (serie_idades > limite_superiorC)]
#---------------- fim de idades ---------------


print("Boxplot de salarios")
print(f"Q1 (25%): {Q1}")
print(f"Q2 (50%): {Q2}")
print(f"Q3 (75%): {Q3}")
print(f"IQR: {IQR}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Whisker inferior: {whisker_inferior}")
print(f"Whisker superior: {whisker_superior}")
print(f"Outliers: {outliers.tolist()}")
print("***************************")

print("Boxplot de venda mensal")
print(f"Q1 (25%): {BQ1}")
print(f"Q2 (50%): {BQ2}")
print(f"Q3 (75%): {BQ3}")
print(f"IQR: {BIQR}")
print(f"Limite inferior: {limite_inferiorB}")
print(f"Limite superior: {limite_superiorB}")
print(f"Whisker inferior: {whisker_inferiorB}")
print(f"Whisker superior: {whisker_superiorB}")
print(f"Outliers: {outliersB.tolist()}")
print("***************************")

print("Boxplot de idades")
print(f"Q1 (25%): {CQ1}")
print(f"Q2 (50%): {CQ2}")
print(f"Q3 (75%): {CQ3}")
print(f"IQR: {CIQR}")
print(f"Limite inferior: {limite_inferiorC}")
print(f"Limite superior: {limite_superiorC}")
print(f"Whisker inferior: {whisker_inferiorC}")
print(f"Whisker superior: {whisker_superiorC}")
print(f"Outliers: {outliersC.tolist()}")
print("***************************")