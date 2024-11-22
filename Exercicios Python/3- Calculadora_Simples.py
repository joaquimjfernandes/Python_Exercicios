# Calculadora Básica
print("    CALCULADORA BÁSICA    ")
print('---'*10)
# recebendo os valores para fazer as operações
numero1 = int(input("Digite um Valor: "))
numero2 = int(input("Digite outro Valor: "))

# Operadores Aritméticos
# 1 + 1 = 2    # 9 // 2 = 4 [Tarefa: adicionar mais esses 3 Operações]
# 2 - 1 = 1    # 10 % 3 = 1
# 3 * 2 = 6    # 15 ** 2 = 225
# 8 / 4 = 2    # Binario <==> Hexadecimal


while True:
    # desenhando o menu de operações
    print('---'*10)
    print('      Menu de Operações ')
    print('---'*10)
    print("""[0] => Adicionar novos valores
[1] => Adição
[2] => Subtração
[3] => Divisão
[4] => Multiplicação
[5] => Binário
[6] => Hexadecimal
[7] => Sair do Programa""")
    # escolher operação para fazer
    escolha = int(input("Qual Operação Fazer: "))
    if escolha == 0:
        # adicionando novos valores
        numero1 = int(input("Digite um Valor: "))
        numero2 = int(input("Digite outro Valor: "))
    # botando para a calculadora funcionar
    elif escolha == 1:
        print('---' * 10)
        print('     Sala de Operações \n            ADIÇÃO')
        print('---' * 10)
        # fazendo a soma dos valores
        soma = (numero1 + numero2)
        print(f'{numero1} + {numero2} = {soma}')
    elif escolha == 2:
        print('---' * 10)
        print('     Sala de Operações \n          SUBTRAÇÃO')
        print('---' * 10)
        # fazendo a subtração dos valores
        subtracao = (numero1 - numero2)
        print(f'{numero1} - {numero2} = {subtracao}')
    elif escolha == 3:
        print('---' * 10)
        print('     Sala de Operações \n          DIVISÃO')
        print('---' * 10)
        # fazendo a divisão dos valores
        divisao = (numero1 / numero2)
        print(f'{numero1} / {numero2} = {divisao:2}')
    elif escolha == 4:
        print('---' * 10)
        print('     Sala de Operações \n       MULTIPLICAÇÃO')
        print('---' * 10)
        # fazendo a multiplicação dos valores
        multiplicacao = (numero1 * numero2)
        print(f'{numero1} * {numero2} = {multiplicacao}')
    elif escolha == 5:
        print('---' * 10)
        print('     Sala de Operações \n           Binário')
        print('---' * 10)
        # fazendo a mudança dos valores para binário
        binario = bin(numero1)
        binario2 = bin(numero2)
        print(f'Inteiros: {numero1} <=> Binário: {binario}')
        print(f'Inteiros: {numero2} <=> Binário: {binario2}')
    elif escolha == 6:
        print('---' * 10)
        print('     Sala de Operações \n           Binário')
        print('---' * 10)
        # fazendo a mudança dos valores para hexadecimal
        extradecimal= hex(numero1)
        extradecimal2= hex(numero2)
        print(f'Inteiros: {numero1} <=> Hexadecimal: {extradecimal}')
        print(f'Inteiros: {numero2} <=> Hexadecimal: {extradecimal2}')
    elif escolha > 6:
        print('SAINDO DA CALCULADORA...')
        break
