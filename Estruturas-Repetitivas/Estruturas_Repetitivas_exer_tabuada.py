from re import I


n = int(input("Deseja a tabuada para qual valor? "))

for i in range(1, 11):
    produto = n * i
    print(f"{n} x {i:02} = {produto:02}")