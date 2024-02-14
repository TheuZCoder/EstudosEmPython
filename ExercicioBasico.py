a = int(input('Digite um numero:'))
b = int(input('Digite o segundo Numero:'))


Soma = (a + b)
Subtração = (a - b)
Multiplicação = (a * b)
Divisão = (a / b)
Divisão_Inteira = (a // b)
Resto_Divisão = (a % b)
Potenciação = (a ** b)

raio = int(input('Digite o raio de circunferencia: '))
area_circulo = 3.14 * raio ** 2

print(f'A área do circulo com raio {raio} é: {area_circulo}')
print(Soma,Subtração,Multiplicação,Divisão,Divisão_Inteira,Resto_Divisão,Potenciação)

#Exercicio 2 
nome = 'matheus '
sobrenome = 'rodrigues'
Nome_Completo = nome + sobrenome

print(Nome_Completo)

textoUper = Nome_Completo.upper()
textoTrim = Nome_Completo.strip()
textoSub = Nome_Completo.replace('matheus','Fernanda')

print(textoTrim)
print(textoUper)
print(textoSub)

#Exercicio 3

cores = ['azul','vermelho','rosa']

cores.append('lilas')
cores.append('roxo')

print(cores)

coordenadas = (40.6543, -58.8759)
latitude, logitude = coordenadas

print(f'Latitude: {latitude} Longitude: {logitude}')

#Exercicio 4

tem_sol = True
tem_chuva = False

if tem_sol and not tem_chuva:
    print('É um dia agradável!')
else:
    print('Não é um dia agradável!')

#Exercicio 5
    
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))

if num1 % 2 == 0 and num2 % 2 == 0:
    print('Ambos são numeros pares')
else:
    print('Pelo menos um dos numeros não é par')

#Exercicio 6
    
numeros = [1,3,6,9,12,15]

for numero in numeros:
    if numero % 3 == 0 and numeros % 2 != 0:
        print(f'{numero} é multiplo de 3 e impar')


