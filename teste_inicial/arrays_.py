c = 0

tam = input()
tam = tam.split()
cn = input()
cn = cn.split()
listaa = input()
listaa = listaa.split()
listab = input()
listab = listab.split()

menor = int(cn[0])

for i in range(0,int(cn[0])):
    aux = listaa[i]
    for i in range(0,int(cn[1])):
        if aux<listab[i]:
            c+=1
        else:
            c = 0
if c >= menor:
    print("YES!")
else:
    print("NO!")
