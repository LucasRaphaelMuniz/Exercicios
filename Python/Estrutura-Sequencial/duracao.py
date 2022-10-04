duracao = int(input("Digite a duracao em segundos: "))

horas = int(duracao / 3600)
resto = duracao % 3600

minutos = int(resto / 60)
segundos = int(resto % 60)

print(f"Horas: {horas:02.0f}:{minutos:02.0f}:{segundos:02.0f}")

