import cmath

a = float(input('Digite o oeficiente a: '))
b = float(input('Digite o oeficiente b: '))
c = float(input('Digite o oeficiente c: '))

#Formula

delta = cmath.sqrt(b**2 - 4*a*c)
raiz1 = (-b + delta) / (2*a)
raiz2 = (-b - delta) / (2*a)

print(f'As raizes da equação quadrática são: {raiz1}, {raiz2}')

#Conversão dolar

dolares = float(input('Digite o valor em Dólares: '))
tava_conversao = float(input('Digite a conversão: '))

euros = dolares* tava_conversao
libras = dolares * 0.75

print(f'Em euros: {euros:.2f}')
print(f'Em Libras: {libras:.2f}')