n = int(input("Quantas pessoas serao digitadas? "))
nome = [0 for x in range(n)]
idade = [0 for x in range(n)]
altura = [0 for x in range(n)]



for i in range(0, n):
    print(f"Dados da {i+1}° pessoa:")
    nome[i] = input("Nome:")
    idade[i] = float(input("Idade:"))
    altura[i] = float(input("Altura:"))

soma = 0
for i in range(0, n):
    soma = soma + altura[i]
    
media = soma / n
print(f"Altura media: {media:.2f}")

cont = 0
for i in range(0, n):
    if idade[i] < 16:
        cont = cont + 1

porcentagem = cont * 100 / n

print(f"Pessoas com menos de 16 anos: {porcentagem:.1f}%")

for i in range(0, n):
    if idade[i] < 16:
        print(nome[i])
