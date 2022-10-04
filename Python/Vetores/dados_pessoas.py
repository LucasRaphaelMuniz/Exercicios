n = int(input("Quantas Alunos serao digitadas? "))
altura = [0 for x in range(n)]
genero = [0 for x in range(n)]

for i in range(0, n):
    altura[i] = float(input(f"Altura da {i+1}° pessoa: "))
    genero[i] = input(f"Genero da {i+1}° pessoa: ")

MenorAltura = altura[0]
MaiorAltura = altura[0]

for i in range(0, n):
    if altura[i] < MenorAltura:
        MenorAltura = altura[i]

    if altura[i] > MaiorAltura:
        MaiorAltura = altura[i]

print(f"Menor altura = {MenorAltura}")
print(f"Maior altura = {MaiorAltura}")


soma = 0
contM = 0

for i in range(0, n):
    if genero[i] == "F":
        soma = soma + altura[i]
        contM = contM + 1


if contM == 0:
    print("Impossivel calcular a altura media das mulhers")
else:
    media = soma / contM
    print(f"Media das alturas da mulheres: {media:.2f}")

contH = n - contM

print(F"Numero de homens = {contH}")