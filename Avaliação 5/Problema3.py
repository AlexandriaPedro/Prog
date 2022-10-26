nome = input("Nome completo do aluno: ")
nome = nome.upper()

posPrimeiroNome = nome.find(' ') #primeiro espaço
primeiroNome = nome[0:posPrimeiroNome]

posSobrenome = nome.rfind(' ') #ultimo espaço
sobrenome = nome[posSobrenome+1:len(nome)]

restanteNome = nome[posPrimeiroNome:posSobrenome]
primeiraletra = ''

for i in range(len(restanteNome)):
    if restanteNome[i] == ' ':
        primeiraletra += restanteNome[i+1]       

print("Login:", primeiroNome + primeiraletra + sobrenome)
