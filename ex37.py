from datetime import date

y = int(input('Digite o ano do seu nascimento: '))
data = date.today().year
idade = data - y
print('''\033[1mQUAL O SEU GÊNERO? 
DIGITE [ 1 ] PARA HOMEM
DIGITE [ 2 ] PARA MULHER ''')
s = int(input('\033[mDigite aqui uma das opções acima: '))
if s == 1:
        if idade == 18:
            print(f'\033[1;32mQuem nasceu em {y} tem {idade} anos em {data} \n'
          f'E está na idade CORRETA para se alistar! Não perca tempo, se aliste AGORA! ')
        elif idade > 18:
            print(f'\033[1;31mQuem nasceu em {y} tem {idade} anos em {data}\n'
          f'Você está {data - (y+18)} anos atrasado, sua data para o alistamento era em {y+18}.')
        elif idade < 18:
            print(f'\033[1;31mQuem nasceu em {y} tem {idade} anos em {data} \n'
          f'Você está {(y+18) - data} anos adiantado, sua data de alistamento será em {y+18}.')

if s == 2:
    print('\033[1;36mVocê não precisa de alistamento militar obrigatório.')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA')