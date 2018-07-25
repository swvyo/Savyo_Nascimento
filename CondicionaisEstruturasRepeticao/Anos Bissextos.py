ano = input()
lista = ano.split()

lista_ano = []

c = 0

y1 = int (lista[0])
y2 = int (lista[1])

for i in range (y1, y2):
    if i%1000 == 0:
        cont = i+1
        lista_ano.append(i)
    if (i%4 == 0 and i%100 != 0) or (i%4 != 0 and i%400 == 0):
        lista_ano.append(i)
        cont = i+1

if cont == 0:
    print ("-1")

else:
    for i in range (len(lista_ano)):
        print (lista_ano[i])


