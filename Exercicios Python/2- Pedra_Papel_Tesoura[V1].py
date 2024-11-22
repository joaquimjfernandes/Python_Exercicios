# Mini-Game do Pedra → Papel → Tesoura

print('---'*15, '\n           Rock => Paper => Seasor')
print('---'*15)

# variáveis extras
vencedor1 = vencedor2 = vencedor3 = 0

# recebendo usuários
player1 = str(input('[Player 1] => pedra, papel, tesoura: ')).lower()
player2 = str(input('[Player 2] => pedra, papel, tesoura: ')).lower()
player3 = str(input('[Player 3] => pedra, papel, tesoura: ')).lower()
print('-----'*9)

# Regras do Jogo            # player1 -> [Vitorias]3 <==>  # player1 -> [Perdas] 2
# Papel ganha Pedra         # player2 -> [Vitorias]2 <==>  # player2 -> [Perdas] 3
# pedra ganha tesoura       # player3 -> [Vitorias]3 <==>  # player3 -> [Perdas] 2
# tesoura ganha papel

# fazendo as condições do vencedor
if player1 in 'papel' and player2 in 'pedra' and player3 in 'papel':
    print(f'Vencedores: Player1:{player1} <==> Player3:{player3}')
elif player1 in 'pedra' and player2 in 'pedra' and 'tesoura':
    print(f'Vencedores: Player1:{player1} <==> Player2:{player2}')
elif player1 in 'tesoura' and player2 in 'papel' and player3 in 'tesoura':
    print(f'Vencedores: Player1:{player1} <==> Player3:{player3}')
elif player1 in 'papel' and player2 in 'tesoura' and player3 in 'papel':
    print(f'Vencedores: Player1:{player2} <==> ')
elif player1 in 'tesoura' and player2 in 'tesoura' and player3 in 'pedra':
    print(f'Vencedores: Player1:{player3} <==> ')
elif player1 in 'pedra' and player2 in 'papel' and player3 in 'pedra':
    print(f'Vencedores: Player1:{player2} <==> ')
# elif player1 == player2 == player3:
#     print(f'Ninguém Ganhou Todos Perderam!!')
elif player1 != player2 != player3:
    print(f'Ninguém Ganhou Todos Perderam!!')

