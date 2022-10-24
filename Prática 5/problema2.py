string = input("")

i = 0

while i < len(string):
    c = i + 1
    if c < len(string):
        if string[i] == string[c]:
            a = string[i] + string[c]
            b = string[i].upper
            
            string = string.replace(a, b)
    i += 1

print(string)
