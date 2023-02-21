print(f"\033[1m{'LEITOR DE FATORIAIS':=^40}")

n = int(input('\033[mEscolha um número: '))
fato = 1
c = n
print(f'Calculando o fatorial de {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fato *= c
    c -= 1
print(f'{fato}')


