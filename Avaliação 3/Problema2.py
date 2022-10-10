def consumo(km, l):
    kml = km / l
    
    if kml < 8:
        return "Venda o carro!"
    if kml >= 8 and kml <= 12:
        return "Econômico!"
    return "Super econômico!"
