num = int(input('Digite um número qualquer: '))
print('\033[36m=*'*15)
print('\033[1;32mDigite 1 para BINÁRIO')
print('Digite 2 para OCTAL')
print('Digite 3 para HEXADECIMAL')
print('Digite 4 para SAIR \033[m')
print('\033[36m=*'*15)
perg = int(input('\033[mDigite uma das opções acima: '))

if perg == 1:
    print(f'\033[1mO número {num} em BINÁRIO fica: {bin(num)[2:]}\033[m')
elif perg == 2:
       print(f'\033[1mO número {num} em OCTAL fica: {oct(num)[2:]}\033[m')
elif perg == 3:
    print(f'\033[1mO número {num} em HEXADECIMAL fica: {hex(num)[2:]}\033[m')
else:
    print(f'\033[31mOPÇÃO INVÁLIDA TENTE NOVAMENTE!')
