"""
Conjuntos
    - Estamos fazendo referência à teoria dos conjuntos em matemática.
    - Em python, os conjuntos são chamados de Sets.
    - Sets não possuem valores duplicados, ordenados.
    - Elementos não são acessados via índice, não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas
não nos importamos com a ordenação deles, chaves ou valores duplicados.

Os conjuntos são referenciados com chaves {}

Diferença entre conjuntos (sets) e dicionários (maps):
    - Um dicionário tem chave/valor;
    - Um conjunto tem valor;
"""

# Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 1, 33, 6, 76, 356})

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja add um valor já existente, o mesmo será ignorado
# sem gerar erros e não fará parte do conjunto.

# Forma 2 - mais comum

s = {1, 2, 3, 3, 4, 5, 5, 6}

print(s)
print(type(s))