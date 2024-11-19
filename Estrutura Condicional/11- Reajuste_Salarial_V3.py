# As Organizações JF resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o novo salário, após o aumento.

# recebendo o salário de um funcionário
salario = float(input("Quanto você ganha: "))

#
novo_salario = valor_aumento = 0

# validando o salário segundo o critério
if salario <= 280000:
    novo_salario = salario + (salario * 20 / 100)
    valor_aumento = novo_salario - (novo_salario * 20 / 100)
elif salario >= 280000 < 700000:
    novo_salario = salario + (salario * 15 / 100)
elif salario >= 700000 < 1500000:
    novo_salario = salario + (salario * 10 / 100)
elif salario >= 1500000:
    novo_salario = salario + (salario * 5 / 100)

# mostrando salário reajustado
print('-'*35, '\n Tabela Salárial Reajustado')
print('-'*35,f'\n Salário Inicial: {salario}')
print(f'Salário Reajustado: {novo_salario}')

