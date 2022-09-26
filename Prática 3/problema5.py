def peso_ideal(alt, sex):
    if sex == 'F':
        peso = (62.1 * alt) - 44.7
    elif sex == 'M':
        peso = (72.7 * alt) - 58

    return peso
