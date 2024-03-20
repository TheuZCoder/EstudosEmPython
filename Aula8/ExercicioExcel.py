import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo XLSX
df = pd.read_excel('Pasta1.xlsx')

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Nome'], df['Duracao'], alpha=0.5)
plt.title('Gráfico de Dispersão da Duração de Filmes')
plt.xlabel('Duração (minutos)')
plt.ylabel('Outra coluna (opcional)')
plt.xticks(rotation=45)  
plt.grid(True)
plt.tight_layout()  
plt.show()

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Nome'], df['Avaliacao'], alpha=0.5)
plt.title('Gráfico de Avalaiação dos Filmes')
plt.xlabel('Nome dos Filmes')
plt.ylabel('Avaliação')
plt.xticks(rotation=45)  
plt.grid(True)
plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Nome'], df['Ano'], marker='o')  # Substitua 'Data' e 'Valor' pelas colunas apropriadas
plt.title('Gráfico de Linhas do Valor ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.xticks(rotation=45)  
plt.grid(True)
plt.tight_layout()  
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Nome', y='Ano', data=df)  # Substitua 'Categoria' e 'Valor' pelas colunas apropriadas
plt.title('Boxplot do Valor por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.xticks(rotation=45)  
plt.grid(True)
plt.tight_layout() 
plt.show()