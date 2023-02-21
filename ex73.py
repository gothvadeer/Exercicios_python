print('=*' * 20)
print(f"\033[1;34m{'TABELA DO BRASILEIRÃO': ^40}\033[m")
print('=*' * 20)

tabela = ('Palmeiras', 'Inter', 'Fluminence', 'Corinthians', 'Flamengo', 'Athletico-PR',
          'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos',
          'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO',
          'Avaí', 'Juventude')
print(f'\033[1;34mOs 5 primeiros colocados:\n\033[m{tabela[0:5]}')
print('-*' * 35)
print(f'\033[1;34mOs 4 últimos colocados:\n\033[m{tabela[-4:]}')
print('-*' * 35)
print(f'\033[1;34mTimes em ordem alfabética: \n\033[m{sorted(tabela)}')
print('-*' * 35)
print(f'\033[1;34mQual posição está o Avaí?\n\033[m{tabela.index("Avaí")+1}º')
