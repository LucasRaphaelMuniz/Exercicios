codigo = int(input("Codigo do produto comprado: "))
qtde = int(input("Quantidade comprada: "))

match codigo:
    case 1:
        vlr = qtde * 5
        print(f"Valor a pagar: R$ {vlr:.2f}")
    case 2:
        vlr = qtde * 3.5
        print(f"Valor a pagar: R$ {vlr:.2f}")
    case 3:
        vlr = qtde * 4.8
        print(f"Valor a pagar: R$ {vlr:.2f}")
    case 4:
        vlr = qtde * 8.9
        print(f"Valor a pagar: R$ {vlr:.2f}")
    case 5:
        vlr = qtde * 7.32
        print(f"Valor a pagar: R$ {vlr:.2f}")



