def soma(n):
    if (n == 1):
        return n
    else:
        return n + soma(n - 1)

n = int(input("Digite N: "))

x = soma(n)
print(x)
