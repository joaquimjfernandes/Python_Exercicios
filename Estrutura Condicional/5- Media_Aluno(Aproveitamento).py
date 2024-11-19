# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a dez;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# Recebendo as notas
n1 = float(input("Primeira Nota: "))
n2 = float(input("Segunda Nota: "))

# Calculando a média do aluno
media = (n1 + n2) / 2
# fazendo a condição do aproveitamento
if media == 10:
    print(f"{media} => APROVADO com DISTINÇÃO")
elif media >=10:
    print(f"{media} => APROVADO")
elif media <= 7:
    print(f"{media} => REPROVADO")