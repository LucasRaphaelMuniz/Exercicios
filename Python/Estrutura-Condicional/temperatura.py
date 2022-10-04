from this import d


unidade = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if unidade == "F":
    F = float(input("Digite a temperatura em Fahrenheit: "))
    C = 5 / 9 * (F - 32)
    print(f"Temperatura equivalente em Celsius: {C:.2F}")
else:
    C = float(input("Digite a temperatura em Celsius: "))
    F = 9 * C / 5 + 32
    print(f"Temperatura equivalente em Fahrenheit: {F:.2F}")
