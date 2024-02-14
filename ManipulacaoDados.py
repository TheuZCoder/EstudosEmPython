nome = "João"
idade = 30

# Usando f-strings
mensagem = f"Olá, {nome}! Você tem {idade} anos."

# Usando método format
outra_mensagem = "Olá, {}! Você tem {} anos.".format(nome, idade)

print(mensagem)
print(outra_mensagem)

#3. Métodos Adicionais:

texto = "   Python é incrível!   "

# Remover espaços em branco no início e no final
texto_trim = texto.strip()

# Converter para letras maiúsculas
texto_upper = texto.upper()

# Substituir parte do texto
texto_substituido = texto.replace("Python", "Java")

# Dividir a string em uma lista de palavras
lista_palavras = texto.split()

print(texto_trim)
print(texto_upper)
print(texto_substituido)
print(lista_palavras)

#4. Verificação e Manipulação:

email = "usuario@email.com"

# Verificar se a string é um e-mail
e_email = email.endswith(".com")

# Contar o número de ocorrências de uma letra
contagem_letra = texto.count("o")

# Encontrar a posição da palavra "incrível"
posicao_incrivel = texto.find("incrível")

print(e_email)
print(contagem_letra)
print(posicao_incrivel)

# 5. Concatenação:

nome = "Maria"
sobrenome = "Silva"

# Concatenar strings usando o operador '+'
nome_completo = nome + " " + sobrenome

# Concatenar usando o método join
lista_palavras = ["Python", "é", "incrível"]
frase_completa = " ".join(lista_palavras)

print(nome_completo)
print(frase_completa)


#Operadores Aritméticos:
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
potencia = a ** b

print(soma, subtracao, multiplicacao, divisao, divisao_inteira, resto, potencia)


