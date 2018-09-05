somaT = 0

quantM = 0
quantT = 0
quantC = 0


while True:
    animal = input()
    p = float (input())
    ps = input()
    if animal.lower() == "macaco":
        quantM = quantM + 1

    elif animal.lower() == "tigre":
        somaT = somaT + p
        quantT = quantT + 1

    elif animal.lower() == "cobra" and ps.lower() == "venezuela":
        quantC = quantC + 1

    ch = input()
    if ch.lower() == "parar":
        break

if quantT == 0:
    quantT = 1

print (quantM)

print ("%.2f" %(somaT/quantT))

print (quantC)
