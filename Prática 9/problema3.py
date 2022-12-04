dicionario = dict()

aux = True

while (aux == True):
    nome = str(input(""))
    
    if (nome == ''):
        aux =  False
    else:
        n1 = float(input(""))
        n2 = float(input(""))
        
        m = (n1 + n2) / 2

        dicionario[nome] = dicionario.get(nome, m)

lista = list()

for nome, media in dicionario.items():
    lista.append((media, nome))

lista.sort(reverse=True)

for media, nome in lista:
    print("{} - {:.2f}".format(nome, media))
