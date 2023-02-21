print('\033[36m=*'*20)
print('''\033[1;35mTABUADA 2.1
DIGITE UM NÚMERO NEGATIVO PARA SAIR\033[m''')
print('\033[36m=*'*20)
c = 1
while True:
    n = int(input('\033[mDigite um número para ver sua tabuada: '))
    if n < 0:
        print('\033[1;31mFIM DO PROGRAMA')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')






