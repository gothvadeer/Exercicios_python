from datetime import date

print('\033[36m=*'*17)
print('\033[1;33mCONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('\033[36m=*'*17)
ano = int(input('\033[mO ano de nascimento do atleta: '))
date = date.today().year
idade = date - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos \n'
          f'Categoria: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos \n'
          f'Categoria: INFANTIL')
elif idade <=19:
    print(f'O atleta tem {idade} anos \n'
          f'Categoria: JÚNIOR')
elif idade <=25:
    print(f'O atleta tem {idade} anos\n'
          f'Categoria: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos \n'
          f'Categoria: MASTER')

