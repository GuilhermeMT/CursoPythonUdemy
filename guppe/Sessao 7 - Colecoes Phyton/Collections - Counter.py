"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista e como valor
a quantidade de ocorrências desse elemento.

# Exemplo 1
lista = [1, 2, 3, 3, 5, 2, 1, 2, 2, 1, 5, 8, 10, 10, 10, 1, 1, 1, 2, 3, 3, 5, 5, 6, 10, 11, 11, 11, 11]

# Counter retorna
res = Counter(lista)

print(type(res))
print(res)

"""

from collections import Counter


#Exemplo 2

texto = 'Tanguar Haor é um ecossistema único de zonas úmidas no nordeste de Bangladesh de' \
        ' importância nacional e ganhou destaque internacional. A área de Tanguar Haor,' \
        ' incluindo 46 aldeias dentro dele, é de cerca de 100 quilômetros quadrados. É a ' \
        'fonte de subsistência para mais de 40 mil pessoas. Todo inverno, o haor abriga ' \
        'cerca de 200 tipos de aves migratórias. Existem mais de 140 espécies de peixes de' \
        ' água doce no haor. Bangladesh declarou-a uma Área Ecologicamente Crítica em 1999,' \
        ' considerando sua condição como resultado da superexploração de seus recursos naturais.'

palavras = texto.split()
res = Counter(texto)
print(res.most_common(5))
