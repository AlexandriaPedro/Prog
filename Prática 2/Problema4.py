salarioInicial = float(input("Digite o valor do salário: "))

salarioFinal = salarioInicial

if salarioInicial <= 280:
    salarioFinal += 0.20 * salarioInicial
elif salarioInicial > 280 and salarioInicial <= 700:
    salarioFinal += 0.15 * salarioInicial
elif salarioInicial > 700 and salarioInicial <= 1500:
    salarioFinal += 0.10 * salarioInicial
else:
    salarioFinal += 0.05 * salarioInicial

aumento = salarioFinal - salarioInicial

print("Valor do aumento: {:.2f}".format(aumento))
print("Novo salário: {:.2f}".format(salarioFinal))
