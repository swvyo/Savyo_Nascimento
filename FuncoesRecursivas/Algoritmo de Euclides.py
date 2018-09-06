def eucli(a,e):
	a = max(c,e)
	b = min(c,e)
	if(a%b == 0):
		return b
	else:
		return eucli(b,(a%b))

n = int(input())
cont = 0

while cont<n:
	cont = cont + 1
	c,e = list(map(int,input().split()))
	print("MDC({},{}) = {}".format(c,e,eucli(c,e)))
