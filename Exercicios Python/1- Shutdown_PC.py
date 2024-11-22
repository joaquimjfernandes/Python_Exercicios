# importando a biblioteca do system
import os

# recebendo valor do usuário
shutdown = str(input("Desligar tua Maquina?[yes/no]: "))

# condições
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")

print("Máquina Desligando...")