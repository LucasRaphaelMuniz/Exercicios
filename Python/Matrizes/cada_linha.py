m = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(m)] for x in range(m)]

for i in range(0, m):
    for j in range(0, m):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))


print("MAIOR ELEMENTO DE CADA LINHA: ")

for i in range(0, m):
    maior = 0
    for j in range(0, m):
        if mat[i][j] > maior:
            maior = mat[i][j]
    print(maior)