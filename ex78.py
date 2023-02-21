lista = []
for v in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Os números digitados foram: {lista}')
print(f'O maior número é: {max(lista)} que está na posição: ', end=' ')
for i, item in enumerate(lista):
    if item == max(lista):
        print(f'{i+1}ª...', end=' ')
print(f'\nO menor número é: {min(lista)} que está na posição: ', end=' ')
for i, item in enumerate(lista):
    if item == min(lista):
        print(f'{i+1}ª...', end=' ')