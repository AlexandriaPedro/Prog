def mdc (x, y):
    if (y == 0):
        return x
    else:
        return(mdc(y, x % y))

x = int(input("Digite x: "))
y = int(input("Digite y: "))

resp = mdc(x, y)
print(resp)
