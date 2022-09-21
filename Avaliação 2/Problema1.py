a1 = float(input("Digite o primeiro arremesso: "))
a2 = float(input("Digite o segundo arremesso: "))
a3 = float(input("Digite o terceiro arremesso: "))

pont = 0
if a1 == -1:
    pont += 1
elif a1 > 7.24:
    pont += 3
elif a1 <= 7.24:
    pont += 2
    
if a2 == -1:
    pont += 1
elif a2 > 7.24:
    pont += 3
elif a2 <= 7.24:
    pont += 2
    
if a3 == -1:
    pont += 1
elif a3 > 7.24:
    pont += 3
elif a3 <= 7.24:
    pont += 2
    
print("Pontuação:", pont)
