v = int(input("Digite a quatidade de dias trabalhados: "))

vd = (v * 30)
r = (vd - (vd * 8) / 100)

print("Valor recebido: {:.2f}".format(r))
