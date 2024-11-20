# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

# recebendo o valor do usuário
numero = int(input('Digite um número[saber se é Par ou Ímpar]: '))

if numero % 2 == 0:
    print(f'{numero} => é Par!')
else:
    print(f'{numero} => é Ímpar!')