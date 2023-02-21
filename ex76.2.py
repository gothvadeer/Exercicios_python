products = [] #mesmo exercicio 76 usando listas
total = 0
while True:
    product = str(input('PRODUTO: ')).strip().upper()
    price = float(input('PREÇO: R$ '))
    total += price
    products.append((product, price))
    q = ' '
    while q not in 'SN':
        q = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if q not in 'SN':
            print('\033[1;31mOPÇÃO INVÁLIDA! Digite "S" para continuar ou "N" para sair do programa\033[m')
    if q == 'N':
        break
print('~' * 40)
print(f"{'LISTA DE COMPRAS': ^40}")
print('~' * 40)
for product, price in products:
    print(f'{product:.<30} R$ {price:.2f}')
print(f'O total da compra deu R$ {total:.2f}')
