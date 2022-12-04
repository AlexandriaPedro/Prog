dicionario = dict()

rna = str(input("Digite o RNA: "))

a = rna[:3]
b = rna[3:6]
c = rna[6:9]

lista = [a, b, c]

for letra in lista:
    if (letra == 'UUU'):
        dicionario[letra] = 'Phe-'
    elif (letra == 'CUU' or letra == 'UUA'):
        dicionario[letra] = 'Leu-'
    elif (letra == 'AAG'):
        dicionario[letra] = 'Lisina-'
    elif (letra == 'UCU'):
        dicionario[letra] = 'Ser-'
    elif (letra == 'UAU'):
        dicionario[letra] = 'Tyr-'
    elif (letra == 'CAA'):
        dicionario[letra] = 'Gln-'

print("Cadeia de Aminoácidos: ", end="")

lista = list()

for x in dicionario.values():
    lista.append(x)

for x in lista:
    if x == lista[len(lista) - 1]:
        lista[len(lista) - 1] = x[:3]

frase = ''
frase = frase.join(lista)

print(frase)
