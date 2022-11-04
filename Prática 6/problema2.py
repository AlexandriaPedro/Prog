lista = []

for i in range(5):
    lista.append(float(input("")))

lista.pop(lista.index(min(lista)))
lista.pop(lista.index(max(lista)))

média =  sum(lista) / len(lista)

print("Média: {:.2f}".format(média))
