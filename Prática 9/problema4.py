mais_recente = '00/00/0000'

arquivo = open('datas.txt')

for data in arquivo:
    dia_data1 = int(mais_recente[:2])
    dia_data2 = int(data[:2])
    mes_data1 = int(mais_recente[3:5])
    mes_data2 = int(data[3:5])
    ano_data1 = int(mais_recente[6:])
    ano_data2 = int(data[6:])

    if ano_data1 > ano_data2:
        mais_recente =  mais_recente
    elif ano_data1 < ano_data2:
        mais_recente =  data
    elif mes_data1 > mes_data2:
        mais_recente =  mais_recente
    elif mes_data1 < mes_data2:
        mais_recente =  data
    elif dia_data1 > dia_data2:
        mais_recente =  mais_recente
    else:
        mais_recente =  data

print(mais_recente, end='')
