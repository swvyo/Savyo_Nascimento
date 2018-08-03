p1, p2 = input().split()

vog = ["a", "e", "i", "o", "u"]

pcripto = ""

for i in range(len(p1)):
    if p1[i] not in vog and p1[i] == p2[i]:
        pcripto = pcripto + str(i)
    elif i % 2 == 0:
        pcripto = pcripto + p1[i].upper()
    else:
        pcripto = pcripto + "!!"
        
print(pcripto)
