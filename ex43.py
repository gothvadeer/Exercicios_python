from random import choice
from time import sleep

print('\033[36m=*' * 10)
print('\033[1;33mVAMOS JOGAR!')
sleep(0.3)
print('\033[1;34mPEDRA...')
sleep(0.5)
print('PAPEL...')
sleep(0.5)
print('TESOURA!')
sleep(0.8)
print('\033[36m=*' * 10)
print(f'''\033[1;37mDIGITE [1] PARA PEDRA')
DIGITE [2] PARA PAPEL')
DIGITE [3] PARA TESOURA''')
escolha = int(input('\033[mDigite sua escolha: '))
random = choice(['PEDRA', 'PAPEL', 'TESOURA'])

if escolha == 1:
    if random == 'PEDRA':
        print(f'\033[1;33mEMPATE! VOCÊ E O COMPUTADOR ESCOLHERAM PEDRA!')
    elif random == 'PAPEL':
        print(f'\033[1;31mO COMPUTADOR ESCOLHEU PAPEL, VOCÊ PERDEU!')
    elif random == 'TESOURA':
        print(f'\033[1;32mO COMPUTADOR ESCOLHEU TESOURA, VOCÊ GANHOU!')
if escolha == 2:
    if random == 'PAPEL':
        print(f'\033[1;33mEMPATE! VOCÊ E O COMPUTADOR ESCOLHERAM PAPEL')
    elif random == 'PEDRA':
        print(f'\033[1;32mO COMPUTADOR ESCOLHEU PEDRA, VOCÊ GANHOU!')
    elif random == 'TESOURA':
        print(f'\033[1;31mO COMPUTADOR ESCOLHEU TESOURA, VOCÊ PERDEU!')
if escolha == 3:
    if random == 'TESOURA':
        print(f'\033[1;33mEMPATE! VOCÊ E O COMPUTADOR ESCOLHERAM TESOURA!')
    elif random == 'PEDRA':
        print(f'\033[1;31mO COMPUTADOR ESCOLHEU PEDRA, VOCÊ PERDEU!')
    elif random == 'PAPEL':
        print(f'\033[1;32mO COMPUTADOR ESCOLHEU PAPEL, VOCÊ GANHOU!')