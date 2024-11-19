# Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite o Primeiro Valor: "))
n2 = int(input("Digite o Segundo Valor: "))

# Recebendo o maior valor
maior = menor = 0
# Fazendo a Condição do Maior para Menor
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

# Mostrando o resultado na tela
print(f'O maior velor digitado é {maior} e o menor valor é {menor}')