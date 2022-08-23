"""
Funções com parâmetro padrão
    - Em funções Python, os parâmetros com valores default DEVEM estar sempre
    no final da declaração;

#Errado

def exponencial(numero=2, potencia): # Valor padrão da potência é 2.

#Certo
def exponencial(numero, potencia=2): # Valor padrão da potência é 2.

-----

def exponencial(numero, potencia=2): # Valor padrão da potência é 2.
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(2))

"""



