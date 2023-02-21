num = []
while True:
    n = int(input('Digite um número: '))
    if n in num:
        print('Valores iguais, não poderá ser adicionado...')
        num.remove(n)
    else:
        print('Número adicionado com sucesso...')
    num.append(n)
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if q not in 'SN':
            print('OPÇÃO INVÁLIDA')
    if q == 'N':
        break
print(f'Os números digitados foram {sorted(num)}')