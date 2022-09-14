import time

x = int(input("Digite o valor do tempo em segundos: "))

h = time.gmtime(x).tm_hour
m = time.gmtime(x).tm_min
s = time.gmtime(x).tm_sec

print("Valor convertido: {} h {} min {} s".format(h, m, s))
