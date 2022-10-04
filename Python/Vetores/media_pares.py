n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

soma = 0
contPares = 0

for i in range(0, n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        contPares = contPares + 1
    
if contPares == 0:
    print("NENHUM NUMERO PAR")
else:
    media = soma / contPares
    print(f"MEDIA DOS PARES = {media:.1f}")
