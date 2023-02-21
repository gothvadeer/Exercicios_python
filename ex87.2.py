matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(5):
    for c in range(3):
        matriz[l][c] = str(input(f'Digite o valor de [{l},{c}]: '))
for l in range(5):
    for c in range(3):
        print(f'[{matriz[l][c]: ^20}]\t', end='')
    print()