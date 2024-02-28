# Função Simples:

def saudacao(nome):
    return f"Olá, {nome}!"
#Função com Parâmetros Padrão:

def potencia(base, expoente=2):
    return base ** expoente
#Função com Retorno Múltiplo:

def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

#EXEMPLO DE ESCOPO

def exemplo_escopo():
    variavel_local = 10
    print(variavel_local)

exemplo_escopo()  # Saída: 10
#print(variavel_local)  # Erro: variavel_local não está definida fora da função

#EXEMPLO DE FUNÇÃO

#resultado = nome_da_funcao(argumentos)

#Por exemplo:

def calcular_quadrado(numero):
    return numero ** 2

resultado = calcular_quadrado(5)
print(resultado)  # Saída: 25

#EXEMPLO DE RECURSIVIDADE

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120





