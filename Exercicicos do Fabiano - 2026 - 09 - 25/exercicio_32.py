N = int(input("Digite um número: "))

eh_primo = True

if N <= 1:
    eh_primo = False
else:
    for i in range(2, N):
        if N % i == 0:
            eh_primo = False
            break

if eh_primo:
    print("É primo!")
else:
    print("Não é primo.")