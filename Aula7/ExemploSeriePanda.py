import pandas as pd


serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

#indexação e fatiamento:

#acessando elementos por indice
value_at_b = serie['b']
print(value_at_b)

#fatiando a serie
slice_of_series = serie[1:3]
print(slice)

#operações matematicas
dobro = serie * 2
print("série multiplicada por 2")
print(dobro)

#filtrando dados
maior_que_30 = serie[serie>30]
print("elementos maiores que 30")
print(maior_que_30)

#operações estatisticas