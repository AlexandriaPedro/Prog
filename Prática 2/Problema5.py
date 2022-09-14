from math import sqrt

numero = int(input("Digite um número: "))

if numero >= 0:
    raiz = sqrt(numero)
    print("Resultado: {:.3f}".format(raiz))
else:
    print("Número inválido")
    