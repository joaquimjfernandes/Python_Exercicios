# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# recebendo a data
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

# validando a data
if dia > 31 and mes > 12 and ano > 2024:
    print("Data Inválido")
elif (dia == 29 and mes == 2) and (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Ano Bissexto")
else:
    print("Data Inválida")

# mostrando a data
print('-'*15, f'\n {dia}/{mes}/{ano}')