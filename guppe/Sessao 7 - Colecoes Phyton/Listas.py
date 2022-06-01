"""
Listas

Listas em python funcionam como vetores/matrizes (arrays), com a diferença de serem
dinâmicos e podermos colocar QUALQUER tipo de dado.

Linguagens C/JAVA: arrays
    - Possuem tamanho e tipo de dado fixo .
    -

- Dinâmico: Não possui tamanho fixo.
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo, podemos colocar qualquer tipo de dado.

As listas em python são representadas entre colchetes: []

---------------------------------------
lista1 = [1, 2, 1, 1, 1, 43, 433, 2, 45, 7, 8, 455]
lista2 = ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']
lista3 = []
lista4 = list(range(20))
lista5 = list('Geek University')

---------------------------------------
# Podemos checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

---------------------------------------
# Podemos facilmente ordenar uma lista
lista5.sort()
print(lista5)

---------------------------------------
# Podemos contar o número de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

---------------------------------------
# Adicionar elementos em listas
Para adicionar elementos em listar, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# lista1.append(1,2,3) ERRO
# OBS: Com append só conseguimos adicionar um elemento por vez

lista1.append([1, 2, 3, 4, 5])  # Coloca a lista como elemento único - sublista
print(lista1)

if [1, 2, 3, 4, 5] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 88])  # Coloca cada elemento da lista como valor adicionar à lista
print(lista1)

---------------------------------------
# Podemos ter um novo elemento na lista informando a posição do índice.
# OBS: Isso não substitui o valor da posição de index, o mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

---------------------------------------
# Podemos juntar 2 listas

lista6 = lista1 + [1 , 2, 2 ,2 ,2 ]
lista6 += ['carai borracha']
print(lista6)

---------------------------------------
# Podemos inverter uma lista utilizando reverse()
lista1.reverse()
lista2.reverse()

# Forma 1
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])

---------------------------------------
# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

---------------------------------------
# Contar quantidade de elementos numa lista
print(len(lista2))

---------------------------------------
# Podemos remover facilmente o último elemento da lista
# O pop remove e retorna o último elemento
print(lista5)
lista5.pop()
print(lista5)

---------------------------------------
# Podemos remover um elemento pelo índice
lista5.pop(2)
print(lista5)

---------------------------------------
# Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

---------------------------------------
# Podemos repetir elementos em uma lista
nova = [1, 2, 3, 4]
print(nova)
nova = nova * 3
print(nova)

---------------------------------------
# Podemos converter uma string para uma lista
# Ex1
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas

# Ex 2
curso = 'Programação,em,python:,essencial'
curso = curso.split(',')
print(curso)

---------------------------------------
# Converter lista em String
lista6 = ['Programação', 'Em', 'Python', 'Essencial']
print(lista6)
curso = ' '.join(lista6) # Pega a lista6, coloca espaço entre os elementos e coloca em uma string
print(curso)

---------------------------------------
# Iterando sobre listas
# Exemplo 1 - for
for elemento in lista1:
    print(elemento)

#Exemplo 2 - While
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto ou digite 'Sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

---------------------------------------
# Utilizando variáveis em listas
num1 = 1
num2 = 2
num3 = 3
numeros = [num1, num2, num3]
print(numeros)

---------------------------------------
# Fazemos acesso aos elementos de forma indexada
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazemos acesso aos elementos de forma indexada INVERSA
print('Inverso:')
print(cores[0])
print(cores[-1])
print(cores[-2])
print(cores[-3])

---------------------------------------
for cor in cores:
    print(cor)

indice = 0

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

---------------------------------------
# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

---------------------------------------

---------------------------------------

---------------------------------------
"""

# Revisão Slicing
# Lista[inicio:fim:passo]

# Trabalhando com o slice de lista com o parametro 'inicio

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com o slice de lista com o parametro 'Fim'


