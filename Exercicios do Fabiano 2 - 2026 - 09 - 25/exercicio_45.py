frase = input("Digite uma frase: ")

palavras = frase.split()

quantidade_palavras = len(palavras)
quantidade_a = 0

for letra in frase:
    if letra == "a" or letra == "A":
        quantidade_a = quantidade_a + 1

print("\nQuantidade de palavras:", quantidade_palavras)
print("Quantidade de letras A:", quantidade_a)