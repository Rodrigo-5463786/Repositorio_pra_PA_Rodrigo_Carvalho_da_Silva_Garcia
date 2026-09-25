nomes = []
notas = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    nomes.append(nome)
    notas.append(nota)

print("\nResultado:")

for i in range(3):
    if notas[i] >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("Nome:", nomes[i])
    print("Nota:", notas[i])
    print("Situação:", situacao)
    print()