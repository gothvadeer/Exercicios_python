import random
from time import sleep
lista = []
print('=*'*20)
print(f"{'JOGO DA MEGA SENA DA VIRADA': ^40}")
print('=*'*20)
num = int(input('Quantos jogos você quer jogar?: '))
for pos in range(num):
    print(f'JOGO {pos+1}: ', end='')
    lista = list(random.sample(range(1, 60), 6))
    sleep(1)
    print(f'{sorted(lista)}')
print(f"{'BOA SORTE':=^40}")