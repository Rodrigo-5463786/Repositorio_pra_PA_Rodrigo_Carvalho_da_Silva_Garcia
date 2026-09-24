n = int(input("Digite quantos elementos deseja mostrar: "))

a = 0
b = 1

for i in range(n):
    print(a)

    proximo = a + b
    a = b
    b = proximo