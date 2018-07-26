lp2 = input()
lp3 = input()

liste = []

listab = lp3.split()
listaa = lp2.split()



for i in range (len(listaa)):
	ax = listaa[i]
	for j in range(len(listab)):
		ax2 = listab[j]
		if ax == ax2:
			liste.append(ax)
			
for i in range(len(liste)):
	print(liste[i], end =" ")

