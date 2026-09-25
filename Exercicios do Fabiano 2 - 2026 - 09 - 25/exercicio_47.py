produtos = []
quantidades = []

while True:
    print("\n--- ESTOQUE ---")
    print("1 - Adicionar Produto")
    print("2 - Dar Baixa")
    print("3 - Ver Estoque")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))

        encontrado = False

        for i in range(len(produtos)):
            if produtos[i] == nome:
                quantidades[i] = quantidades[i] + quantidade
                encontrado = True

        if encontrado == False:
            produtos.append(nome)
            quantidades.append(quantidade)

        print("Produto adicionado!")

    elif opcao == 2:
        nome = input("Digite o produto: ")
        quantidade = int(input("Quantidade para retirar: "))

        encontrado = False

        for i in range(len(produtos)):
            if produtos[i] == nome:
                encontrado = True

                if quantidades[i] >= quantidade:
                    quantidades[i] = quantidades[i] - quantidade
                    print("Baixa realizada!")
                else:
                    print("Estoque insuficiente.")

        if encontrado == False:
            print("Produto não encontrado.")

    elif opcao == 3:
        print("\n--- ESTOQUE ATUAL ---")

        for i in range(len(produtos)):
            print(produtos[i], "-", quantidades[i], "unidades")

    elif opcao == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")