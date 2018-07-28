peso = int(input())
c = 1
peso2 = []

peso2.append(peso)
s = peso

while c < 7 and peso!=0 and s < 560:
	peso = int(input())
	s = s + peso
	peso2.append(peso)
	c = c + 1

if c >= 7:
	print("Limite de pessoas Atingido")
	
c2 = 0
s2 = 0

for i in range(len(peso2)):
	if (s + peso2[i])<560:
		s += peso2[i]
		c2 = c2 + 1
	else:
		break

print(' {}\n{}'.format(c2,s))
