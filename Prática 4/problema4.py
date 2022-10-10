preço = float(input("Digite o preço do pão: "))

i = 1

while i <= 50:
    print(i, "- R$ {:.2f}".format(preço * i))    
    i += 1
