import random

numero_secreto = random.randint(1, 10)

tentativas = 0
chute = 0

while chute != numero_secreto:
    chute = int(input("Tente adivinhar o número de 1 a 10: "))

    tentativas = tentativas + 1

    if chute < numero_secreto:
        print("Maior!")

    elif chute > numero_secreto:
        print("Menor!")

    else:
        print("Acertou!")

print("Número de tentativas:", tentativas)