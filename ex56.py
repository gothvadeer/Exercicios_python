from random import randint
from time import sleep

print('\033[35m=*\033[35m'*23)
print(f'''\033[1;36m{'UPGRADE DO JOGO #26!!!':^40}
{'PENSE EM UM NÚMERO DE 1 À 10' :^40}''')
print('\033[35m=*\033[m'*23)

random = randint(1, 10)
count = 0

n = int(input('NÚMERO: '))
print('\033[1;32mPROCESSANDO...\033[m')
sleep(1)
while n != random:
    if n > random:
        print('\033[31mVOCÊ ERROU! PENSE EM UM NÚMERO MENOR')
    if n < random:
        print('\033[31mERROU! PENSE MAIS ALTO')
    n = int(input('\033[mNÚMERO: '))
    print('\033[1;32mPROCESSANDO...\033[m')
    sleep(1)
    count += 1
if n == random:
    print(f'\033[1mPARABÉNS, VOCÊ GANHOU!  O NÚMERO ESCOLHIDO FOI:\033[7;40m{random}\033[m')
if count >= 2:
    print(f'Você levou {count} tentativas para acertar!')
else:
    print(f'\033[1mUAU! DE PRIMEIRA! você levou apenas UMA tentativa para acertar!')

