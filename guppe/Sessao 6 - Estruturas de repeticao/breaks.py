"""
Saindo de loops com break

Utilizamos o break para sair de loops de maneira forçada ou de maneira projetada.
"""

# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)

