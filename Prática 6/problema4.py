lista = []

for i in range(12):
    lista.append(int(input("")))

média =  sum(lista) / 12
print("Média: {:.2f}".format(média))

for i in range(12):
    if lista[i] > média:
        print(lista[i])
