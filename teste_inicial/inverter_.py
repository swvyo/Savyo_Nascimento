n = 1
while n != 0:
    n = int(input ())
    if n == 0:
        break
    inverte = 0
    num2 = n
    a = '['
    f = ']'
    while num2 > 0:
        inverte *= 10        
        inverte = num2 % 10
        num2 //= 10
        print("%c%d%c" %(a,inverte,f),end='')
    print()
