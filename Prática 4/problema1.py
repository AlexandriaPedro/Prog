def populacao(ha, ta, hb, tb):
    anos = 0
    
    while ha < hb:
        ha += (ha * (ta / 100))
        hb += (hb * (tb / 100))
        anos += 1
    
    return anos
