print(f"\033[1;36m{'PROGRESSÃO ARITMÉTICA' :=^40}")

pt = int(input('\033[mDigite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10-1) * r

for c in range(pt, decimo+r, r):
    print(f'{c}', end=' - ')
print('fim')
