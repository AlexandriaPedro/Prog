def soma_divisores(n):
    somad = 0
    
    for c in range(1, n):
        if n % c == 0:
            somad += c
    
    return (somad)
