import time

n = int(input("Digite um número inteiro: "))

print(f"Número ímpares até: {n}")

for numero in range(1, n +1):
    if numero % 2 != 0:
        print(numero)
        


