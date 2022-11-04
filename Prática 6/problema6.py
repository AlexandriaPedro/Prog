def tamanho_maior_string(lista):
    maior = 0
    
    for i in range(len(lista)):
        if len(lista[i]) > maior:
            maior = len(lista[i])

    return maior
