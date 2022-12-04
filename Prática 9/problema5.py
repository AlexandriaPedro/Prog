dicionario_aminioacido = {'UUU': 'Phe', 'CUU': 'Leu', 'UUA': 'Leu', 'AAG': 'Lisina', 'UCU': 'Ser', 'UAU': 'Tyr', 'CAA': 'Gln'}

dicionario = dict()
lista = list()

rna = str(input("Digite o RNA: "))

rna = list(rna)

tamanho_rna = len(rna)

numero_de_divisoes = int(tamanho_rna / 3)

aux = 3

for i in range(1, numero_de_divisoes):
    rna.insert(aux, '-')
    
    aux += 4


rna = ''.join(rna)


for i in range(0, len(dicionario_aminioacido)):
    for x, y in dicionario_aminioacido.items():
        rna = rna.replace(x, y)

print("Cadeia de Aminoácidos: {}".format(rna))
