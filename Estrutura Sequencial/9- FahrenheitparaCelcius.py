# Faça um Programa que peça a temperatura em graus Fahrenheit
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
F = float(input("Graus Fº: "))
C = 5 * ((F-32) / 9)
print(f"Temperatura convertida em graus Cº:{C:2}")