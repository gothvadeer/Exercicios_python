palavras = []
vogais = 'AÁÂÃÀEÉÊIÍOÔÕÓUÚ'
tupla = ''
v = 0
while True:
    p = str(input('Digite uma palavra: ')).strip().upper()
    palavras.append(p)
    tupla = tuple(palavras)
    q = ' '
    while q not in 'SN':
        q = str(input('Deseja digitar mais palavras? [S/N]: ')).upper().strip()[0]
        if q not in 'SN':
            print('OPÇÃO INVÁLIDA')
    if q == 'N':
        break
for palavra in tupla:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for vogal in palavra:
        if vogal in vogais:
            print(f'{vogal}', end=' ')
            v += 1
print(f'\nForam digitadas {len(tupla)} palavras e foram encontradas {v} vogais')