joao = 0
maria = 0
jose = 0
nulo = 0
branco = 0

print("1 - João")
print("2 - Maria")
print("3 - José")
print("4 - Nulo")
print("5 - Branco")
print("0 - Encerrar")

while True:
    voto = int(input("\nDigite seu voto: "))

    if voto == 0:
        break
    elif voto == 1:
        joao = joao + 1
    elif voto == 2:
        maria = maria + 1
    elif voto == 3:
        jose = jose + 1
    elif voto == 4:
        nulo = nulo + 1
    elif voto == 5:
        branco = branco + 1
    else:
        print("Voto inválido.")

print("\nRESULTADO")
print("João:", joao)
print("Maria:", maria)
print("José:", jose)
print("Nulos:", nulo)
print("Brancos:", branco)

if joao > maria and joao > jose:
    print("Vencedor: João")
elif maria > joao and maria > jose:
    print("Vencedor: Maria")
elif jose > joao and jose > maria:
    print("Vencedor: José")
else:
    print("Houve empate entre os candidatos.")