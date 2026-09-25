numero = int(input("Digite o 1º número: "))

maior = numero
menor = numero

for i in range(2, 6):
    numero = int(input("Digite o " + str(i) + "º número: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("Maior valor:", maior)
print("Menor valor:", menor)