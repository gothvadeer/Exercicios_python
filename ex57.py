n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
maior = 0
menor = 0

print('ESCOLHA UMA DAS OPÇÕES ABAIXO:')
print('''\033[1m[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
escolha = 0
while escolha != 5:
    escolha = int(input('\033[1;36mDIGITE UMA DAS OPÇÕES ACIMA: '))
    if escolha == 1:
        print(f'\033[mA soma de {n1} com o {n2} é {n1+n2}')
    if escolha == 2:
        print(f'\033[mO produto dos números {n1} e {n2} é {n1*n2}')
    if escolha == 3:
        maior = n1
        menor = n2
        if maior < n2:
            maior = n2
            menor = n1
        print(f'\033[mO maior número é {maior} e o menor número é {menor}')
    if escolha == 4:
        n1 = int(input('\033[mDigite um número: '))
        n2 = int(input('\33[mDigite outro número: '))
    if escolha > 5 or escolha == 0:
        print('\033[1;31mOPÇÃO INVÁLIDA')
print('\033[1;31mFIM DO PROGRAMA')