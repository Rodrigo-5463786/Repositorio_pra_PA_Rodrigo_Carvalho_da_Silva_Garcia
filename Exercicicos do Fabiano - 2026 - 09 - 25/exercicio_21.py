quantidade = 0
soma = 0

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma = soma + numero
    quantidade = quantidade + 1

    numero = int(input("Digite um número (0 para parar): "))

print("Quantidade de números digitados:", quantidade)
print("Soma dos números:", soma)