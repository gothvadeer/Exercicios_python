print(f"\033[1;36m{'PROGRESSÃO ARITMÉTICA:' :=^40}")

pt = int(input('\033[mDigite o primeiro termo: '))
r = int(input('Digite a razão: '))
limite = int(input('Digite quantos termos deseja ver: '))
termo = pt
pa = 1

while pa <= limite:
    print(f' -> {termo}', end='')
    termo += r
    pa += 1
print('FIM')
