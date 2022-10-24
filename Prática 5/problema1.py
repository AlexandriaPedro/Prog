nome = str(input(""))

aux = nome.rfind(" ")

sobrenome = nome[aux + 1:]

print("Nome formatado:", sobrenome + ", " + nome[:aux])
