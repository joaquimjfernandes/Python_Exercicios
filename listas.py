# Estudando sobre Listas
"""
    1- Listas são coleções heterogêneas de objetos(qualquer tipo) → É MUTÁVEL[Pode se alterar]
    Uma Lista é, na verdade, um objeto da classe list() ⇒ Implementação de arrays()
    2- Diferença ⇒ Listas são mutáveis e Tuplas imutáveis
    3- Listas são mais lentas, porém mais poderosas que tuplas
"""
# Listas simples
comida = ['Arroz', 'Massa', 'Feijão']
print(comida)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[::])
print('-'*25)

# Lista de Amigos
amigos = ['Francisco', 'Levi', 'Gonga', 'Claúdio', 'Antonio']
# Varrendo a Lista
for amigo in amigos:
    print(amigo)
print('-'*25)

# Atribuições de Dados na lista
idade = [12, 25, 15, 23, 32, 10, 5, 1, 'Todos Velhos']
idade[0] = 24
idade[-1] = 'Irmãos'
idade[3] = 24
print(idade)
print('-'*25)

# Operações nas listas [Trocando Elementos]
idade[-1] = 'Afonso'
idade[0] = 'Chico'
for idades in idade:
    print(idades)
print('-'*25)

# Operações [Incluindo Elementos]
amigos.append('Afonso')
comida.append('Café')
comida.append('Bolo')
comida.append('Leite')
comida.append('Bolacha')
for amigo in amigos:
    print(amigo)
print('-'*25)

# Operações [Removendo Elementos(por valor)]
idade.remove('Chico')
idade.remove('Afonso')
for ls in idade:
    print(ls)
print('-'*25)

# Operações [Removendo Elementos(por posição)]
del comida[2]
print(comida)

# Ordenando a lista
amigos.sort()
for amigo in amigos:
    print(amigo)
print('-'*25)

# Invertendo a lista
idade.reverse()
for idades in idade:
    print(idades)
print('-'*25)

# Imprimindo com a posição de cada elemento
for i, p in enumerate(amigos):
    print(i + 1, '=>', p)

# A função enumerate() retorna dois elementos a cada iteração: 1 → a Posição Sequencial =+
# 2 → Item da Sequencial Correspondente // comandos de Ordenação ==> sort() and Inversão ==> reverse()
print('-'*35)
print(comida, '\n', amigos, '\n', idade)
# Fatiando
print(idade[1])  # Mostrando o indice 1
print(amigos[:2])  # Mostrando os indice 0 e 1 ⇨ ignorando os outros
print(comida[1:3:2])  # Mostrando o indice 1 ignorando todos os outros
print(comida[0:3:2])  # Mostra o indice 0 e 2
print('-'*35)

# Operações em Listas
# Dados do tipo listas, dicionarios são pré-definidos pelo usuário são mutáveis!
a = [1, 2, 3]
b = (4, 5, 6)
# Cópias de Listas
c = a[:]
a.append(4)
print(a, c)
a[0] = 0
# list(tuple(a)) Convertendo lista para tupla(vice-versa)
# b[3] = 7 # TypeError: 'tuple' object does not support item assignment
print(a, b)
print('-'*35)

# Operações Matemática
elementos = [0, 1, 2, 3, 4, 5]
elementos.extend([12, 0, 1, 0, 1])
print(elementos)
print('Total:', sum(elementos))  # Somátório de todos elementos
print('Tamanho:', len(elementos))  # Tamanho dos elementos da lista
print('Maxímo:', max(elementos))  # Valor maxímo dos elementos da lista
print('Mínimo:', min(elementos))  # Valor mínimo dos elementos da lista
print('-'*35)

# Trabalhando com Métodos
# extend() -> Acrescenta os elementos da lista2 ao final da lista1 [Altera a lista Original]
som = ['Stay', '45', '3:5']
print(som)  # lista Original
som.extend(['1998', 'Run Away'])
print(som)  # lista extendida
print('-'*35)

# count() -> Retorna quantas vezes o elemento aparece na lista
print('O elemento aparece:', elementos.count(1))

