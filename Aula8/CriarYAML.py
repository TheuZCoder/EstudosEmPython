import numpy as np  # Importar a biblioteca NumPy
import pandas as pd  # Importar a biblioteca Pandas
import matplotlib.pyplot as plt  # Importar a biblioteca Matplotlib
import seaborn as sns
import yaml  # Importar a biblioteca Seaborn


# Gerar dados aleatórios
np.random.seed(0)  # Definir a semente do gerador de números aleatórios do NumPy
x = np.random.randn(100)  # Gerar 100 números aleatórios com distribuição normal (média 0 e desvio padrão 1) para o eixo x
y = np.random.randn(100)  # Gerar 100 números aleatórios com distribuição normal (média 0 e desvio padrão 1) para o eixo y


# Criar DataFrame com os dados gerados
df = pd.DataFrame({'X': x, 'Y': y})  # Criar um DataFrame do Pandas com duas colunas 'X' e 'Y' contendo os dados gerados


# Plotar gráfico de dispersão com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho 8x6 polegadas
plt.scatter(df['X'], df['Y'], color='blue', alpha=0.5)  # Plotar um gráfico de dispersão com os dados do DataFrame
plt.title('Gráfico de Dispersão - Matplotlib')  # Definir o título do gráfico
plt.xlabel('X')  # Definir o rótulo do eixo x
plt.ylabel('Y')  # Definir o rótulo do eixo y
plt.grid(True)  # Habilitar a grade no gráfico
plt.show()  # Mostrar o gráfico


# Plotar gráfico de dispersão com Seaborn
plt.figure(figsize=(8, 6))  # Criar uma nova figura com tamanho 8x6 polegadas
sns.scatterplot(data=df, x='X', y='Y', color='red', alpha=0.5)  # Plotar um gráfico de dispersão com Seaborn usando os dados do DataFrame
plt.title('Gráfico de Dispersão - Seaborn')  # Definir o título do gráfico
plt.xlabel('X')  # Definir o rótulo do eixo x
plt.ylabel('Y')  # Definir o rótulo do eixo y
plt.grid(True)  # Habilitar a grade no gráfico
plt.show()  # Mostrar o gráfico




# Dados fictícios
dados = {
    'alunos': ['Joao', 'Maria', 'Pedro', 'Ana', 'Carla'],
    'notas': [8, 7, 9, 6, 8],
    'idade': [20, 22, 21, 19, 20],
    'altura': [1.75, 1.65, 1.80, 1.70, 1.68]
}


# Salvar os dados em um arquivo YAML
with open('dados.yaml', 'w') as file:
    yaml.dump(dados, file)


print("Arquivo YAML criado com sucesso!")








# Carregar dados do arquivo YAML
with open('dados.yaml', 'r') as file:
    dados = yaml.safe_load(file)


# Criar DataFrame com os dados
df = pd.DataFrame(dados)


# Plotar histograma da idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
plt.hist(df['idade'], bins=5, color='skyblue', edgecolor='black')  # Plotar histograma
plt.title('Histograma da Idade - Matplotlib')  # Definir título do gráfico
plt.xlabel('Idade')  # Definir rótulo do eixo x
plt.ylabel('Frequência')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico


# Plotar gráfico de barras das notas com Seaborn
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
sns.barplot(data=df, x='alunos', y='notas', palette='pastel')  # Plotar gráfico de barras com Seaborn
plt.title('Gráfico de Barras das Notas - Seaborn')  # Definir título do gráfico
plt.xlabel('Alunos')  # Definir rótulo do eixo x
plt.ylabel('Notas')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico


# Plotar gráfico de dispersão da altura e idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
plt.scatter(df['altura'], df['idade'], color='green', alpha=0.5)  # Plotar gráfico de dispersão
plt.title('Gráfico de Dispersão da Altura e Idade - Matplotlib')  # Definir título do gráfico
plt.xlabel('Altura')  # Definir rótulo do eixo x
plt.ylabel('Idade')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico


# Plotar gráfico de dispersão da altura e idade com Seaborn
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
sns.scatterplot(data=df, x='altura', y='idade', color='purple', alpha=0.5)  # Plotar gráfico de dispersão com Seaborn
plt.title('Gráfico de Dispersão da Altura e Idade - Seaborn')  # Definir título do gráfico
plt.xlabel('Altura')  # Definir rótulo do eixo x
plt.ylabel('Idade')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico









# Dados para o primeiro gráfico de linha
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 20]


# Plotar gráfico de linha
plt.plot(x, y)  # Plotar gráfico de linha usando os dados x e y
plt.title('Gráfico de Linha')  # Definir título do gráfico
plt.xlabel('X')  # Definir rótulo do eixo x
plt.ylabel('Y')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico


# Dados para o segundo gráfico de barra
categorias = ['A', 'B', 'C', 'D']
valores = [20, 35, 30, 25]


# Plotar gráfico de barra
plt.bar(categorias, valores)  # Plotar gráfico de barra usando os dados de categorias e valores
plt.title('Gráfico de Barra')  # Definir título do gráfico
plt.xlabel('Categorias')  # Definir rótulo do eixo x
plt.ylabel('Valores')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico


# Dados para o terceiro histograma
dados = np.random.normal(loc=0, scale=1, size=1000)


# Plotar histograma
plt.hist(dados, bins=30)  # Plotar histograma dos dados com 30 bins
plt.title('Histograma')  # Definir título do gráfico
plt.xlabel('Valores')  # Definir rótulo do eixo x
plt.ylabel('Frequência')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico


# Dados para o quarto gráfico de dispersão
x = np.random.randn(100)
y = np.random.randn(100)


# Plotar gráfico de dispersão
plt.scatter(x, y)  # Plotar gráfico de dispersão usando os dados x e y
plt.title('Gráfico de Dispersão')  # Definir título do gráfico
plt.xlabel('X')  # Definir rótulo do eixo x
plt.ylabel('Y')  # Definir rótulo do eixo y
plt.show()  # Mostrar o gráfico


# Dados
dados = np.random.normal(loc=0, scale=1, size=1000)


# Plotar histograma com KDE
sns.histplot(dados, kde=True)
plt.title('Histograma com KDE')
plt.xlabel('Valores')
plt.ylabel('Densidade')
plt.show()


# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [20, 35, 30, 25]


# Plotar gráfico de barras categóricas
sns.barplot(x=categorias, y=valores)
plt.title('Gráfico de Barras Categóricas')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()




# Dados
dados = sns.load_dataset('iris')


# Plotar box plot
sns.boxplot(x='species', y='sepal_length', data=dados)
plt.title('Box Plot')
plt.xlabel('Espécies')
plt.ylabel('Comprimento da Sépala')
plt.show()


# Dados
dados = sns.load_dataset('iris')


# Plotar violin plot
sns.violinplot(x='species', y='sepal_length', data=dados)
plt.title('Violin Plot')
plt.xlabel('Espécies')
plt.ylabel('Comprimento da Sépala')
plt.show()














