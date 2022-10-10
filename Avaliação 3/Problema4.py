def valor_energia(qtde_kwh, tipo):
    if tipo == 'R':
        if qtde_kwh <= 500:
            preco = qtde_kwh * 0.4
        else:
            preco = qtde_kwh * 0.65
    elif tipo == 'C':
        if qtde_kwh <= 1000:
            preco = qtde_kwh * 0.55
        else:
            preco = qtde_kwh * 0.60
    else:
        if qtde_kwh <= 5000:
            preco = qtde_kwh * 0.55
        else:
            preco = qtde_kwh * 0.60
    return preco
