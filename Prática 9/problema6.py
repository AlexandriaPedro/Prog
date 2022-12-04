unidades = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
dezenas = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
centenas = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

numero = int(input("Digite um número: "))

unidade = numero % 10

dezena = ((numero - unidade) / 10) % 10
dezena = int(dezena)

centena = (((numero - unidade) / 10) - dezena) / 10
centena = int(centena)

print("Número Romano: ", end='')

lista = [centena, dezena, unidade]

for x in lista:
    if x == lista[0]:
        for a, b in centenas.items():
            if x == a:
                lista[0] = b
    elif x == lista[1]:
        for a, b in dezenas.items():
            if x == a:
                lista[1] = b
    elif x == lista[2]:
        for a, b in unidades.items():
            if x == a:
                lista[2] = b

print(''.join(lista))
