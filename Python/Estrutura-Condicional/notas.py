#Problema "notas"

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: : "))

NotaFinal = nota1 + nota2

print(f"NOTA FINAL = {NotaFinal}")

if NotaFinal < 60:
    print("REPROVADO")
else:
    print("APROVADO")

    