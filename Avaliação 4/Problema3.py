def v_atual (tempo): #Retorna a velocidade em um determinado momento, fazendo V = Vo + at
    return float(v_inicial + (a*tempo))

def s_atual (tempo): #Retorna a posição em um determinado momento, fazendo S = So +Vot + (at^2)/2
    return float(s_inicial + (v_inicial*tempo)+((a/2)*(tempo**2)))

v_inicial = float(input("Digite a velocidade inicial: ")) #Velocidade Inicial
s_inicial = float(input("Digite a posição inicial: ")) #Posição inicial
a = float(input("Digite a aceleração: ")) #Aceleração
t = int(input("Digite os segundos a serem avaliados: ")) #Segundos a serem avaliados

for i in range(t): #Calcula e imprime os valores da velocidade e posição para cada segundo entre 0 e t-1
    print(f"t = {i} s; V = {v_atual(i):.1f} m/s; S = {s_atual(i):.1f} m")
