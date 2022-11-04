def nested_sum(lista):
    soma = 0
    
    for i in range(len(lista)):
        soma += sum(lista[i])

    return ("Soma: ", soma)
