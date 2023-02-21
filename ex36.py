n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 == n2:
    print(f'\033[1;31mNÃO EXISTE MAIOR NÚMERO, OS NÚMEROS DIGITADOS SÃO IGUAIS!')
elif (n1 > n2):
    print(f'\033[32mO MAIOR NÚMERO ENTRE {n1} E {n2} É {n1}')
elif (n2 > n1):
    print(f'O MAIOR NÚMERO ENTRE {n1} E {n2} É {n2}')
print('\033[36m=*'*28)


