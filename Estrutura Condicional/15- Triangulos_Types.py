# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

# recebendo os lados do Triangulo
v1 = int(input('Primeiro Lado: '))
v2 = int(input('Segundo Lado: '))
v3 = int(input('Terceiro Lado: '))

# tipos de triangulo
tipos = ('Equilátero', 'Isósceles', 'Escaleno')

# Triangulo Equilátero => [Os 3 lados Iguais]
if v1 == v2 and v1 == v3:
    print(tipos[0])
elif v2 == v1 and v2 == v3:
    print(tipos[0])
elif v3 == v1 and v3 == v2:
    print(tipos[0])

# Triangulo Isósceles => [2 lados Iguais]
if v1 == v2 != v3:
    print(tipos[1])
elif v2 == v3 != v1:
    print(tipos[1])
elif v3 == v1 != v2:
    print(tipos[1])

# Triangulo Escaleno => [3 lados Diferentes]
if v1 != v2 != v3:
    print(tipos[2])
elif v2 != v1 != v3:
    print(tipos[2])
elif v3 != v1 != v2:
    print(tipos[2])
print('-'*15)
