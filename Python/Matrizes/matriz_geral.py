m = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(m)] for x in range(m)]

for i in range(0, m):
    for j in range(0, m):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

soma = 0

for i in range(0, m):
    for j in range(0, m):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]

print(f"SOMA DOS POSITIVOS: {soma:.1f}")

linha = int(input("Escolha uma linha: "))


print(f"LINHA ESCOLHIDA: ", end="")
for j in range(0, m):
    print(f"{mat[linha][j]:.1f} ", end="")
print("")
print("")

coluna = int(input("Escolha uma coluna: "))
print(f"COLUNA ESCOLHIDA: ", end="")

for i in range(0, m):    
    print(f"{mat[i][coluna]:.1f} ", end="")
print("")
print("")

print("DIAGONAL PRINCIPAL: ", end="")
for i in range(0, m):
    print(f"{mat[i][i]:.1f} ", end="")
print("")
print("")

for i in range(0, m):
    for j in range(0, m):
        if mat[i][j] < 0:
            mat[i][j] = mat[i][j] ** 2

print("MATRIZ ALTERADA: ")

for i in range(0, m):
    for j in range(0, m):
        print(f"{mat[i][j]:.1f} ", end="")
    print()