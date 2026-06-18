import pandas as pd
#notas = pd.Series([8.5, 9.0, 7.5], index=['Ana', 'Beto', 'Caio'])

# Carregar arquivo
df = pd.read_excel('vendas_empresas.xlsx')


media_sal =df['Salario'].mean()
max_sal =df['Salario'].max()

# Mostrar todas as colunas, forçando
#pd.set_option('display.max_columns', None)

# (Opcional) Mostrar todas as linhas também, forçando
#pd.set_option('display.max_rows', None)


Sumo_vendas_Meta_Alcancada = df[df["Meta_Alcancada"] == "Sim" ]["Vendas_Mes"].sum() # vai aparecer o total das metas alcançadas ( do sim)
Sumo_vendas_Meta_Alcancada22 = df[(df["Meta_Alcancada"] == "Sim") & (df["Salario"] > 5000)]["Vendas_Mes"].sum()
funcionario_Meta_Alcancada = df[df["Meta_Alcancada"] == "Sim" ]["Nome"]
media_Meta_Alcancada =df['Vendas_Mes'].mean()
print(df)
print(media_Meta_Alcancada)


