maioridade = homens = mulheres = 0
while True:
    print(f"\033[36m{'CADASTRE UMA PESSOA':=^40}\033[m")
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if idade >= 18:
         maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if escolha == 'N':
         break
if maioridade == 1:
    print('Existe uma pessoa maior de idade cadastrada')
if maioridade >= 2:
    print(f'Existem {maioridade} pessoas maiores de 18 cadastradas')
if maioridade == 0:
    print('Não existe pessoas maiores de idade cadastradas')
if homens == 1:
    print('Existe apenas um homem cadastrado')
if homens >= 2:
    print(f'Existem {homens} homens cadastrados.')
if homens == 0:
    print('Não há homens cadastrados')
if mulheres == 1:
    print('Existe apenas uma mulher com menos de 20 anos cadastrada')
if mulheres >= 2:
    print(f'Existem {mulheres} mulheres com menos de 20 anos cadastradas')
if mulheres == 0:
    print('Não há nenhuma mulher com menos de 20 anos cadastrada')