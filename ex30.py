from datetime import date

y = int(input('Digite um ano e para analisar o ano atual, digite 0: '))
if y == 0:
    y = date.today().year
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(f'\033[32mO ano {y} é um ano bissexto!')
else:
    print(f'O ano {y} \033[1;31mNÃO\033[m é um ano bissexto!')
