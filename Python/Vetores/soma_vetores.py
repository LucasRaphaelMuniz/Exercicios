n = int(input("Quantos valores vai ter cada vetor? "))
vetA = [0 for x in range(n)]
vetB = [0 for x in range(n)]
vetC = [0 for x in range(n)]

for i in range(0, n):
    vetA[i] = float(input("Digite os valores do vetor A: "))

for i in range(0, n):
    vetB[i] = float(input("Digite os valores do vetor B: "))

print(f"VETOR RESULTANTE: ")
for i in range(0, n):
    vetC[i] = vetA[i] + vetB[i]
    print(f"{vetC[i]:.0f}")