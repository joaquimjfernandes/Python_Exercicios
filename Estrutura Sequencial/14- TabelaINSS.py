#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# Inicializando o programa
print( '-'*25,"\n  REAJUSTE SALARIAL\n",'-'*25)

# Recebendo dados
ganho_hora = int(input("Quanto ganhas por hora: "))
hora_trabalhada = int(input("Quantas horas trabalhas no mês: "))

print('-'*35)
# Calculando o total do Ganho Mensal
salario = ganho_hora * hora_trabalhada

# Descontando no Salário Bruto
imposto_renda = salario - (salario * 11 / 100)
inss = imposto_renda - (imposto_renda * 8 / 100)
sindicato = inss - (inss * 5 / 100)

# Salário Liquido
salario_liquido = sindicato

# Exibindo os Resultados
print(f"+ Salário Bruto: {salario:.2f}R$")
print(f"- Imposto de Renda (11%): {imposto_renda:.2f}R$")
print(f"- INSS (8%): {inss:.2f}R$")
print(f"- Sindicato (5%): {sindicato:.2f}R$")
print(f"= Salário Liquido: {salario_liquido:.2f}")

