from random import randint
from time import sleep
print('\033[1mVAMOS JOGAR PAR OU IMPAR? PENSE EM UM NÚMERO DE 1 À 10')
soma = count = total = 0
escolha = ''
while True:
    computador = randint(1, 10)
    n = int(input('\033[mDigite um número: '))
    soma = n + computador
    escolha = str(input('\033[mVocê quer ímpar ou par? [I/P]: ')).strip().upper()[0]
    if escolha == 'P':
        if soma % 2 == 0:
            count += 1
            print(f'\033[32mPARABÉNS! O computador escolheu {computador} e você escolheu {n},\na soma desses números é {soma} PAR!')
            sleep(1)
            print('\033[36mVamos uma revanche...')
        else:
            print(f'\033[33mVOCÊ perdeu! O computador escolheu {computador} e você escolheu {n}, \na soma desses números é {soma} IMPAR')
            break
    if escolha == 'I':
        if soma % 2 != 0:
            count += 1
            print(f'\033[32mPARABÉNS! O computador escolheu {computador} e você escolheu {n},\na soma desses números é {soma} IMPAR!')
            sleep(1)
            print('\033[36mVamos uma revanche...')
        else:
            print(f'\033[33mVOCÊ perdeu! O computador escolheu {computador} e bocê escolheu {n}, \na soma desses números é {soma} PAR')
            break
if count == 1:
    print(f'\033[1;31mGAME OVER! você ganhou do computador apenas {count} vez')
if count == 0:
    print(f'\033[1;31mGAME OVER! Você perdeu feio pro computador')
if count >= 2:
    print(f'\033[1;31mGAME OVER! Você ganhou {count} vezes do computador')