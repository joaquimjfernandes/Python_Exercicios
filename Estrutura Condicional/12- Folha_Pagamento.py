# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# iniciando o programa
print('-'*35, '\n       Folha de Pagamento ')
print('-'*35)

# recebendo valores das horas trabalhadas
valorHora = int(input("Digite o valor da sua hora de trabalho: "))
horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))

# calculando o salário bruto
salarioBruto = valorHora * horasTrabalhadas

# calculo do imposto de renda
if salarioBruto <= 900:
    impostoRenda = 0
elif salarioBruto <= 1500:
    impostoRenda = salarioBruto * 0.05
elif salarioBruto <= 2500:
    impostoRenda = salarioBruto * 0.10
else:
    impostoRenda = salarioBruto * 0.20

# sindicato
sindicato = salarioBruto * 0.03
# fgts
fgts = salarioBruto * 0.11

# desconto e salário liquido
totalDescontos = impostoRenda + sindicato
salarioLiquido = salarioBruto - totalDescontos

# mostrando os resultados
print(f"Salário Bruto: R$ {salarioBruto:2}")
print(f"(-) IR: R$ {impostoRenda:2}")
print(f"(-) Sindicato (3%): R$ {sindicato:2}")
print(f"FGTS (11%): R$ {fgts:2}")
print(f"Total de descontos: R$ {totalDescontos:2}")
print(f"Salário Líquido: R$ {salarioLiquido:2}")