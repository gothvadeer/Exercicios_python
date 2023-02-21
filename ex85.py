lista = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Valores pares: {sorted(lista[0])}')
print(f'Valores ímpares: {sorted(lista[1])}')
