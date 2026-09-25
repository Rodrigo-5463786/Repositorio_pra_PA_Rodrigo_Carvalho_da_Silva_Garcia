poltronas = [False] * 10

while True:
    print("\n--- MAPA DE ASSENTOS ---")

    for i in range(10):
        if poltronas[i] == False:
            print(i, "- Livre")
        else:
            print(i, "- Reservada")

    poltrona = int(input("\nDigite o número da poltrona (0 a 9): "))

    if poltrona < 0:
        print("Programa encerrado.")
        break

    if poltrona > 9:
        print("Poltrona inválida.")
    elif poltronas[poltrona] == True:
        print("Ocupada.")
    else:
        poltronas[poltrona] = True
        print("Reservada.")