unidade = float(input("Preço unitário do produto: "))
quantidade = float(input("Quantidade comprada:  "))
pago = float(input("Dinheiro recebido:  "))

troco = pago - (quantidade * unidade)

print(f"TROCO = R$ {troco:.2f}")


