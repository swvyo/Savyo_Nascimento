c = "sim"
s = 0
	
while c != "não":
	n = int(input())
	c = input()
	c = c.lower()
	if(n<=2):
		s = s + (9*30)
	else:
		s = s + (6*30)

if s < 100:
    fralda = 1
    r = 0
elif s % 100 == 0:
    fralda = int(s/100)
    r = 100*fralda - s
else:
	fralda = int(s/100) + 1
	r = 100*fralda - s

print(fralda)
print(r)
