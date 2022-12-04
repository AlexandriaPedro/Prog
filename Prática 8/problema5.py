def imprime_naturais(n):
    if (n == 0):
        print(0)
    else:
        imprime_naturais(n - 1)
        print(n)

n = int(input("Digite N: "))

imprime_naturais(n)
