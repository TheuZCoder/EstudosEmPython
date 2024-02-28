#EXEMPLO DE MÓDULOS

#Exemplo: Módulo Matemático (math):

import math

raiz_quadrada = math.sqrt(25)  # Calcula a raiz quadrada de 25
seno_30_graus = math.sin(math.radians(30))  # Calcula o seno de 30 graus convertidos para radianos
print(raiz_quadrada)
print(seno_30_graus)
#Exemplo: Módulo de Data e Hora (datetime):

from datetime import datetime

data_atual = datetime.now()  # Obtém a data e hora atual
ano_atual = data_atual.year  # Obtém o ano atual
print(data_atual)
print(ano_atual)

import operacoes

resultado_soma = operacoes.somar(5, 3)
resultado_subtracao = operacoes.subtrair(10, 4)
