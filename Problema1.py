ii = float(input("Digite o valor do investimento inicial: "))
j = float(input("Digite a taxa de juros anual: "))
ia = float(input("Digite o período do investimento em anos: "))

v = ii * (1 + (j * 0.01)) ** ia

print("Valor futuro: {:.2f}".format(v))
