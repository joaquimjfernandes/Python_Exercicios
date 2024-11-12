print('='*25)
print("| Colégio Bons Hábitos  |")
print('='*25)

nome = str(input("Nome do Aluno: "))
nota1 = float(input("1ª Nota: "))
nota2 = float(input("2ª Nota: "))
nota3 = float(input("3º Nota: "))
nota4 = float(input("4ª Nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"{nome} | {nota1} | {nota2} | {nota3} | {nota4} | {media}")

