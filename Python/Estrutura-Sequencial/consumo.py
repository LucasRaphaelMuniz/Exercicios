from turtle import distance


distancia = float(input("Distancia percorrida: "))
combustivel = float(input("Combustível gasto: "))

media = distancia / combustivel

print(f"Consumo medio = {media:.3f}")