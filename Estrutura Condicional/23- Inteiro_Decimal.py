# Faça um Programa que peça um número e informe se o número é inteiro ou extradecimal.
# Dica: utilize uma função de arredondamento.

numero = float(input("Digite um número: "))

if round(numero) == numero:
    print(f"{numero} => é Inteiro")
else:
    print(f"{numero} => é Decimal")