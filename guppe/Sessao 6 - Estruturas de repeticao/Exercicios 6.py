"""
EX 1
cont = 0
for multiplo in range(3, 50, 3):
    print(multiplo)
    cont += 1
    if cont == 5:
        break

EX 2
print("Loop for:")
for num in range(1, 100 + 1):
    print(num)

print("\nLoop While:")
cont = 0
while cont < 100:
    print(cont + 1)
    cont += 1

EX 3
cont = 10

while cont >= 0:
    print(cont)
    cont -= 1

print('Fim!')

EX 4
num = 0
while num < 100000:
    num += 1000
    print(num)

EX 8
menor = 0
maior = 0

for num in range(0, 10):
    valor = int(input("Digite um valor:"))

    if num == 0:
        menor = valor
        maior = valor

    if valor < menor:
        menor = valor
    elif valor > maior:
        maior = valor

print('Maior valor: ', maior)
print('Menor valor: ', menor)

EX 23
numero = int(input('Digite um número inteiro:'))

for num in range(numero, 0, -1):
    if numero % num == 0: # Verifica se o resto '%' da divisão é igual à 0
        print(num)
"""

