# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# Iniciando o programa
# print('-'*35, "\n       Loja de Tintas - JFK\n",'-'*35)
# print("""[1] - Comprar Latas de 18 Litros
# [2] - Comprar Galões de 3,6 Litros
# [3] - Misturar Lata e Galão
# [4] - Sair do Programa """)
# opcao = int(input("Como prefere Comprar os Litros: "))

area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
# Acrescentar 10% de folga
area_com_folga = area * 1.1

# Quantidade de litros necessários
litros_necessario = area_com_folga / 3

# Apenas latas de 18 litros
latas_18 = math.ceil(litros_necessario / 18)
preco_latas = latas_18 * 80

# Apenas galões de 3,6 litros
galoes_3 = math.ceil(litros_necessario / 3.6)
preco_galoes = galoes_3 * 25

# Mistura das latas e galões
lata_misto = int(litros_necessario // 18) # Quantidade máxima
resto = litros_necessario - (lata_misto * 18) # Resto após latas

# Quantidade de galões de 3,6L
galoes_misto = math.ceil(resto/ 3.6)
preco_misto = (latas_18 * 80) + (galoes_3 * 25)

# Mostrando o resultado
print(f"Quantidade de latas: {latas_18}")
print(f"Preço total: R$ {preco_latas:.2f}")
print('-'*35)
print(f"Quantidade de galões: {galoes_3}")
print(f"Preço total: R$ {preco_galoes:.2f}")
print('-'*35)
print(f"Quantidade de latas de 18 litros: {lata_misto}")
print(f"Quantidade de galões de 3,6 litros: {galoes_misto}")
print(f"Preço total: R$ {preco_misto:.2f}")
