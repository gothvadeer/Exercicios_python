lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
        if q not in 'SN':
            print('OPÇÂO INVÁLIDA')
    if q == 'N':
        break
print(f'A lista completa digitada: {lista}')
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    elif i % 2 == 1:
        impares.append(i)
print(f'Os números pares da lista são: {pares}')
print(f'Os números impares da lista são: {impares}')