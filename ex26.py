from random import randint
from time import sleep

print('\033[35m=*\033[35m'*23)
print('\033[1;36mVAMOS JOGAR! PENSE EM UM NÚMERO DE 1 À 10...\033[m')
print('\033[35m=*\033[m'*23)

n = int(input('NÚMERO: '))
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)
random = randint(1, 10)
if n == random:
    print(f'\033[1mPARABÉNS, VOCÊ GANHOU! O NÚMERO ESCOLHIDO FOI:\033[7;40m{random}\033[m')
else:
    print(f'\033[1mVOCÊ PERDEU! O NÚMERO ESCOLHIDO FOI: \033[7;40m{random}\033[m')
