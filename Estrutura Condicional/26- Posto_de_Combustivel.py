# posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de
# litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
# é R$ 2,50 o preço do litro do álcool é R$ 1,90.


tipo = str(input("Oque vai abastecer[A - G]: "))
if tipo in "Aa":
    # Litros do Alcool
    alcool = float(input("Quantos litros compraste: "))
    # Valor do Álcool
    valor_alcool = alcool * 1.90
    # Validando descontos do alcool
    if alcool <= 20:
        novo_valorA = valor_alcool - (valor_alcool * 3 / 100)
    elif alcool > 20:
        novo_valorA = valor_alcool - (valor_alcool * 5 / 100)
    print(f"Total a Pagar: {novo_valorA}")
elif tipo in "Gg":
    # Litros da Gasolina
    gasolina = float(input("Quantos litros compraste: "))
    # Valor do Álcool
    valor_gasolina = gasolina * 2.50

    # Validando desconto da gasolina
    if gasolina <= 20:
        novo_valorG = valor_gasolina - (valor_gasolina * 4 / 100)
    elif gasolina > 20:
        novo_valorG = valor_gasolina - (valor_gasolina * 6 / 100)

    print(f"Total a Pagar: {novo_valorG}")