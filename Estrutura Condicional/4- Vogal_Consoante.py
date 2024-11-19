# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input("Digite uma Letra: "))

# recebendo as vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# recebendo as consoante
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
              'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# Achando se é Vogal ou Consoante
if letra in vogais:
    print("A letra que você digitou é uma Vogal!")
elif letra in consoantes:
    print("A letra que você digitou é CONSOANTE!")