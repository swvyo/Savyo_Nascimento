valr = int(input())
aux = False
num = []
for x in range(1, valr):
    if int(x) * int(x + 1) * int(x + 2) == valr:
        aux = True
        num.append(x)
        num.append(x + 1)
        num.append(x + 2)
        break
if aux:
    print("{} * {} * {} = {}".format(num[0], num[1], num[2], valr))
    print("Verdadeiro")
elif not aux:
    print("Falso")

