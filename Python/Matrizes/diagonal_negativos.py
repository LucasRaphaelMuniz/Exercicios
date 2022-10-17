m = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(m)] for x in range(m)]

for i in range(0, m):
    for j in range(0, m):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL:")

for i in range(0, m):
    print(f"{mat[i][i]} ", end="")
print()

cont = 0

for i in range(0, m):
    for j in range(0, m):
        if mat[i][j] < 0:
            cont = cont+1

print(f"QUANTIDADE DE NEGATIVOS = {cont}")
