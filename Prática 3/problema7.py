def operacao(n1, n2, simb):
    if simb == '+':
        resp = n1 + n2
    elif simb == '-':
        resp = n1 - n2
    elif simb == '*':
        resp = n1 * n2
    elif simb == '/':
        resp = n1 / n2
    
    return resp
