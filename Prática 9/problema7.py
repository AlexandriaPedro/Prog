abrir_arquivo = open('tempos.txt')

dicionario = dict()

pessoa_com_menor_tempo = None
menor_tempo = 1000

for linha in abrir_arquivo:
    palavra =  linha.split(' ')
    
    volta1 = int(palavra[1])
    volta2 = int(palavra[2])
    volta3 = int(palavra[3])
    volta4 = int(palavra[4])
    volta5 = int(palavra[5])
    
    lista_de_voltas = [volta1, volta2, volta3, volta4, volta5]
    
    for volta in lista_de_voltas:
        if volta < menor_tempo:
            menor_tempo = volta
            pessoa_com_menor_tempo = palavra[0]
    
    volta_total = volta1 + volta2 + volta3 + volta4 + volta5
    
    volta_total_media = volta_total / 5
    
    dicionario[palavra[0]] = volta_total_media

print("Melhor volta: {} - {} segundos".format(pessoa_com_menor_tempo, menor_tempo))

print("Classificação final:")

lista_classificação = list()

for corredor, media in dicionario.items():
    lista_classificação.append((media, corredor))

lista_classificação.sort()

for i in range(0, len(lista_classificação)):
    print("{} - {} - {:.2f}".format(i + 1, lista_classificação[i][1], lista_classificação[i][0]))
