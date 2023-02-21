print('\033[36m=*' * 20)
print(f"\033[1;34m{'30 MELHORES FILMES DE TERROR': ^40}")
print(f"\033[1;34m{'DE TODOS OS TEMPOS': ^40}\033[m")
print('\033[36m=*\33[m' * 20)

filmes = ('O Gabinete do Dr. Caligari', 'Nosferatu', 'O Fantasma Da Ópera',
          'Frankenstein', 'Drácula', 'A Múmia',
          'Monstros', 'O Homem Invisível', 'A Noiva De Frankenstein', 'Sangue De Pantera',
          'O Vampiro Da Noite', 'Os Olhos Sem Rosto', 'Psicose', 'O Solar Maldito',
          'Repulsa Ao sexo', 'O Bebê De Rosemary', 'A Noite Dos Mortos-Vivos',
          'O Exorcista', 'As 7 Máscaras Da Morte', 'Inverno De Sangue Em Veneza',
          'O Homem De Palha', 'Prelúdio Para Matar', 'Carrie, A Estranha', 'A Profecia',
          'Suspiria', 'Halloween – A Noite Do Terror', 'Os Invasores De Corpos',
          'Alien, O Oitavo Passageiro', 'O Iluminado', 'Sexta-feira 13')

while True:
    escolha = 0
    print('\033[1mUSE UMA DAS OPÇÕES ABAIXO:\n'
          '[ 1 ] VER LISTA DE FILMES\n'
          '[ 2 ] VER OS 10 PRIMEIROS COLOCADOS\n'
          '[ 3 ] VER OS 10 ÚLTIMOS COLOCADOS\n'
          '[ 4 ] VER LISTA EM ORDEM ALFABÉTICA\n'
          '[ 5 ] SABER A POSIÇÃO DE UM FILME\n'
          '[ 6 ] FINALIZAR PROGRAMA\033[m')
    escolha = int(input('Digite sua opção: '))
    if escolha == 1:
        print('=*' * 20)
        for pos, f in enumerate(filmes):
            print(f'\033[1;33m{pos + 1}: {f}\033[m')
        print('=*' * 20)
    elif escolha == 2:
        print('=*' * 20)
        for pos, f in enumerate(filmes[0:10]):
            print(f'\033[1;33m{pos + 1}: {f}\033[m')
        print('=*' * 20)
    elif escolha == 3:
        print('=*' * 20)
        for pos, f in enumerate(filmes[-10:]):
            print(f'\033[1;33m{pos + 1}: {f}\033[m')
        print('=*' * 20)
    elif escolha == 4:
        print('=*' * 20)
        print(f'\n{sorted(filmes)}\n')
        print('=*' * 20)
    elif escolha == 5:
        q = str(input('Qual o nome do filme deseja saber a posição?: ')).strip().title()
        if q not in filmes:
            print('\033[1;31mNÃO EXISTE O FILME MENCIONADO, TENTE NOVAMENTE\033[m')
        else:
            pos = filmes.index(q) + 1
            print('=*' * 20)
            print(f'\033[1;33m{q} está na {pos}ª posição\033[m')
            print('=*' * 20)
    elif escolha == 6:
        print('\033[1;31mFim do programa\033[m')
        break
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE\033[m')
