from ast import Break


print('Digite dois numeros:')
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print("CRESCENTE")
        break
    else:
        print("DECRESCENTE")
        break
