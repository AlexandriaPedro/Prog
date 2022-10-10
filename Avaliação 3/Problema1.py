def progressoes(a1, r, n):
    PA_enesimo = a1 + ((n - 1) * r)   
    PG_enesimo = a1 * (r ** (n - 1))
    
    if PA_enesimo > PG_enesimo:
        PA_soma = ((a1 + PA_enesimo) * n) // 2
        return PA_soma
    else:
        PG_soma = a1 * (((r ** n) - 1) / (r - 1))
        return int(PG_soma)
