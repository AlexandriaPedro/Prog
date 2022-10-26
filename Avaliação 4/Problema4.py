numero = int(input('Digite um número: '))

maior = None
menor = None

while numero >= 0:
    if maior == None and menor == None:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    numero = int(input('Digite um número: '))

print('Maior: %d'%maior)
print('Menor: %d'%menor)
