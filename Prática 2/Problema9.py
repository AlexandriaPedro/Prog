valorInicial = float(input("Digite o valor do produto: "))
estado = str(input("Digite o estado: "))

valorFinal = valorInicial

if estado == "MG":
    valorFinal += 0.07 * valorInicial
elif estado == "SP":
    valorFinal += 0.12 * valorInicial
elif estado == "RJ":
    valorFinal += 0.15 * valorInicial
elif estado == "MS":
    valorFinal += 0.08 * valorInicial
else:
    print("Estado inválido")
    exit()
    
print("Valor final: {:.2f}".format(valorFinal))
