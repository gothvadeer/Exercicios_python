n = int(input('Quantos termos deseja ver? '))
t1 = 0
t2 = 1
count = 3
print(f'{t1} -> {t2}', end='')
while count <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end=' ')
    t1 = t2
    t2 = t3
    count += 1
print(' -> FIM')
