custoInicial = float(input("Digite o custo da fábrica: "))

custoFinal = custoInicial

if custoInicial <= 12000:
    custoFinal += 0.05 * custoInicial
elif custoInicial > 12000 and custoInicial <= 25000:
    custoFinal += (0.10 * custoInicial) + (0.15 * custoInicial)
else:
    custoFinal += (0.15 * custoInicial) + (0.20 * custoInicial)
    
print("Custo total: {:.2f}".format(custoFinal))
