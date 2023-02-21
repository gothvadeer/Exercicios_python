print('=*'*20)
print(f"{'LOJA BARATÃO': ^35}")
print('=*'*20)
total = caro = produtopreço = count = menor = 0
baratonome = ''
while True:
    produtonome = str(input('NOME do produto: ')).strip().upper()
    produtopreço = float(input('PREÇO do produto: R$ '))
    total += produtopreço
    pergunta = ' '
    count += 1
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if produtopreço > 1000:
        caro += 1
    if count == 1:
        menor = produtopreço
        baratonome = produtonome
    else:
        if produtopreço < menor:
            menor = produtopreço
            baratonome = produtonome
    if pergunta == 'N':
        break
print(f"{' FIM DO PROGRAMA ':-^40}")
print(f'O total de gasto na loja foi de: R$ {total:.2f}')
if caro == 1:
    print('Apenas um produto custa mais que 1000 reais')
if caro >= 2:
    print(f'{caro} produtos custam mais que R$ 1000 reais')
if caro == 0:
    print(f'Nenhum produto custa mais que 1000 reais')
print(f'O nome do produto mais barato é {baratonome} que custa R$ {menor}')







