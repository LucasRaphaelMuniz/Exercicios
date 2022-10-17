m = int(input("Quantas linhas vai ter a matriz? "))
n = int(input("Quantas colunas vai ter a matriz? "))
mat = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    print(f"Digite os elementos da {i+1}° linha:")
    for j in range(0, n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("VALORES NEGATIVOS:")

for i in range(0, m):
    for j in range(0, n):
        if mat[i][j] < 0:
            print(mat[i][j])