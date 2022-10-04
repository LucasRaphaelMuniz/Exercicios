n = int(input("Quantos numeros vc vai digitar? "))
vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))
    
print("NUMERO DIGITADOS:")
for i in range(0, n):
    print(f"{vet[i]:.1f}")