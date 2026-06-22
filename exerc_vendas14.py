import pandas as pd

# Carregar arquivo
df = pd.read_excel('Vendas_empresas.xlsx')

df_Quantitativa = df[['Salario', 'Vendas_Mes', 'Horas_Extras', 'Idade']]
df_Qualitativa = df[['Nome', 'Departamento', 'Cargo', 'Data_Admissao',]]

df_Quantitativa.to_csv('Quant_vendas.csv', index=False)
df_Qualitativa.to_csv('Qualit_vendas.csv', index=False)

#print(df)
#print(df_Quantitativa)
print(df_Qualitativa)
