def imprime_naturais_impares(n):
    if (n == 1):
        print(1)
    else:
        if (n % 2 != 0):
            print(n)
            imprime_naturais_impares(n - 1)
        else:
            imprime_naturais_impares(n - 1)

n = int(input("Digite N: "))

imprime_naturais_impares(n)
