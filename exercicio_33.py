Q = int(input("Quantos termos deseja mostrar? "))

a = 0
b = 1

for i in range(Q):
    print(a)
    proximo = a + b
    a = b
    b = proximo