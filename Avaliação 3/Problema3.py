def estacionamento(hc, mc, hp, mp):
    minc = hc * 60 + mc
    minp = hp * 60 + mp

    if minp > minc:
        minuto = (minp - minc) % 60
        hora = int((minp - minc) / 60)
    else:
        minuto = ((24 * 60) - minc + minp) % 60
        hora = int(((24 * 60) - minc + minp) / 60)

    if hora < 2 or (hora == 2 and minuto == 0):
        if minuto != 0:
            hora += 1
        return hora
    elif hora < 4 or (hora == 4 and minuto == 0):
        if minuto != 0:
            hora += 1
        return (hora * 1.40)
    else:
        if minuto != 0:
            hora += 1 
        return (hora * 2)
