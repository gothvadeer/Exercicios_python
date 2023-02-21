print(f'\033[33m=*'*20)
print(f"\033[36m{'VERIFICADOR DE NÚMEROS PRIMOS' : ^40}")
print(f'\033[33m=*'*20)

n = int(input('\033[mDigite um número: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end='')
        s += 1
    else:
        print('\033[32m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[34mO número {n} pode ser dividido {s} vezes!', end=' ')
if s == 2:
    print('\033[1;33mÉ um número primo!')

