velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5

    print("Você foi multado!")
    print("Valor da multa: R$", multa)
else:
    print("Boa viagem!")