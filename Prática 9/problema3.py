n = int(input("Digite um inteiro: "))

palavras = ''

texto = open('texto.txt')

for linha in texto:
    for i in linha.split():
        if len(i) >= n:
            palavras += i + '\n'

print(palavras)
