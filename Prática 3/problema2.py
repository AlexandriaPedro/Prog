def pagamento(valh, quah):
    sal = valh * quah
    if sal <= 900:
        des = 0.00
    elif sal <= 1500:
        des = 0.05 * sal
    elif sal <= 2500:
        des = 0.10 * sal
    else:
        des = 0.20 * sal
        
    saln = sal - des
    return saln
