import calendar

yy = 2024
mm = int(input("Mês[1 - 12]:"))
print('---'*8)

# Verificando os mês do Ano
if mm > 12:
    print('Valor Inválido! [1 - 12]')
else:
    print(calendar.month(yy,mm))