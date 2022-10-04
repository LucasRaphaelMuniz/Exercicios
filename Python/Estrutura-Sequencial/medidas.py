a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

AreaQuadrado = a * a
AreaTriangulo = a * b / 2
AreaTrapezio = (a + b) * c / 2

print(f"AREA DO QUADRADO = {AreaQuadrado:.4f}")
print(f"AREA DO TRIANGULO = {AreaTriangulo:.4f}")
print(f"AREA DO TRAPEZIO = {AreaTrapezio:.4f}")
