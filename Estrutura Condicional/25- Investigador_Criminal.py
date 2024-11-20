# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente"

# Perguntas a serem feitos nos suspeitos
pergunta1 = str(input("Telefonou para a vítima?[y/n]: "))
pergunta2 = str(input("Esteve no local do crime?[y/n]: "))
pergunta3 = str(input("Mora perto da vítima?[y/n]: "))
pergunta4 = str(input("Devia para a vítima?[y/n]: "))
pergunta5 = str(input("Já trabalhou com a vítima?[y/n]: "))

# Declarando uma classificação sobre a participação da pessoa no crime
if pergunta1 in "Yy" and pergunta2 in "Yy":
    print("Suspeito/a")
elif pergunta3 in "Yy" and pergunta4 in "Yy":
    print("Suspeito/a")
elif pergunta3 in "Yy" and pergunta1 in "Yy":
    print("Cúmplice")
elif pergunta2 in "Yy" and pergunta4 in "Yy":
    print("Cúmplice")
elif pergunta5 in "Yy" and pergunta2 in "Yy":
    print("Assassino")
elif pergunta5 in "yy":
    print("Assassino")
else:
    print("Suspeito Liberado")

print("Encerrando Programa!!!")
