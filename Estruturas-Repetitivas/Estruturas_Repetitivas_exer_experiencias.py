n = int(input("Quantos casos de teste serao digitados? "))

TotalRatos = 0
TotalSapos = 0
TotalCoelhos = 0

for i in range(0, n):
    qtde = int(input("Quantidade de cobaias: "))
    TpCobaia = str(input("Tipo de Cobaia: "))

    if TpCobaia == "R":
        TotalRatos = TotalRatos + qtde
    elif TpCobaia == "S":
        TotalSapos = TotalSapos + qtde
    else:
        TotalCoelhos = TotalCoelhos + qtde

TotalCobaias = TotalCoelhos + TotalRatos + TotalSapos

PercCoelhos = TotalCoelhos / TotalCobaias * 100
PercRatos = TotalRatos / TotalCobaias * 100
PercSapos = TotalSapos / TotalCobaias * 100

print("RELATORIO FINAL:")
print(f"Total: {TotalCobaias} cobaias")
print(f"Total de coelhos: {TotalCoelhos}")
print(f"Total de ratos: {TotalRatos}")
print(f"Total de sapos: {TotalSapos}")
print(f"Percentual de coelhos: {PercCoelhos:.2f}%")
print(f"Percentual de ratos: {PercRatos:.2f}%")
print(f"Percentual de sapos: {PercSapos:.2f}%")
