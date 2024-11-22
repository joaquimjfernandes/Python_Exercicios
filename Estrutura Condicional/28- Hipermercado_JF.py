# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#              Até 5 Kg        Acima de 5 Kg
# File Duplo  R$ 4,90 por Kg  R$ 5,80 por Kg
# Alcatra    R$ 5,90 por Kg  R$ 6,80 por Kg
# Picanha   R$ 6,90 por Kg  R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas
# um dos tipos de carne da promoção, porém não há limites para a quantidade
# de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
# ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o
# tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
# as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento
# valor do desconto e valor a pagar.

preco_file = preco_alcatra = preco_picanha = desconto_file =0
print('-'*55, '\n           HIPERMERCADO JF Importadora ')
print('-'*55)
print("""               Tabela de Produtos
[1] -> File Duplo           R$4,90/kg ==> R$ 5,80/kg
[2] -> Alcatra              R$5,90/kg ==> R$ 6,80/kg
[3] -> Picanha              R$6,90/kg ==> R$ 7,80""")
opcao = int(input("Oque deseja Comprar: "))

# Validando a compra
if opcao == 1:
    # quantidade do filé duplo
    quantidade_file = int(input("Quantidade do File Duplo: "))

    # quantidade do filé preço a pagar
    if quantidade_file <= 5:
        preco_file = quantidade_file * 4.90
    elif quantidade_file > 5:
        preco_file = quantidade_file * 5.80

    # mostrando resultado
    print('-'*55, '\nInformação da Compra: ')
    print(f"Carne: Filé Duplo => Quantidade: {quantidade_file} => Preço Total: {preco_file:2}")

if opcao == 2:
    # quantidade do Alcatra
    quantidade_alcatra = int(input("Quantidade de Alcatra: "))

    # preço total a pagar do alcatra
    if quantidade_alcatra <= 5:
        preco_alcatra = quantidade_alcatra * 5.90
    elif quantidade_alcatra > 5:
        preco_alcatra = quantidade_alcatra * 6.80

    # mostrando resultado
    print('-' * 55, '\nInformação da Compra: ')
    print(f"Carne: Filé Duplo => Quantidade: {quantidade_alcatra} => Preço Total: {preco_alcatra:2}")

if opcao == 3:
    # quantidade de picanha
    quantidade_picanha = int(input("Quantidade de Picanha: "))

    # preço total a pagar da Picanha
    if quantidade_picanha <= 5:
        preco_picanha = quantidade_picanha * 6.90
    elif quantidade_picanha > 5:
        preco_picanha = quantidade_picanha * 7.80

    # mostrando resultado
    print('-' * 55, '\nInformação da Compra: ')
    print(f"Carne: Filé Duplo => Quantidade: {quantidade_picanha} => Preço Total: {preco_picanha}")
