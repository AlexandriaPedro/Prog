maior = 0
linhamaior = ''

texto = open('texto.txt')

for linha in texto:
    if len(linha) > maior:
        maior = len(linha)
        linhamaior = linha

print(linhamaior)
print(maior)
