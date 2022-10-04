minutos = int(input("Digite a quantidade de minutos: "))

if minutos <= 100:
    print("Valor a pagar: R$ 50.00 ")
else:
    vlr_pagar = (minutos - 100) * 2 + 50
    print(f"Valor a pagar: R$ {vlr_pagar:.2f}")