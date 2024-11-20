# Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print('-'*35, '\n CAIXA ELETRÔNICO JF BANKS')
print('-'*35)



def caixa_eletronico():
    # Notas disponíveis
    notas = [100, 50, 10, 5, 1]

    # Solicita o valor do saque
    valor_saque = int(input("Digite o valor do saque (mínimo R$ 10 e máximo R$ 600): "))

    # Verifica se o valor está dentro dos limites
    if valor_saque < 10 or valor_saque > 600:
        print("Valor inválido! O valor deve estar entre R$ 10 e R$ 600.")
        return

    # Dicionário para armazenar a quantidade de cada nota
    quantidade_notas = {}

    # Calcula a quantidade de notas
    for nota in notas:
        if valor_saque >= nota:
            quantidade = valor_saque // nota  # Quantidade de notas dessa denominação
            quantidade_notas[nota] = quantidade  # Armazena a quantidade
            valor_saque -= quantidade * nota  # Atualiza o valor restante

    # Exibe o resultado
    print("Notas fornecidas:")
    for nota, quantidade in quantidade_notas.items():
        print(f"{quantidade} nota(s) de R$ {nota}")


# Chama a função
caixa_eletronico()
