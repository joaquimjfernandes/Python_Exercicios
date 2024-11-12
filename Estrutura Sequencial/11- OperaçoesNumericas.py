# Faça um Programa que peça 2 números inteiros e um número real
# Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

# Recebendo Dados das Variáveis
n1 = int(input("Digite um número(I): "))
n2 = int(input("Digite outro número(I): "))
n3 = float(input("Digite um número(Real): "))

# dobro do primeiro valor
dobro_n1 = n1 * 2

# triplo do primeiro valor
triplo_n1 = n1 * 3

# metade do segundo valor
metade_n2 = n2 / 2

# triplo do terceiro valor
triplo_n3 = n3 * 3

print('-'*35)
print(f"O Resultado da primeira operação:{dobro_n1*metade_n2}")
print(f"A Soma da segunda operação:{triplo_n1+triplo_n3}")
print(f"O Resultado da ultima operação:{n3*3}")