# index() -> Retorna o índece da primeira ocorrência de elemento na lista
# [Um erro ocorre se o elemento não consta na lista Ex: ValueError: 15 is not in list]
print('Primeira ocorrência do elemento:', elementos.index(3))
print('-'*35)

# insert(índice, elemento) -> Insere elemento na posição indicada por índice(Altera a lista Original)
musica = ['Favorite Song', 'Better of Me', 'Antisocial', 'Negócios']
musica.insert(2, 'Mockingbird')
print(musica)
# Outras formas de inserir
numero = [3, 7, 10]
numero[3:] = [30]
print(numero)
print('-'*35)

# pop() -> Remove da lista o elemento na posição índice e o retorna
# [Se o índice não for mencionado, é assumido o último]
numero.pop()  # Elimina o ultimo elemento
musica.pop(3)  # Elimina o elemento do indice 3
print(numero, '\n', musica)
print('-'*35)

# split() -> Separa uma string em uma lista de strings menores. Recebe como parâmetro um
# caractere separador e um número máximo de pedaços (opcional). Retorna uma lista de strings
url = 'www.facebook.com'.split('.')
print(url)
data = '19,05,25'.split(':')
print('-'*35)
print(data)
print('-'*35)

# Compreensão de Listas
"""
    Funcionalidade muito poderosa da linguagem Python Gera uma lista nova aplicando 
    uma função para cada elemento da lista original. Muito usado por programadores Python!
"""
s = [x**2 for x in range(10)]  # Simple Expression
m = [x**2 for x in s if x % 2 == 0]
print(s, '=>', m)
print('-'*35)
# Testando List Compression
t = 12
r = [t*2 for t in s if t % 2 == 0]  # Não entendi direito
print(r)
print('-'*35)
m = [i*2 for i in m if i > 5]
# -> i-variável de control, para i dentro de m-variável principal, me mostra só se o i for maior que 5
print(m)
s = [i for i in [a for a in s]]  # aninhar compreensão de listas!
print(s)
print('-'*35)
# Listas: Concatenação e Repetição
n = [2]*4  # * Usamos para Repetição
p = n + [1]*4  # + Usamos para Concatenação
print(n, '\n', p)
print('-'*35)

# Inicializando Listas
# Não é possível atribuir: valor a uma posição inexistente de uma lista(vetor)
# ATT: Se uma lista vai ser usada como vetor, é conveniente iniciá-la
# vetor = [] vetor[0] = 1  # IndexError: list assignment index out of range
vetor = [0] * 5
vetor[0] = 3
vetor[2] = 6
vetor[4] = 12
# vetor[0] = 3, 4, 5, 6, 9  # Criando uma tupla dentro de um vetor
v = [vetor*2 for vetor in range(10)]
print(vetor)

# Usando None(não faz parte de nenhum tipo, é melhor que usar 0 ou string vazia)
# Útil para criar uma lista “vazia” mas com um número conhecido de posições
lista = [None]*5
print(lista)

# A função list()
"""
    Pode ser usada para converter uma string numa lista. É útil pois uma lista pode ser modificada, 
    mas uma string não. Para fazer a transformação inversa, pode-se usar o método join
"""
palavra = list('Olá')
print(palavra)
palavra[1] = 'p'
print(palavra)
''.join(palavra)
print(palavra)

# Alguns métodos da classe list
# sort(cmp=None, key=None, reverse=False) -> Ordena a lista
# Os argumentos são opcionais. Por default, a lista é ordenada crescentemente
numeros = [22, 13, 19, 1, 0, 8, 5,]
numeros.sort()  # Crescente
print(numeros)
# sort(cmp=None, key=None, reverse=True)
numeros.sort(reverse=True)  # Decrescente
print(numeros)

# Matrizes -> Listas podem ser usadas para guardar matrizes
# podemos criar uma matriz identidade 3X3 -:
mI = []
for i in range(3):
    mI.append([0]*3)
    mI[i][i] = 1
    print(mI)

m = [[0]*3]*3
for i in range(3):
    m[i][i] = 1
    print(m)
