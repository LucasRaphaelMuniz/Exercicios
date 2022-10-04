HoraInicial = int(input("Hora inicial: "))
HoraFinal = int(input("Hora final: "))

if HoraInicial < HoraFinal:
    duracao = HoraFinal - HoraInicial
else:
    duracao = 24 - HoraInicial + HoraFinal

print(f"O JOGO DUROU {duracao} HORA(S) ")