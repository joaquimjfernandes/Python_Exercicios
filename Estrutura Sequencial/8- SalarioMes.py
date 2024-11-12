# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

ganhoHora = float(input("Quanto ganhas por hora: "))
numeroHoraMes = float(input("Quantas horas trabalhas no mês: "))

GanhoMensais = ganhoHora * numeroHoraMes

print(f"Total de Ganho Mensais: {GanhoMensais:2}")
