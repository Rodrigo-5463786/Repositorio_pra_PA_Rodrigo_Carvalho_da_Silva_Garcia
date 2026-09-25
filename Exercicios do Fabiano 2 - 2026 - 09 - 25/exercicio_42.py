notas = []
soma = 0

for i in range(5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    soma = soma + nota

media = soma / 5

print("\nMédia da turma:", media)

acima = 0

for nota in notas:
    if nota > media:
        acima = acima + 1

print("Alunos acima da média:", acima)