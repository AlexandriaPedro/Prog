v = float(input("Digite o valor da compra: "))

vd = v - ((v * 10) / 100)
vp = v / 6
vd10 = ((v * 10) / 100)
vd105 = (vd * 5) / 100
vcp = ((v * 5) / 100)

print("Valor com desconto: {:.2f}".format(vd))
print("Valor da parcela: {:.2f}".format(vp))
print("Comissão do vendedor (à vista): {:.2f}".format(vd105))
print("Comissão do vendedor (parcelado): {:.2f}".format(vcp))
