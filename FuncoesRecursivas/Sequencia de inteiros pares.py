def pares(num):
	num = num - 1
	if num>0:
		pares(num)
	if num%2 == 0:
		print(num)

num = int(input())
num = num + 1
pares(num)
