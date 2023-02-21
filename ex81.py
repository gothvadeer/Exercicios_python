lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    q = ' '
    while q not in 'SN':
        q = str(input('Deseja continuar? [S/N]:  ')).strip().upper()[0]
        if q not in 'SN':
            print('OPÇÃO INVÁLIDA')
    if q == 'N':
        break
print(f'Foram {len(lista)} valores inseridos\nA lista em ordem decrescente fica {sorted(lista, reverse= True)}')
if 5 in lista:
    print('O valor 5 está incluso na lista!')
else:
    print('O valor 5 não está inserido na lista')
