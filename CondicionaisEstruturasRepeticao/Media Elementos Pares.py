numlinha = input()

lista = []
s = []

listanume = numlinha.split()

for i in range(len(listanume)):
	lista.append(int(listanume[i]))
	
for i in range(len(lista)):
	if (lista[i] > 0) and (lista[i]%2 == 0):
		s.append(lista[i])
		
c = 0

for i in range(len(s)):
	c += s[i]

if c == 0:
	print("-1")

else:
	print(c/len(s)) 
