import pandas as pd
import numpy as np

dados = pd.Series([10, 12, 15, 18, 20, 22, 25, 28, 30, 35, 40, 45, 50, 55, 60])

# Cálculo dos elementos do boxplot
Q1 = dados.quantile(0.25)      # Primeiro quartil (25%)
Q2 = dados.quantile(0.50)      # Mediana (50%)
Q3 = dados.quantile(0.75)      # Terceiro quartil (75%)
IQR = Q3 - Q1                   # Amplitude interquartil

# Bigodes (whiskers) - método padrão do matplotlib
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Bigodes reais (menor/maior valor dentro dos limites)
whisker_inferior = dados[dados >= limite_inferior].min()
whisker_superior = dados[dados <= limite_superior].max()

# Outliers
outliers = dados[(dados < limite_inferior) | (dados > limite_superior)]

print(f"Q1 (25%): {Q1}")
print(f"Q2 (50%): {Q2}")
print(f"Q3 (75%): {Q3}")
print(f"IQR: {IQR}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")
print(f"Whisker inferior: {whisker_inferior}")
print(f"Whisker superior: {whisker_superior}")
print(f"Outliers: {outliers.tolist()}")
