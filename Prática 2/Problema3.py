idade = int(input("Digite a idade: "))
tempo = int(input("Digite o tempo de contribuição: "))
sexo = str(input("Digite o sexo (M/F): "))

if sexo == "F":
    if (idade >= 55 and tempo >= 30) or (idade >= 60):
        print("Pode aposentar")
    else:
        print("Não pode aposentar")
        
elif sexo == "M":
    if (idade >= 60 and tempo >= 35) or (idade >= 65):
        print("Pode aposentar")
    else:
        print("Não pode aposentar")
