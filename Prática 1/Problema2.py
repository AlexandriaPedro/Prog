vo = float(input("Digite o valor da velocidade: "))
a = float(input("Digite o valor da aceleração: "))
t = float(input("Digite o valor do tempo: "))

vf = vo + (a * t)
d = (vo * t) + ((a * (t ** 2)) / 2)

print("Velocidade final: {:.2f}".format(vf))
print("Distância percorrida: {:.2f}".format(d))
