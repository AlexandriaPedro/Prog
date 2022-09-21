#Calcular raízes do segundo grau

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))


if(a == 0):
    print('Não é uma equação quadrática')
else:  
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('Não existe raiz real')
    elif delta == 0:
        print('Raiz única')
        x = -b / (2 * a)
        print('Raiz: %.2f '%x)
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5))  / (2 * a)

        print('Raiz 1: %.2f'%x1)
        print('Raiz 2: %.2f'%x2)
