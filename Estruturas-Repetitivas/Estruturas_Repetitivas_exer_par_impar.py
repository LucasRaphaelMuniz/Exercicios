x = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, x):
    y = int(input("Digite um numero: "))
    if y == 0:
        print("NULO")
    else:
        if y % 2 == 0:
            if y < 0:
                print("PAR NEGATIVO") 
            else:
                print("PAR POSITIVO")
        else:
            if y < 0:
                print("IMPAR NEGATIVO") 
            else:
                print("IMPAR POSITIVO")                
