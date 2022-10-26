frase = input("")

aux = ''
i = 0

while i < len(frase):
    if i + 1 < len(frase):
        if frase[i] == frase[i+1]:
            aux += frase[i].upper()
            i+=2
        else:
            aux += frase[i]
            i+=1
    else:
        aux += frase[i]
        break

print(aux.lstrip())
