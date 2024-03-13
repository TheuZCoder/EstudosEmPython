import pandas as pd
import matplotlib.pyplot as plt

data = {'nome': ['alice','bruno','carlos','denis'],
        'idade': [25,28,33,35],
        'cidade': ['A','B','C','D']}



df = pd.DataFrame(data)

# Acessando uma coluna por nome
coluna_idade = df['Idade']
print(coluna_idade)


# Selecionando linhas com base em uma condição
linha_filtro = df[df['Idade'] > 30]
print(linha_filtro)

#adicionando uma nova coluna
df['profissao'] = ['engenheiro', 'analista', 'designer', 'produtor']
print(df)

#grafico de barras da idade por nome
df.plot.bar(x='Nome', y='Idade')
plt.show()