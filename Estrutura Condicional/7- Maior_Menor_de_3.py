# Faça um Programa que leia três números e mostre o maior e o menor deles

# recebendo os valores
v2 = int(input("Digite um valor: "))
v3 = int(input("Digite outro valor: "))
v1 = int(input("Digite outro valor: "))

# maior e menor valor
maior = menor = 0

# v1 -> maior = v2 -> maior = v3 -> maior
if v1 > v2 and v1 > v3:
    maior = v1
elif v2 > v1 and v2 > v3:
    maior = v2
elif v3 > v1 and v3 > v2:
    maior = v3

# v1 -> menor = v2 -> menor = v3 -> menor
if v1 < v2 and v1 < v3:
    menor = v1
elif v2 < v1 and v2 < v3:
    menor = v2
elif v3 < v1 and v3 < v2:
    menor = v3

# Mostrando o resultado
print(f"O Maior Valor: {maior} => O Menor Valor: {menor}")