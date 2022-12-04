def soma (m, n):
    if (n == m):
        return m
    else:
        return m + soma(m + 1, n)

m = int(input("Digite m: "))
n = int(input("Digite n: "))

x = soma(m, n)
print(x)
