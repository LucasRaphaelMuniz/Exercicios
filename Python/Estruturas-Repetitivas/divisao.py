n = int(input("Quantos casos voce vai digitar? "))

for i in range(0, n):
    x = float(input("Entre com o numerador: "))
    y = float(input("Entre com o denominador: "))

    if y == 0:
        print("DIVISAO IMPOSSIVEL")
    else:
        divisao = x / y
        print(f"DIVISAO = {divisao}")