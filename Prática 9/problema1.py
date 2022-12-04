dicionario = dict()

palavra = str(input(""))

for letra in palavra:
    dicionario[letra] = dicionario.get(letra, 0) + 1

maior_valor = 0
maior_letra = None

for letra, valor in dicionario.items():
    if valor > maior_valor:
        maior_valor = valor
        maior_letra = letra

print(maior_letra)
