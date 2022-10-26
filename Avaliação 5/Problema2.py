senha = input('Entrada: ')

a = 1
e = 3
i = 5
o = 7
u = 9
soma = 0

for c in senha:
    if c == 'a':
        soma += a
    elif c == 'e':
        soma += e
    elif c == 'i':
        soma += i
    elif c == 'o':
        soma += o
    elif c == 'u':
        soma += u

print('Soma:', soma)
