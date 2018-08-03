num_romano = input()

val = {"0": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
ant = "0"
total = 0
aux = 0

for num in num_romano:
    if num == ant:
        aux = aux + val[num]
    else:
        if val[num] > val[ant]:
            total = total - aux
        else:
            total = total + aux
        aux = val[num]
        ant = num
        
total = total + aux

if total % 5 == 0:
    print("O número é múltiplo de 5!")
else:
    print("O resto da divisão por 5 do numero dado é {}.".format(total % 5))
