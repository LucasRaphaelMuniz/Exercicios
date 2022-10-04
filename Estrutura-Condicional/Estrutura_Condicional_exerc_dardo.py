dardo1 = float(input("Primeiro valor: "))
dardo2 = float(input("Segundo valor: "))
dardo3 = float(input("Terceiro valor: "))

if dardo1 > dardo2 and dardo1 > dardo3:
    print(f"MAIOR DISTANCIA = {dardo1:.2f}")
elif dardo2 > dardo3:
    print(f"MAIOR DISTANCIA = {dardo2:.2f}")
else:
    print(f"MAIOR DISTANCIA = {dardo3:.2f}")