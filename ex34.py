print('\033[36m=*'*15)
print('\033[1;32mSEU EMPRÉSTIMO SERÁ APROVADO?')
print('\033[36m=*'*15)
casa = float(input('\033[mDigite o valor da casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
anos = int(input('Digite em quantos anos pretende pagar: '))
vp = casa / (anos*12)
porcentagem = (salario*30) / 100

if vp >= porcentagem:
    print(f'\033[1;31mINFELIZMENTE SEU EMPRÉSTIMO FOI NEGADO!')
    print(f'\033[mPois as parcelas ficaram de R$ {vp:.2f} exercendo 30% ou mais do seu salário!  ')
else:
    print('\033[32mSeu empréstimo foi APROVADO!')
    print(f'\033[mAs parcelas do seu empréstimo ficam: R$ {vp:.2f}')



