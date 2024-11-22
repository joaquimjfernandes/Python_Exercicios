# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

print('-'*35, '\n OPERAÇÕES ARITMÉTICAS ')
print('-'*35)

# recebendo os valores
v1 = float(input("Primeiro Valor: "))
v2 = float(input("Segundo Valor: "))

print("""Tabela de Operações
[1] - Par ou Ímpar
[2] - Positivo ou Negativo
[3] - Inteiro ou Decimal
[4] - Sair do Programa
""")
opcao = int(input("Qual Operação Fazer: "))
print('-'*35)

# Par ou Ímpar
if opcao == 1:
    print('Par ou Ímpar \n', '-'*35)
    if v1 % 2 == 0 and v2 % 2 == 0:
        print(f'Os valores {v1} e {v2} são Pares')
    elif v1 % 2 == 1 and v2 % 2 == 1:
        print(f'Os valores {v1} e {v2} são ÍMPARES')
    elif v1 % 2 == 0 and v2 % 2 == 1:
        print(f"O valor {v1} => é PAR ==> E o valor {v2} => é Ímpar")
    elif v2 % 2 == 0 and v1 % 2 == 1:
        print(f"O valor {v1} => é Ímpar ==> E o valor {v2} => é PAR")

# Positivo ou Negativo
elif opcao == 2:
    print('POSITIVO ou NEGATIVO')
    if v1 > 0 and v2 > 0:
        print(f'Os Valores {v1} e {v2} são POSITIVOS')
    elif (v1 > 0) and (v2 < 0):
        print(f'O valor {v1} => POSITIVO ==> E o Valor {v2} => NEGATIVO')
    elif (v1 < 0) and (v2 > 0):
        print(f'O valor {v1} => NEGATIVO ==> E o Valor {v2} => POSITIVO')

# Inteiro ou Decimal
elif opcao == 3:
    print('Inteiro ou Decimal')
    if round(v1) == v1:
        print(f"{v1} => é Inteiro")
    else:
        print(f"{v1} => é Decimal")
    if round(v2) == v2:
        print(f"{v1} => é Inteiro")
    else:
        print(f"{v2} => é Decimal")

# Sair do Programa
elif opcao == 4:
    print('Saindo do Programa...')