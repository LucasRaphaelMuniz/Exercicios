salarioAtual = float(input("Digite o salario da pessoa: "))

if salarioAtual <= 1000:   
    porcentagem = 20
elif salarioAtual <= 3000: 
    porcentagem = 15
elif salarioAtual <= 8000: 
    porcentagem = 10
else: 
    porcentagem = 5

aumento = salarioAtual * (porcentagem/100)
salarioNovo = salarioAtual + aumento

print(f"Novo salario = R$ {salarioNovo:.2f}")
print(f"Aumento = R$  {aumento:.2f}")
print(f"Porcentagem = {porcentagem:.2f} %")





