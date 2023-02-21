s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        s += c
print(f'\033[1mA soma dos {count} valores solicitados é: {s}')
