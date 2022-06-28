"""
Mapas são conhecidos em Python como dicionários

São representados por {}

# Iterar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

    print(receita.keys())

for chave in receita.keys(): #Retorna as chaves do dicionário
    print(chave)

for valor in receita.values():
    print(valor)
"""

receita = {'jan': 100, 'fev': 200, 'mar': 300}

