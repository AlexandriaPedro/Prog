ip = input("")

ip = ip.split('.')

aux = 0
aux1 = 0

for i in range(len(ip)):
    aux = int(ip[i])
    
    if aux >= 0 and aux <= 255:
        continue
    else:
        aux1 += 1

if aux1 > 0:
    print("Inválido")
else:
    print("Válido")
