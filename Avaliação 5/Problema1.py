a = input('Digite o primeiro número: ')
b = input('Digite o segundo número: ')

res = int(a) + int(b)
res = str(res)

newRes = ''

for l in res:
    if l != '0':
        newRes = newRes + l

print('Resultado:', newRes)
