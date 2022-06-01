"""
Tuplas (tuple)

Tuplas são parecidas com listas

Existem duas diferenças básicas

1- As tuplas são representadas por parenteses ()
2- As tuplas são imutáveis. Ao criar uma tupla, ela não muda. Toda operação em
uma tupla gera uma nova tupla.

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

----------------------------------------------------------------------

----------------------------------------------------------------------

----------------------------------------------------------------------

----------------------------------------------------------------------

----------------------------------------------------------------------

----------------------------------------------------------------------

"""


