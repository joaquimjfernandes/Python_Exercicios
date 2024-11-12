# Mostre-me as seguintes listas, derivadas de:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Intervalo de 1 a 9
print('Lista de 1-9')
lIntervalo = lista[1:10]
print(lIntervalo)
print('-'*40)

# Intervalo de 8 a 13
print('Lista de 8-13')
lIntervalo = lista[8:14]
print(lIntervalo)
print('-'*40)

# Lista Reversa
print('Lista Reversa')
reversa = lista
reversa.sort(reverse=True)
print(reversa)
print('-'*40)

# Ler uma lista de 5 números inteiros e mostre cada número
# juntamente com a sua posição na lista.
print('Lista de 5 numeros Inteiros e sua Posição')
nFive = [5, 6, 3, 9]
for i, v in enumerate(nFive):
    print(i+1, '=>', v)
print('-'*40)

# Ler uma lista de 10 números reais e mostre-os na ordem inversa.
print('Lista de 10 numeros Reais na Ordem Inversa')
reais = [1.2, 3.40, 75.3, 11.11, 150.321, 21.22, 20.21, 61.64, 90.1, 32.1]
reais.sort(reverse=True)
print(reais)
