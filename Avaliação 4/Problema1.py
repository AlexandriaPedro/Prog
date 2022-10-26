m = float(input("Insira a massa inicial: "))

t = 0 #acumuladordotempo
f = m #massa final

while f >= 0.5:
    t += 50
    f = f/2

print(f"Tempo necessário (em s): {t}")
print(f"Massa restante (em g): {f:.2f}")
