conjA = []
conjB = []
sec = []

for i in range (0,20):
    n1 = int(input())
    conjA.append(n1)
    
for y in range (0,20):
    n2 = int(input())
    conjB.append(n2)

for z in range (0,20):
    for w in range (0,20):
        if (conjA[w]==conjB[z]):
            sec.append(conjA[w])

if (len (sec) == 0):
    print ("Vazio")
else:
    sec = list (set(sec))
    sec.sort()
    for x in range (0,len(sec)):
        print (sec[x])
