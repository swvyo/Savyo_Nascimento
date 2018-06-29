
continuar = input()
veloc = []
ano = []


if continuar != 'n' and continuar != 'N':
    while continuar != 'n' and continuar != 'N':
        ano.append(int(input()))
        veloc.append(float(input()))
        continuar = input()
    print(max(veloc))
    print(max(ano))
    print(sum(veloc) / len(veloc))
    
else:
    print("ZERO")
