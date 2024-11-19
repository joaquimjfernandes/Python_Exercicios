# Faça um Programa que leia três números e mostre-os em ordem decrescente.

v1 = int(input("Digite um Valor: "))
v2 = int(input("Digite outro Valor: "))
v3 = int(input("Digite outro Valor: "))

# Criando uma lista dos valores
valores = [v1, v2, v3]

# Sorteando os valores em ordem decrescente
valores.sort(reverse=True)

# Mostrando os valores na Ordem
print(f"Os Valores na ordem decrescente: {valores}")