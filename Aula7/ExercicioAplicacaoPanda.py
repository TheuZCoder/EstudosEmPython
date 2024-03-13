import pandas as pd
import yaml
import matplotlib.pyplot as plt


# Carregar os dados dos funcionários a partir do arquivo YAML
with open('Aula7/dados_funcionarios.yaml', 'r') as file:
    dados_yaml = yaml.safe_load(file)


# Converter para DataFrame
df = pd.DataFrame(dados_yaml['funcionarios'])

# 1. Analise Exploratoria

# print('1. Analise Exploratoria:')
# print(df.head())
# print('=================')
# print(df.info())
# print('=================')
# print(df.describe())
# print('=================')
# print('2. Seleção e filtragem de dados')
# funcionarios_acima_dos_30 =df[df['idade'] > 30]
# print('funcionario com mais de 30 anos')
# print(funcionarios_acima_dos_30)
# funcionarios_salario_acima_4000 = df[df['salario'] > 4000]
# print('funcionarios com salario acima de 4000')
# print(funcionarios_salario_acima_4000)
#3. manipulação de dados

# print('3. manipulação de dados')
# df['salario_ajustado'] = df['salario'] * 1.10 #criado nova coluna salario_ajustado e multiplicado salario por 1.10
# print(df)

# print('4. agregação de dados')
# salario_medio = df['salario'].mean()
# print(f'salario medio dos funcionarios antes do ajuste:, {salario_medio: .2f}')

# salario_medio =df['salario_ajustado'].mean()
# print(f'salario medio dos funcionarios depois do ajuste, {salario_medio: .2f}')

# idade_media = df['idade'].mean()
# print(f'idade media dos funcionarios, {idade_media: .2f}')

# cria um Arquivo CSV com o dataFrame
df.to_csv('dados_funcionarios.csv', index=False)
# 5. Visualização de Dados
print("\n5. Visualização de Dados:")
plt.hist(df['idade'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Distribuição de Idades dos Funcionários')
plt.show()


plt.scatter(df['idade'], df['salario'], color='green')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Idade vs Salário dos Funcionários')
plt.show()
