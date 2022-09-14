velocidadeMax = int(input("Digite o valor da velocidade máxima: "))
velocidadeReg = int(input("Digite o valor da velocidade registrada: "))

if velocidadeReg <= velocidadeMax:
    print("Sem Infração")
elif velocidadeReg <= velocidadeMax + (0.2 * velocidadeMax):
    print("Infração Média")
elif velocidadeReg > velocidadeMax + (0.2 * velocidadeMax) and velocidadeReg <= velocidadeMax + (0.5 * velocidadeMax):
    print("Infração Grave")
else:
    print("Infração Gravíssima")
