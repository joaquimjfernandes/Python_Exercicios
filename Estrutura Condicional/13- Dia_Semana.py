# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# recebendo o dia da semana
n = int(input("Digite um número para saber o dia da semana[1-7]: "))

# validando a referência
if n == 1:
    print('Domingo')
elif n == 2:
    print('Segunda-Feira')
elif n == 3:
    print('Terça-Feira')
elif n == 4:
    print('Quarta-Feira')
elif n == 5:
    print('Quinta-Feira')
elif n == 6:
    print('Sexta-Feira')
elif n == 7:
    print('Sábado')
else:
    print('Dia inválido!')