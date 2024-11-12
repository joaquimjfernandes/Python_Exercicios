# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
# maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos)deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa
# que você faça um programa que leia a variável peso (peso de peixes)e calcule
# o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
# na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

# Definindo as variáveis
peso_maior_estabelecido = 50
multa_por_quilo = 4

peso_peixe = float(input("Qual é o Peso do Peixe: "))

# Calculo do excesso de da multa
if peso_peixe > peso_maior_estabelecido:
    excesso = peso_peixe - peso_maior_estabelecido
    multa = excesso * multa_por_quilo
else:
    excesso = 0
    multa = 0

# Exibindo o resultado
print(f"Peso do Peixe: {peso_peixe}kg")
print(f"Excesso de Peso: {excesso}kg")
print(f"Valor da multa: {multa:.2f}R$")
