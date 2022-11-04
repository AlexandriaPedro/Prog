nt = []
np = []
ni = []

for i in range(5):
    nt.append(int(input('')))
    if nt[i] % 2 == 0:
        np.append(nt[i])
    else:
        ni.append(nt[i])

print(nt)
print(np)
print(ni)
