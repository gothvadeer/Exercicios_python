n = int(input('Digite um número: '))
fato = 1
c = n
for f in range(n, 0, -1):
    fato *= c
    c -= 1
print(f'O fatorial de {n}! é {fato}')
