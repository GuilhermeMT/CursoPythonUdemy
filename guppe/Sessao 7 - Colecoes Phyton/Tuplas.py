"""
Tuplas (tuple)

Tuplas são parecidas com listas, mas são mais rápidas. Tuplas deixam o código mais seguro,
pois os elementos são imutáveis.

Existem duas diferenças básicas

1- As tuplas são representadas por parenteses ()
2- As tuplas são imutáveis. Ao criar uma tupla, ela não muda. Toda operação em
uma tupla gera uma nova tupla.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

----------------------------------------------------------------------
# Cuidado1: As tuplas são representadas por (), mas veja

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6

print(tupla2)
print(type(tupla2))

# Cuidado2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é tupla!
print(tupla4)
print(type(tupla4))

----------------------------------------------------------------------
# Podemos gerar uma tupla dinamicamente usando o range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)

----------------------------------------------------------------------
# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python')
escola, curso = tupla

print(escola)
print(curso)

----------------------------------------------------------------------
tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla)) #Soma valores tupla
print(max(tupla))
print(min(tupla))
print(len(tupla))
----------------------------------------------------------------------
# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)

tupla1 = tupla1 + tupla2

print(tupla1)
----------------------------------------------------------------------
# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)
print(34 in tupla)
----------------------------------------------------------------------
# Iterando sobre uma tupla

tupla = (1, 2, 3, 4, 5)

for n in tupla:
    print(n)

print("Indice valor")
for indice, valor in enumerate(tupla):
    print(indice, valor)
----------------------------------------------------------------------
# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'd', 'd', 'e', 'f')

print(tupla.count('d'))
----------------------------------------------------------------------
# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar dados contidus numa coleção
# EX
meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
----------------------------------------------------------------------
"""



