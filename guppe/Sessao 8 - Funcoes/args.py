"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer.
- O *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Tuplas são imutáveis.



"""

# Exemplo


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros('oi', 3, [1, 2, 2, 1], {'a': 'amor', 'b': 'baixinhos'}))
