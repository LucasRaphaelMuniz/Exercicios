n = int(input("Quantas Alunos serao digitadas? "))
nomes = [0 for x in range(n)]
nota1 = [0 for x in range(n)]
nota2 = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados do {i+1}° aluno:")
    nomes[i] = input("Nome:")
    nota1[i] = float(input("1° Nota: "))
    nota2[i] = float(input("2° Nota: "))
    média = nota1[i] + nota2[i]

print("Alunos Aprovados: ")
for i in range(0, n):
    média = (nota1[i] + nota2[i]) / 2
    if média >= 6:
        print(nomes[i])