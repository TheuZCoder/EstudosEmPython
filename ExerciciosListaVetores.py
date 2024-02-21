 #EXERCICIO1

# # Inicializa um vetor vazio
# vetor = []

# # Lê 5 números inteiros e os adiciona ao vetor
# for i in range(5):
#     numero = int(input(f"Digite o {i+1}º número inteiro: "))
#     vetor.append(numero)

# # Imprime os números do vetor
# print("Números digitados:")
# for num in vetor:
#     print(num)

#EXERCICIO 2

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Lê 10 números reais
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    numeros.append(numero)

# Imprime os números na ordem inversa
print("\nNúmeros na ordem inversa:")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])


