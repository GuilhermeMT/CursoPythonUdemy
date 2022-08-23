"""
Faça uma função que receba a data atual (dia, mês e ano em INTEIRO) e exiba=a na tela
no formato textual por extenso.

Exemplo:
01/01/2000, imprimir 1 de janeiro de 2000

Resolução:

meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
         7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

dt = input('Digite uma data no formato xx/xx/xxxx: ')
dt = dt.split('/')
dia = int(dt[0])
mes = int(dt[1])
ano = int(dt[2])

if dia <= 0 or dia > 31:
    print("O dia deve estar entre 1 e 31")
elif mes <= 0 or mes > 12:
    print("O mes deve estar entre 1 e 12")
else:
    print(str(dia) + ' de ' + str(meses[mes]) + ' de ' + str(ano))


"""
