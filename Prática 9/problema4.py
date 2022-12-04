dicionario = dict()

aux = True

while (aux == True):
    numero = int(input(""))
    
    if (numero != -1):
        dicionario[numero] = dicionario.get(numero, 0) + 1
    else:
        aux = False

numero_mais_digitado = None
numero_mais_digitado_quantidade = 0

for x, y in dicionario.items():
    if y > numero_mais_digitado_quantidade:
        numero_mais_digitado_quantidade = y
        numero_mais_digitado = x

print(numero_mais_digitado)
