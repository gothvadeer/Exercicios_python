num = []
for c in range(5):
    n = int(input('Digite o número: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('O número foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'O número foi adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem ficam {num}')