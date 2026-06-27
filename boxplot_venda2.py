import pandas as pd
import numpy as np

# Carregar arquivo
df = pd.read_excel('Vendas_empresas.xlsx')

# Criar as séries
serie_salarios = pd.Series(df['Salario'])
serie_venda_mes = pd.Series(df['Vendas_Mes'])
serie_idades = pd.Series(df['Idade'])
serie_hora_extra = pd.Series(df['Horas_Extras'])

def calcular_boxplot(serie, nome_serie):
    """
    Calcula e retorna todos os elementos do boxplot para uma série
    
    Parâmetros:
    serie: pandas Series
    nome_serie: str - Nome da série para exibição
    
    Retorna:
    dict: Dicionário com todos os elementos do boxplot
    """
    
    # Cálculo dos quartis
    Q1 = serie.quantile(0.25)
    Q2 = serie.quantile(0.50)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    
    # Limites para detecção de outliers
    limite_inferior = Q1 - (1.5 * IQR)
    limite_superior = Q3 + (1.5 * IQR)
    
    # Bigodes (whiskers) - valores reais dentro dos limites
    whisker_inferior = serie[serie >= limite_inferior].min()
    whisker_superior = serie[serie <= limite_superior].max()
    
    # Outliers
    outliers = serie[(serie < limite_inferior) | (serie > limite_superior)]
    
    # Estatísticas adicionais
    estatisticas = {
        'média': serie.mean(),
        'desvio_padrao': serie.std(),
        'minimo': serie.min(),
        'maximo': serie.max(),
        'total': serie.sum(),
        'count': serie.count()
    }
    
    # Retornar todos os valores em um dicionário
    return {
        'nome': nome_serie,
        'Q1': Q1,
        'Q2': Q2,
        'Q3': Q3,
        'IQR': IQR,
        'limite_inferior': limite_inferior,
        'limite_superior': limite_superior,
        'whisker_inferior': whisker_inferior,
        'whisker_superior': whisker_superior,
        'outliers': outliers.tolist() if not outliers.empty else [],
        'quantidade_outliers': len(outliers),
        'estatisticas': estatisticas
    }

def exibir_boxplot(resultado):
    """
    Exibe os resultados do boxplot de forma formatada
    """
    print(f"\n{'='*60}")
    print(f"📊 BOXPLOT - {resultado['nome'].upper()}")
    print(f"{'='*60}")
    
    print(f"\n📌 QUARTIS:")
    print(f"  Q1 (25%): {resultado['Q1']:.2f}")
    print(f"  Q2 (50%): {resultado['Q2']:.2f}")
    print(f"  Q3 (75%): {resultado['Q3']:.2f}")
    
    print(f"\n📌 AMPLITUDE:")
    print(f"  IQR: {resultado['IQR']:.2f}")
    
    print(f"\n📌 LIMITES:")
    print(f"  Limite inferior: {resultado['limite_inferior']:.2f}")
    print(f"  Limite superior: {resultado['limite_superior']:.2f}")
    
    print(f"\n📌 BIGODES (WHISKERS):")
    print(f"  Whisker inferior: {resultado['whisker_inferior']:.2f}")
    print(f"  Whisker superior: {resultado['whisker_superior']:.2f}")
    
    print(f"\n📌 OUTLIERS:")
    print(f"  Quantidade: {resultado['quantidade_outliers']}")
    if resultado['outliers']:
        print(f"  Valores: {resultado['outliers']}")
    else:
        print("  Nenhum outlier detectado")
    
    print(f"\n📌 ESTATÍSTICAS ADICIONAIS:")
    print(f"  Média: {resultado['estatisticas']['média']:.2f}")
    print(f"  Desvio Padrão: {resultado['estatisticas']['desvio_padrao']:.2f}")
    print(f"  Mínimo: {resultado['estatisticas']['minimo']:.2f}")
    print(f"  Máximo: {resultado['estatisticas']['maximo']:.2f}")
    print(f"  Total: {resultado['estatisticas']['total']:.2f}")
    print(f"  Contagem: {resultado['estatisticas']['count']}")
    
    print(f"\n{'='*60}\n")

def analisar_todas_series():
    """
    Analisa todas as séries e exibe os resultados
    """
    series = [
        (serie_salarios, 'Salários'),
        (serie_venda_mes, 'Vendas por Mês'),
        (serie_idades, 'Idades'),
        (serie_hora_extra, 'Horas Extras')
    ]
    
    resultados = {}
    
    for serie, nome in series:
        resultado = calcular_boxplot(serie, nome)
        resultados[nome] = resultado
        exibir_boxplot(resultado)
    
    return resultados

def salvar_resultados(resultados, arquivo='resultados_boxplot.xlsx'):
    """
    Salva os resultados em um arquivo Excel
    """
    dados = []
    for nome, resultado in resultados.items():
        dados.append({
            'Série': nome,
            'Q1': resultado['Q1'],
            'Q2': resultado['Q2'],
            'Q3': resultado['Q3'],
            'IQR': resultado['IQR'],
            'Limite_Inferior': resultado['limite_inferior'],
            'Limite_Superior': resultado['limite_superior'],
            'Whisker_Inferior': resultado['whisker_inferior'],
            'Whisker_Superior': resultado['whisker_superior'],
            'Qtd_Outliers': resultado['quantidade_outliers'],
            'Média': resultado['estatisticas']['média'],
            'Desvio_Padrão': resultado['estatisticas']['desvio_padrao'],
            'Mínimo': resultado['estatisticas']['minimo'],
            'Máximo': resultado['estatisticas']['maximo']
        })
    
    df_resultados = pd.DataFrame(dados)
    df_resultados.to_excel(arquivo, index=False)
    print(f"\n✅ Resultados salvos em '{arquivo}'")

# Executar a análise
if __name__ == "__main__":
    print("🚀 INICIANDO ANÁLISE DE BOXPLOT PARA TODAS AS SÉRIES")
    print("="*60)
    
    # Analisar todas as séries
    resultados = analisar_todas_series()
    
    # Opcional: Salvar resultados em Excel
    salvar_resultados(resultados)
    
    print("\n✅ Análise concluída com sucesso!")