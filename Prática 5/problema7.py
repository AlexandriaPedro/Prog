p = input('Digite uma palavra: ')
c = int(input('Digite o valor da chave: '))

cripto = ''

for i in p:
	if ord(i) + c > ord('z'):
		cripto += chr((ord('a') + c - (ord('z')+1 - ord(i))))
	else:
		cripto += chr(ord(i) + c)   

print('Resultado:', cripto)
