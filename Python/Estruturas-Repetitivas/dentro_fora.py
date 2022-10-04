x = int(input("Quantos numeros voce vai digitar? "))

dentro = 0
fora = 0

for i in range(0, x):
    y = int(input("Digite um numero: "))
    if y <= 20 and y >= 10:
        dentro = dentro + 1
    else:
        fora = fora + 1

print(f"{dentro} DENTRO")
print(f"{fora} FORA")