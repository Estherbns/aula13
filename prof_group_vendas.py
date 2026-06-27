import pandas as pd

df = pd.read_excel("Vendas_empresas.xlsx")

# ==================== 1. GROUPBY SIMPLES ====================
print("\n" + "="*70)
print("1. GROUPBY SIMPLES - AGRUPANDO POR UMA COLUNA")
print("="*70)

# 1.1 Média de Salário por Departamento
print("\n💰 Média Salarial por Departamento:")
media_salario = df.groupby('Departamento')['Salario'].mean().round(2)
print(media_salario)

# 1.2 Total de Vendas por Departamento
print("\n📈 Total de Vendas por Departamento (em milhares):")
total_vendas = df.groupby('Departamento')['Vendas_Mes'].sum() / 1000
print(total_vendas.round(2))

# 1.3 Contagem de Funcionários por Departamento
print("\n👥 Quantidade de Funcionários por Departamento:")
contagem_func = df.groupby('Departamento')['ID_Funcionario'].count()
print(contagem_func)

# 1.4 Média de Horas Extras por Departamento
print("\n⏰ Média de Horas Extras por Departamento:")
media_he = df.groupby('Departamento')['Horas_Extras'].mean().round(2)
print(media_he)

# 1.5 Média de Idade por Cargo
print("\n🎂 Média de Idade por Cargo:")
media_idade = df.groupby('Cargo')['Idade'].mean().round(2)
print(media_idade)

# ==================== 2. GROUPBY COM MÚLTIPLAS COLUNAS ====================
print("\n" + "="*70)
print("2. GROUPBY COM MÚLTIPLAS COLUNAS")
print("="*70)

# 2.1 Média Salarial por Departamento e Cargo
print("\n💰 Média Salarial por Departamento e Cargo:")
media_salario_cargo = df.groupby(['Departamento', 'Cargo'])['Salario'].mean().round(2)
print(media_salario_cargo)

# 2.2 Contagem por Departamento e Meta Alcançada
print("\n📊 Contagem por Departamento e Meta Alcançada:")
contagem_meta = df.groupby(['Departamento', 'Meta_Alcancada']).size()
print(contagem_meta)

# 2.3 Média de Vendas por Cargo e Meta
print("\n📈 Média de Vendas por Cargo e Meta Alcançada:")
media_vendas_meta = df.groupby(['Cargo', 'Meta_Alcancada'])['Vendas_Mes'].mean().round(2)
print(media_vendas_meta)

# 2.4 Total de Vendas por Departamento e Cargo (em milhares)
print("\n📊 Total de Vendas por Departamento e Cargo (em milhares):")
total_vendas_cargo = df.groupby(['Departamento', 'Cargo'])['Vendas_Mes'].sum() / 1000
print(total_vendas_cargo.round(2))

# ==================== 4. ANÁLISE DE META ALCANÇADA ====================
print("\n" + "="*70)
print("4. ANÁLISE DE META ALCANÇADA (STRING)")
print("="*70)

# 4.1 Tabela Cruzada - Departamento x Meta
print("\n📊 Tabela Cruzada - Departamento x Meta:")
cross_meta = pd.crosstab(df['Departamento'], df['Meta_Alcancada'])
print(cross_meta)

# 4.2 Percentual de Meta por Departamento
print("\n📊 Percentual de Meta Alcançada por Departamento:")
if 'Sim' in cross_meta.columns:
    cross_meta['%_Meta'] = (cross_meta['Sim'] / cross_meta.sum(axis=1) * 100).round(2)
print(cross_meta)

# 4.3 Análise Detalhada por Departamento e Meta
print("\n📊 Análise Detalhada por Departamento e Meta:")
analise_meta = df.groupby(['Departamento', 'Meta_Alcancada']).agg({
    'Salario': 'mean',
    'Vendas_Mes': 'sum',
    'Horas_Extras': 'sum',
    'ID_Funcionario': 'count'
}).round(2)
print(analise_meta)

# 4.4 Comparação: Quem Bateu a Meta vs Quem Não Bateu
print("\n📊 Comparação entre Quem Bateu e Quem Não Bateu a Meta:")
comparacao_meta = df.groupby('Meta_Alcancada').agg({
    'Salario': ['mean', 'min', 'max'],
    'Vendas_Mes': ['mean', 'sum'],
    'Horas_Extras': ['mean', 'sum'],
    'ID_Funcionario': 'count'
}).round(2)
print(comparacao_meta)

# 4.5 Filtrando apenas quem bateu a meta
print("\n📊 Média Salarial de Quem Bateu a Meta por Departamento:")
meta_sim = df[df['Meta_Alcancada'] == 'Sim']
media_meta_sim = meta_sim.groupby('Departamento')['Salario'].mean().round(2)
print(media_meta_sim) 