import random

campo = [0] * 10

minas = 0

while minas < 3:
    posicao = random.randint(0, 9)

    if campo[posicao] == 0:
        campo[posicao] = 1
        minas = minas + 1

print("Campo criado!")

passos = 0

while passos < 5:
    posicao = int(input("\nEscolha uma posição de 0 a 9: "))

    if posicao < 0 or posicao > 9:
        print("Posição inválida.")
        continue

    if campo[posicao] == 1:
        print("BOOM! Você pisou em uma mina!")
        print("Você perdeu!")
        break
    else:
        print("Posição segura!")
        passos = passos + 1

if passos == 5:
    print("\nParabéns! Você sobreviveu aos 5 passos e ganhou!")