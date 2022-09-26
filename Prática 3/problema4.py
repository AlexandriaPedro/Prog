def calcula_valor(preço, quant, tipo):
    valor = preço * quant
    
    if tipo == 'a':
        if quant <= 20:
            valort = valor - (0.03 * valor)
        else:
            valort = valor - (0.05 * valor)
    elif tipo == 'g':
        if quant <= 20:
            valort = valor - (0.04 * valor)
        else:
            valort = valor - (0.06 * valor)
    
    return(valort)
