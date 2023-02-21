print('\033[36m=*'*20)
print(f"\033[1;35m{'PROGRESSÃO ARITMÉTICA': ^40}")
print(f"{'APERTE [ 0 ] PARA ENCERRAR O PROGRAMA': ^40}")
print('\033[36m=*'*20)

pt = int(input('\033[mDigite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
pa = 1
total = 0
q = 10
while q != 0:
    total += q
    while pa <= total:
        print(f' -> {termo}', end=' ')
        termo += r
        pa += 1
    print('\nPAUSA')
    q = int(input('Quantos termos deseja ver a mais?: '))
print(f'\033[1;31mFIM DO PROGRAMA, FORAM MOSTRADOS {total} TERMOS')








