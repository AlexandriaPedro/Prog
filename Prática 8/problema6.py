def imprime_naturais_pares(n):
    if (n == 0):
        print(0)
    else:
        imprime_naturais_pares(n - 1)
        if (n % 2 == 0):
            print(n)

n = int(input("Digite N: "))

imprime_naturais_pares(n)
