n = int(input("Quantas pessoas serao digitadas? "))
nome = [0 for x in range(n)]
idade = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}° pessoa:")
    nome[i] = input("Nome:")
    idade[i] = float(input("Idade:"))

maior = idade[0]

for i in range(1, n):
    if idade[i] > maior:
        maior = idade[i]
        nrpessoa = i

print(f"PESSOA MAIS VELHA: {nome[nrpessoa]}")