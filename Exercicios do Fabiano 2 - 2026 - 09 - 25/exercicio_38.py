principal = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    principal.append(numero)

for numero in principal:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nLista principal:", principal)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)