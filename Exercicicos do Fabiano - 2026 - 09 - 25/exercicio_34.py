quantidade = int(input("Quantos alunos existem? "))

notas = []

for i in range(quantidade):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Média da turma:", media)