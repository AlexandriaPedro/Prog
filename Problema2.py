p = float(input("Digite o valor que o Pedro apostou: "))
j = float(input("Digite o valor que o João apostou: "))
m = float(input("Digite o valor que o Marcela apostou: "))
v = float(input("Digite o valor do prêmio: "))

prop = v / (p + j + m)
propp = prop * p
propj = prop * j
propm = prop * m

print("Prêmio do Pedro: {:.2f}".format(propp))
print("Prêmio do João: {:.2f}".format(propj))
print("Prêmio da Marcela: {:.2f}".format(propm))
