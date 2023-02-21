temporaria = []
pessoas = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')).strip().upper())
    temporaria.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    pessoas.append(temporaria[:])
    temporaria.clear()
    q = ' '
    while q not in 'SN':
        q = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if q not in 'SN':
            print('OPÇÂO INVÁLIDA')
    if q == 'N':
        break
print(f'A lista tem {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso é de {maior:.f}KG e quem tem esse peso é: ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso é de {menor:.2f}KG e quem tem esse peso é: ', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
