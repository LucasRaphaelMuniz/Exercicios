print('Digite as idades: ')

soma = 0
cont = 0

idade = int(input())

while idade >= 0:
    soma = soma + idade
    cont = cont + 1
    idade = int(input())

if cont == 0:
    print("IMPOSSIVEL CALCULAR ")
else:
    media = soma / cont
    print(f"MÉDIA = {media:.2f}")