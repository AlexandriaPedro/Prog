numero1 = int(input("Digite o primeiro inteiro: "))
numero2 = int(input("Digite o segundo inteiro: "))
numero3 = int(input("Digite o terceiro inteiro: "))
numero4 = int(input("Digite o quarto inteiro: "))
numero5 = int(input("Digite o quinto inteiro: "))

maior = numero1
menor = numero1
divisiveis = 0

if numero2 > maior:
    maior = numero2
elif numero2 < menor:
    menor = numero2

if numero3 > maior:
    maior = numero3
elif numero3 < menor:
    menor = numero3
    
if numero4 > maior:
    maior = numero4
elif numero4 < menor:
    menor = numero4
    
if numero5 > maior:
    maior = numero5
elif numero5 < menor:
    menor = numero5
    
if numero1 % 3 == 0:
    divisiveis += 1
if numero2 % 3 == 0:
    divisiveis += 1
if numero3 % 3 == 0:
    divisiveis += 1
if numero4 % 3 == 0:
    divisiveis += 1
if numero5 % 3 == 0:
    divisiveis += 1

print("Maior: ", maior)
print("Menor: ", menor)
print("Quantidade de divisíveis por 3: ", divisiveis)
