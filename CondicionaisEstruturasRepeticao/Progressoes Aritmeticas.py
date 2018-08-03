p_a = [int(x) for x in input().split()]

i = 0

cont = 1

while i < len(p_a) - 2:
    if abs(p_a[i] - p_a[i + 1]) != abs(p_a[i + 1] - p_a[i + 2]):
        cont = i + 1
        i = i + 1
    i = i + 1
    
print(cont)
