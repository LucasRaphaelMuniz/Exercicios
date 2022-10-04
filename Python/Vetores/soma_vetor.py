n = int(input("Quantos numeros vc vai digitar? "))
vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

print(f"VALORES = ", end=" ")

for i in range(0, n):
    print(vet[i], end=" ")
    

soma = 0
print()
for i in range(0, n):
    soma = soma + vet[i]

print(f"SOMA = {soma}")
media = soma / n
print(f"MEDIA = {media}")

