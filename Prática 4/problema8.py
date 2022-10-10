def quantidade_pares(inicio, fim):
    pares = 0
    
    while inicio <= fim:
        if inicio % 2 == 0:
            pares += 1
        inicio += 1

    return (pares)
