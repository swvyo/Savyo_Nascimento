n = int(input())
num = input()

print(num[::-1])

lista3 = []

lista = num.split()
lista3.append(lista[1:len(lista)])
lista3.append(lista[0])

print(lista3)

lista2 = []

for i in range(len(lista)):
	lista2.append(int(lista[i]))

print(sorted(lista2, key=int, reverse=True))
