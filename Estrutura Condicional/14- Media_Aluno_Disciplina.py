# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# recebendo dados do aluno
nome = 'Joaquim'
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
semestre = int(input('Qual Semestre: '))
disciplina = str(input('Qual Disciplina: '))

# validação ⇛ aproveitamento indices
aproveitamento = ' ' # A - B - C - D - E
situacao = ' ' # APROVADO - RECUPERAÇÃO - REPROVADO
# calculando a média do aluno
media = (nota1 + nota2) / 2

# validando aproveitamento do aluno
if media >= 10:
    aproveitamento = "A"
    situacao = "APROVADO"
elif media <= 9 >= 7:
    aproveitamento = " C"
    situacao = "RECUPERAÇÃO"
else:
    aproveitamento = "E"
    situacao = "REPROVADO"

# mostrando na tela o resultado
print(f'Nome: {nome} => Média: {media}=> Aproveitamento: {aproveitamento} \n=> Situação: {situacao} => Disciplina: {disciplina}')