numero = int(input())
inicio = 0
quadrado = 5
passo_a_mais = 3
i = 1

while (i*i<=numero/2):
	if ((numero-quadrado)%passo_a_mais == 0):
		inicio = inicio + 1
	quadrado = quadrado + 3
	passo_a_mais = passo_a_mais + 2
	i= i + 1
	
print(inicio)
