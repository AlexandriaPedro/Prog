def power (k, n):
    if (n == 1):
        return k
    else:
        return k * power(k, n - 1)

k = int(input("Digite k: "))
n = int(input("Digite n: "))

x = power(k, n)
print(x)
