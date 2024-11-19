# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Qual é o teu Sexo[M/F]: "))

# Fazendo a Condição
if sexo not in "FfMm": # Erro!! se digitar outras letras
    print("Sexo Inválido.")
elif sexo in "Mm": # Masculino
    print("M - Masculino")
elif sexo in "Ff": # Feminino
    print("F - Feminino")
print('-'*25)