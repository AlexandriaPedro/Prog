maior = 0
palavramaior = ''

texto = open('texto.txt')

for linha in texto:
    for i in linha.split():
        if len(i) > maior:
            maior = len(i)
            palavramaior = i

print(palavramaior)
print(maior)
