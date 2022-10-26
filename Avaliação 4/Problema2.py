soma = 0 
maximo = 0

for dia in range(1, 8):
    indice = float(input(f"Qual o Índice Pluviométrico do dia {dia}? "))
    soma += indice
    
    if indice > maximo:
        maximo = indice
        diadomaximo = dia

media = soma/7

print(f"Índice Médio: {media:.2f}")
print(f"Índice Máximo: {maximo:.2f}")
print(f"Dia do Máximo = {diadomaximo}")
