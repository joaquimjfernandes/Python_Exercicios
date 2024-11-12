# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

# Entrada de dados
tamanho_arquivo = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Informe a velocidade do link de Internet (em Mbps): "))

# Cálculo do tempo de download em segundos
# 1 Mbps = 1 Megabit por segundo; o arquivo está em MB (Megabytes), então convertemos.
# 1 Byte = 8 bits, portanto dividimos a velocidade por 8 para converter para MBps.
velocidade_MBps = velocidade_internet / 8
tempo_segundos = tamanho_arquivo / velocidade_MBps

# Converte o tempo de segundos para minutos
tempo_minutos = tempo_segundos / 60

# Exibe o tempo aproximado de download
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")
