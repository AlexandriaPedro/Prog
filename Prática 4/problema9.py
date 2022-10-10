somap = 0
somai = 0
n = 0

while n >= 0:
    if n % 2 == 0:
        somap += n
    else: 
        somai += n
    n = int(input("Digite um número: "))

print("Soma pares:", somap)
print("Soma ímpares:", somai)
