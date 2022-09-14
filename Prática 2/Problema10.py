dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if (mes > 12 or mes < 1) or (dia > 31 or dia < 1) or (ano < 1):
    print("Data inválida")
    exit()
    
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    if mes == 2 and dia <= 29: 
        print("Data válida")
    elif mes == 4 and dia <= 30:
        print("Data válida")
    elif mes == 6 and dia <= 30:
        print("Data válida")
    elif mes == 9 and dia <= 30:
        print("Data válida")
    elif mes == 11 and dia <= 30:
        print("Data válida")
    elif mes == 1 and dia <= 31:
        print("Data válida")
    elif mes == 3 and dia <= 31:
        print("Data válida")
    elif mes == 5 and dia <= 31:
        print("Data válida")
    elif mes == 7 and dia <= 31:
        print("Data válida")
    elif mes == 8 and dia <= 31:
        print("Data válida")
    elif mes == 10 and dia <= 31:
        print("Data válida")
    elif mes == 12 and dia <= 31:
        print("Data válida")
    else:
        print("Data inválida")
        
elif mes == 2 and dia <= 28:
    print("Data válida")
elif mes == 4 and dia <= 30:
        print("Data válida")
elif mes == 6 and dia <= 30:
        print("Data válida")
elif mes == 9 and dia <= 30:
        print("Data válida")
elif mes == 11 and dia <= 30:
        print("Data válida")
elif mes == 1 and dia <= 31:
        print("Data válida")
elif mes == 3 and dia <= 31:
        print("Data válida")
elif mes == 5 and dia <= 31:
        print("Data válida")
elif mes == 7 and dia <= 31:
        print("Data válida")
elif mes == 8 and dia <= 31:
        print("Data válida")
elif mes == 10 and dia <= 31:
        print("Data válida")
elif mes == 12 and dia <= 31:
        print("Data válida")
else:
    print("Data inválida")
