def pagamento(sala):
    if sala <= 280:
        aum = 0.20 * sala
    elif sala <= 700:
        aum = 0.15 * sala
    elif sala <= 1500:
        aum = 0.10 * sala
    else:
        aum = 0.05 * sala
        
    saln = aum + sala
    return saln
