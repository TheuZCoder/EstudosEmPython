# Crie uma lista de números inteiros e ordene-a em ordem crescente.
lista_numeros = [8, 3, 1, 6, 4, 7, 2, 9, 5, 10]
lista_numeros.sort()

# Adicione o número 10 ao final da lista.
lista_numeros.append(10)

# Remova o elemento de valor 5 da lista.
lista_numeros.remove(5)

print("Lista ordenada:", lista_numeros)
# Crie uma lista com os primeiros 10 números inteiros.
lista_inteiros = list(range(1, 11))

# Utilize o slicing para criar uma sublista com os números pares.
sublista_pares = lista_inteiros[1::2]

# Inverta a ordem da sublista criada.
sublista_pares.reverse()

print("Lista original:", lista_inteiros)
print("Sublista de números pares invertida:", sublista_pares)
# Crie uma lista aninhada com nomes de cores e códigos hexadecimais correspondentes.
lista_cores_codigos = [
    ["vermelho", "#FF0000"],
    ["verde", "#00FF00"],
    ["azul", "#0000FF"],
    ["amarelo", "#FFFF00"],
    ["roxo", "#800080"],
    # Adicione mais cores conforme necessário
]

# Acesse e imprima o código hexadecimal da cor "verde".
codigo_verde = None
for cor_codigo in lista_cores_codigos:
    if cor_codigo[0] == "verde":
        codigo_verde = cor_codigo[1]
        break

print("Código hexadecimal da cor verde:", codigo_verde)

# Crie uma tupla com os meses do ano.
meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

# Acesse os meses de janeiro a junho.
primeiros_meses = meses_do_ano[:6]

# Tente adicionar um novo mês à tupla e observe o resultado.
# Isso resultará em um erro, pois tuplas são imutáveis.
# meses_do_ano += ("Novo Mês",)

print("Meses de Janeiro a Junho:", primeiros_meses)

# Crie um dicionário onde as chaves são tuplas representando coordenadas (latitude, longitude) e os valores são nomes de cidades.
coordenadas_cidades = {
    (40.7128, -74.0060): "Nova York",
    (34.0522, -118.2437): "Los Angeles",
    # Adicione mais coordenadas conforme necessário
}

# Acesse e imprima o nome da cidade correspondente à coordenada (40.7128, -74.0060).
cidade_ny = coordenadas_cidades[(40.7128, -74.0060)]
print("Cidade correspondente à coordenada (40.7128, -74.0060):", cidade_ny)

# Crie dois conjuntos com números inteiros.
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# Realize a união, interseção e diferença entre esses conjuntos.
uniao = conjunto_a.union(conjunto_b)
intersecao = conjunto_a.intersection(conjunto_b)
diferenca = conjunto_a.difference(conjunto_b)

print("União dos conjuntos:", uniao)
print("Interseção dos conjuntos:", intersecao)
print("Diferença entre os conjuntos A e B:", diferenca)

# Crie uma lista com elementos duplicados.
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]

# Converta a lista para um conjunto para remover as duplicatas.
conjunto_sem_duplicatas = set(lista_com_duplicatas)

print("Lista original:", lista_com_duplicatas)
print("Lista sem duplicatas (como conjunto):", conjunto_sem_duplicatas)

# Crie um dicionário representando informações sobre um livro (título, autor, ano de publicação).
livro_info = {
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano_publicacao": 1954
}

# Adicione uma nova chave-valor ao dicionário representando a quantidade de páginas do livro.
livro_info["paginas"] = 1178

print("Informações do livro:", livro_info)

# Crie um dicionário com nomes de países e suas respectivas capitais.
paises_capitais = {
    "Brasil": "Brasília",
    "EUA": "Washington D.C.",
    "França": "Paris",
    # Adicione mais países conforme necessário
}

# Utilize um loop para imprimir cada país e sua capital.
print("Países e suas capitais:")
for pais, capital in paises_capitais.items():
    print(f"{pais}: {capital}")

# Crie um dicionário com pares chave-valor representando um inventário de produtos.
inventario = {
    "item1": 10,
    "item2": 5,
    "item3": 20
}

# Remova um item do inventário utilizando sua chave.
chave_remover = "item2"
if chave_remover in inventario:
    del inventario[chave_remover]

print("Inventário após a remoção:", inventario)
