# Tendo como dado de entrada a altura (h) de uma pessoa construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print('-'*25)
print(" MEDIDOR DE PESO IDEAL ")
print('-'*25)
sexo = str(input("Genero[F/M]: "))
altura = float(input("Qual é a sua altura: "))
print('-'*30)

# Validando o genero do User
if sexo in "Mm":
    homem_peso_ideal = (72.7 * altura) - 58
    print(f"O seu Peso Ideal é:{homem_peso_ideal:2f}")
elif sexo in "Ff":
    mulher_peso_ideal = (62.1 * altura) - 44.7
    print(f"O seu Peso Ideal é:{mulher_peso_ideal:2}")
else:
    print("Genero Inválido!!!")
