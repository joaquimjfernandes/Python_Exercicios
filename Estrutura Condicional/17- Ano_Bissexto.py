# Faça um Programa que peça um número correspondente a um determinado ano e em seguida
# informe se este ano é ou não bissexto.

# função para saber se o ano é bissexto
def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# recebendo o ano do usuário
ano = int(input("Em ano estamos: "))
# validando se é bissexto ou não
if ano_bissexto(ano):
    print(f'{ano} => Ano Bissexto')
else:
    print(f'{ano} => Não é Ano Bissexto')

# Chamando a função do Ano Bissexto
ano_bissexto(ano)
