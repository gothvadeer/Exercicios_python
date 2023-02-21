lista_geral = []
pessoas = []
while True: #minha solução para o problema
    lista_geral.append(str(input('Nome: ')).strip().upper())
    lista_geral.append(float(input('Peso: ')))
    pessoas.append(lista_geral[:])
    lista_geral.clear()
    q = ' '
    while q not in 'SN':
        q = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if q not in 'SN':
            print('OPÇÃO INVÁLIDA!')
    if q == 'N':
        break
print(f'Há {len(pessoas)} pessoas cadastradas')
print(f'As pessoas mais pesadas são: ', end=' ')
for p in pessoas:
    if p[1] >= 80:
        print(f'{p[0]} com {p[1]:.2f}KG...', end=' ')
print(f'\nAs pessoas mais leves são: ', end=' ')
for p in pessoas:
    if p[1] <= 70:
        print(f'{p[0]} com {p[1]:.2f}', end=' ')
