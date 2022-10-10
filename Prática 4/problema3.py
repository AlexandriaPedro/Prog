print("Loja Quase Dois - Tabela de preços")

preço = 1.99
i = 1

while i <= 50:
    print(i, "- R$ {:.2f}".format(preço * i))    
    i += 1
