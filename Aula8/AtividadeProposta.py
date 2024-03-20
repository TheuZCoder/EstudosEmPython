import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml

with open('empresa.yaml', 'r') as file:
    dados = yaml.safe_load(file)

df_vendas = pd.DataFrame(dados['vendas'])
df_clientes = pd.DataFrame(dados['comportamento_do_cliente'])
df_produtos = pd.DataFrame(dados['desempenho_do_produto'])



# Gráfico de barras para o desempenho de vendas por cliente
plt.figure(figsize=(10, 6))
sns.barplot(x='cliente_id', y='preco_unitario', data=df_vendas, estimator=sum)
plt.title('Desempenho de Vendas por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Valor gasto total pelo cliente')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

df_merged = pd.merge(df_vendas, df_clientes, left_on='cliente_id', right_on='id', how='left')

# Gráfico de dispersão para relacionar os IDs dos clientes com a idade dos clientes que fizeram vendas
plt.figure(figsize=(10, 6))
plt.scatter(df_merged['id_y'], df_merged['idade'], alpha=0.5)
plt.title('Relação entre IDs dos Clientes e Idade dos Clientes que Fizeram Vendas')
plt.xlabel('ID do Cliente')
plt.ylabel('Idade do Cliente')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

df_merged['valor_gasto_total'] = df_merged['quantidade'] * df_merged['preco_unitario']

# Gráfico de dispersão idade vs valor_gasto_total
plt.figure(figsize=(10, 6))
sns.scatterplot(x='idade', y='valor_gasto_total', data=df_merged)
plt.title('Relação entre Idade e Valor Gasto Total por Cliente')
plt.xlabel('Idade')
plt.ylabel('Valor Gasto Total')
plt.grid(True)
plt.show()