m = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(m)] for x in range(m)]

for i in range(0, m):
    for j in range(0, m):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

soma = 0

for i in range(0, m):
    for j in range(i+1, m):
        soma = soma + mat[i][j]

print(f"MAIOR ELEMENTO DE CADA LINHA: {soma}")