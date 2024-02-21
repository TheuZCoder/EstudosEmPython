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
