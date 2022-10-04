n = int(input("Quantos numeros voce vai digitar? "))
vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

print("NUMEROS PARES:", end=" ")

cont = 0
for i in range(0, n):
    if vet[i] % 2 == 0:
        print(f"{vet[i]:.0f}", end=" ")
        cont = cont + 1
print()
print(f"QUANTIDADE DE PARES = {cont}")