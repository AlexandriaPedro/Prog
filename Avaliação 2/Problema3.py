preco = float(input('Digite o valor da hora de trabalho: '))
horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

s_bruto = preco * horas
ir = 0.0

if s_bruto > 2500:
    ir = s_bruto * 0.2
elif s_bruto > 1500:
    ir = s_bruto * 0.1
elif s_bruto > 900:
    ir = s_bruto * 0.05
    
fgts = s_bruto * 0.11
inss = s_bruto * 0.1
descontos = ir + inss
s_liq = s_bruto - descontos

print ('Salário Bruto: R$ %.2f' % s_bruto)
print ('IR: R$ %.2f' % ir)
print ('INSS: R$ %.2f' % inss)
print ('FGTS: R$ %.2f' % fgts)
print ('Total de descontos: R$ %.2f' % descontos)
print ('Salário líquido: R$ %.2f' % s_liq)
