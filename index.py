# Importar a base de dados
# Visualizar e entender a base de dados
# Tratar a base de dados
# Entender as notas dos clientes
# Entender como cara característica influencia na nota do cliente

# Bibliotecas:
# pandas - openpyxl - numpy - plotly - packaging ( caso der erro: --upgrade plotly plotly.express )

import pandas as pd
import plotly.express as px

# Lendo a base de dados em csv, o encoding serve para ler caracteres especiais, o sep serve para separar as colunas
tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

# Deletar a coluna "Unnamed: 8", já que não possui nenhum uso
# axis=1 serve para deletar colunas, axis=0 serve para deletar linhas
tabela = tabela.drop("Unnamed: 8", axis=1)

# Aparece as informações da tabela, dados vazios e tipos de dados
print(tabela.info())

# transformando a coluna de salário em númerico ao invés de string - erros="coerce" força a virar um número
tabela["Salário Anual (R$)"] = pd.to_numeric(
    tabela["Salário Anual (R$)"], errors="coerce")

# corrigir informações vazias
tabela = tabela.dropna()

# entender as notas dos clientes
# describe da uma visão geral de como funciona a tabela, com informações de média, desvio padrão, etc
print(tabela.describe())

for coluna in tabela.columns:
    grafico = px.histogram(
        tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10, title=f"Relação entre {coluna} e Nota (1-100)")
    grafico.show()
