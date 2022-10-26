string = input()

vogais = 'aeiouAEIOU'

i = 0
for c in string:
    if c in vogais:
        print(i, c)
    i += 1
