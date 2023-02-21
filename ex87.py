matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = maior  = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor de [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            coluna += matriz[l][c]
        if l == 1:
           maior = max(matriz[l])
print('=*'*20)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]: ^5}]\t', end='')
    print()
print('=*'*20)
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {coluna}')
print(f'O maior valor da linha dois é: {maior}')
