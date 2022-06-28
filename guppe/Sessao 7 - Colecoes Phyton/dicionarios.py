"""
Dicionários

OBS: Em algumas linguagens, são conhecidos como mapas

Dicionários são coleções do tipo chave/valor e são representados por {}

OBS:
    - chave e valor são separados por dois pontos :
    - Tanto chave como valor podem ser de qualquer tipo
    - Podemos misturar tipo de dados

--------------------------------------------------------

# Criação de dicionários

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
--------------------------------------------------------
# Acessando elementos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 1 (Acessando via chave)

print(paises['br'])
print(paises['py'])

# OBS: Se a chave não existir, retornará um KeyError

# Forma 2 (acessando via get - recomendada)

print(paises.get('br'))
print(paises.get('ru'))
--------------------------------------------------------
# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Brasil' in paises)

if 'ru' in paises:
    russia = paises['ru']
--------------------------------------------------------
# Podemos utilizar qualquer tipo de dado (int, float, string, boolean, tupla, lista, dicionario) como
# chaves de dicionarios

# Tuplas são interessantes para serem usadas como chaves de dicionários
localidades = {
    (35.5456, 34.4432): 'Escritório em Tóquio',
    (12.5456, 3.4432): 'Escritório em São Paulo',
    (335.5456, 434.4432): 'Escritório em Nova York',
}
print(localidades)
--------------------------------------------------------
# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1 - mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)
--------------------------------------------------------
# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - mais comum

receita.pop('mar')
print(receita)

# Forma 2

del receita['fev']

print(receita)
--------------------------------------------------------
# Carrinho de compras de uma loja de eletrônicos
Carrinho de compras
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
# Utilizando listas
carrinho = []

produto1 = ['playstation 4', 1, 2300.00]
produto2 = ['god of war 4', 1, 250.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# Utilizando Tupla

produto1 = ('playstation 4', 1, 2300.00)
produto2 = ('god of war 4', 1, 250.00)

carrinho = (produto1, produto2)

print(carrinho)

# Utilizando dicionários

carrinho = []

produto1 = {'nome': 'Playstation4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of war', 'quantidade': 1, 'preco': 300.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Dessa forma, facilmente add ou removemos produtos do carrinho.
--------------------------------------------------------
# métodos de dicionários
# Limpar o dicionário

d.clear()
print(d)

# métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)

# Forma 1 - Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo['d']= 4

print(novo)
--------------------------------------------------------
"""


