numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("\nPosição e valor:")
for i in range(5):
    print("Posição:", i, "- Valor:", numeros[i])