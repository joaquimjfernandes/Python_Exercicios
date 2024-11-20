# ma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg           Acima de 5 Kg
# Morango ⇒ R$ 2,50 por Kg => R$ 2,20 por Kg
# Maçã ⇒ R$ 1,80 por Kg => R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

total_pagar = morango_preco = maca_preco = 0

# Informações do morango
numero_morango = int(input("Quantos kg de Morango compraste: "))
preco_morango = 2.50 # 2.20

# Validando o preço do Morango
if numero_morango <= 5:
    morango_preco = preco_morango * numero_morango
elif numero_morango > 5:
    morango_preco = preco_morango * numero_morango

# Informações da maçã
numero_maca = int(input("Quantos kg de Maçã compraste: "))
preco_maca = 1.80 # 1.50

# Validando o preço da maça
if numero_maca <= 5:
    maca_preco = preco_maca * numero_maca
elif numero_maca > 5:
    maca_preco = preco_maca * numero_maca

# Total a Pagar pelas Compras
total_pagar = morango_preco + maca_preco
if (numero_morango > 8) and (numero_maca > 8) or total_pagar > 25.00:
    total_pagar = total_pagar - (total_pagar * 10 / 100)

print(f"Preço dos Morangos: {morango_preco:2}")
print(f"Preço das Maçãs: {maca_preco:2}")
print(f"Total a Pagar: {total_pagar:2}")
