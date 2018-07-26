n1 = int(input(""))
n2 = int(input(""))

lista = []

L1 = []
L2 = []

for i in range(1,50):
        if (i*n1) < 50:
                L1.append(i*n1)
        else:
                break

for x in range (1,50):
        if (x*n2) < 50:
                L2.append(x*n2)
        else:
                break

for i in range (len(L1)):
        ax = L1[i]
        for y in range (len(L2)):
                ax2 = L2[y]
                if ax == ax2 and ax not in lista:
                        lista.append(ax)

print (len(lista))
