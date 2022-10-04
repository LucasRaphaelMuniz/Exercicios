vlr_unitario = float(input("Preço unitário do produto: "))
qtde = int(input("Quantidade comprada: "))
vlr_recebido = float(input("Dinheiro recebido: "))

troco = vlr_recebido - (vlr_unitario * qtde)

if troco > 0:
    print(f"TROCO = {troco:.2f}")
else:
    troco = troco * -1
    print(f"DINHEIRO INSUFICIENTE. FALTAM {troco:.2f} REAIS")