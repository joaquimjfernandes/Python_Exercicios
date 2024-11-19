# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

print('-'*35, '\n SITUAÇÃO DO ALUNO')
print('-'*35)

# recebendo as notas do aluno
nota1 = float(input("1ª Nota: "))
nota2 = float(input("2ª Nota: "))
nota3 = float(input("3ª Nota: "))

# calculando a média do aluno
media = (nota1 + nota2 + nota3) / 3
print('-'*35)
# validando o aproveitamento
if media > 10:
    print(f"Aluno APROVADO => Média: {media}")
elif media < 10:
    print(f"Aluno REPROVADO => Média: {media}")
elif media == 10:
    print(f"Aluno APROVADO com DISTINÇÃO => Média: {media}")