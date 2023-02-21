n = s = count = 0
while True:
    n = int(input('Digite um número, [ 999 ] faz o programa parar: '))
    if n == 999:
        break
    s += n
    count += 1
print(f'A soma dos {count} valores é igual a: {s}')
