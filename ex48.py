print(f"\033[1;36m{'SOMA ENTRE NÚMEROS PARES':=^40}")

s = 0
count = 0
for c in range(1,7):
    n = int(input('\033[mDigite um número: '))
    if (n%2) == 0:
        s += n
        count += 1
print(f'\033[1;33mA SOMA ENTRE OS {count} NÚMEROS PARES DIGITADOS É: {s}')