n = int(input("Serao digitados dados de quantos produtos? "))
nome = [0 for x in range(n)]
precoCompra = [0 for x in range(n)]
precoVenda = [0 for x in range(n)]

lucro = 0

for i in range(0, n):
    print(f"Produto {i+1}:")
    nome[i] = input("Nome: ")
    precoCompra[i] = float(input("Preco de compra: "))
    precoVenda[i] = float(input("Preco de venda: "))

abaixo = 0
entre = 0
acima = 0

for i in range(0, n):
    lucro = precoVenda[i] - precoCompra[i]
    precentualLucro = lucro * 100 / precoCompra[i]

    if precentualLucro < 10:
        abaixo = abaixo + 1
    else:
        if precentualLucro <= 20:
            entre = entre + 1
        else:
            acima = acima + 1

totalCompra = 0
totalVenda = 0

for i in range(0, n):
    totalCompra = totalCompra + precoCompra[i]
    totalVenda = totalVenda + precoVenda[i]

totalLucro = totalVenda - totalCompra

print("RELATORIO")
print(f"Lucro abaixo de 10%: {abaixo:.0f}")
print(f"Lucro entre 10% e 20%: {entre:.0f}")
print(f"Lucro acima de 20%: {acima:.0f}")
print(f"Valor total de compra: {totalCompra:.2f}")
print(f"Valor total de venda: {totalVenda:.2f}")
print(f"Lucro total:{totalLucro:.2f}")


