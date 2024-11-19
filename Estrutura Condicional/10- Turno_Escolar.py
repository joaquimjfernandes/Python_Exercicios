# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("M - Matutino => V - Vesperino => N - Noturno \n ", '-'*35)
# Sabendo o turno escolar
turno = str(input("Em que turno estudas: "))

# Validando a mensagem
if turno in "Mm":
    print("Bom Dia!!")
elif turno in "Vv":
    print("Boa Tarde!")
elif turno in "Nn":
    print("Boa Noite!")
else:
    print("Valor Inválido.")
