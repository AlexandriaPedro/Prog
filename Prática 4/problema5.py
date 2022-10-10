n = int(input("Digite um inteiro n: "))

i = 1
t = 0

while i <= n:
    if n % i == 0:
        t += 1
    i += 1

if t <= 2:
    print("É primo")
else:
    print("Não é primo")
