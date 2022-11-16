texto = open('notas.txt')

for linha in texto:
    soma = 0
    
    array = linha.split(" ")
    
    for i in array:
        if i != array[0]:
            soma += int(i)  

    media = soma / 4
    
    if media >= 60:
        nome = array[0]

        print("Nome: {} - Média: {:.2f}".format(nome, media))
