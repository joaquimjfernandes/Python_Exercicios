# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

# variáveis principais
preco_prod1 = float(input("Preço do Primeiro Produto[teclado]: "))
preco_prod2 = float(input("Preço do Segundo Produto[pendrive]: "))
preco_prod3 = float(input("Preço do Terceiro Produto[modem]: "))

# variáveis que receberam decisões
mais_alto = mais_barato = 0

# Comparando preços dos produtos mais alto
if preco_prod1 > preco_prod2 and preco_prod1 > preco_prod3:
    mais_alto = preco_prod1
elif preco_prod2 > preco_prod1 and preco_prod2 > preco_prod3:
    mais_alto = preco_prod2
elif preco_prod3 > preco_prod1 and preco_prod3 > preco_prod2:
    mais_alto = preco_prod3

# Achando preços dos produtos mais baixo
if preco_prod1 < preco_prod2 and preco_prod1 < preco_prod3:
    mais_barato = preco_prod1
elif preco_prod2 < preco_prod1 and preco_prod2 < preco_prod3:
    mais_barato = preco_prod2
elif preco_prod3 < preco_prod1 and preco_prod3 < preco_prod2:
    mais_barato = preco_prod3

# Mostrando o resultado
print('-'*35)
print(f"Produto Mais Alto: {mais_alto} => Produto Mais Barato: {mais_barato}")
print(f"Produto para comprar é o que custa: {mais_barato}")
