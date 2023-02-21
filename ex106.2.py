from time import sleep
cores = ('\033[m', # 0 sem cor
'\033[1;30;41m', # 1 vermelho
'\033[1;30;45m', # 2 roxo
'\033[1;30;46m',# 3 ciano
'\33[1;30;47m', # 4 grey
 )

# exercicio resolvido pelo professor
def ajuda(comando):
    titulo(f"Acessando o manual do '{comando}'", 2)
    sleep(1)
    print(cores[4], end='')
    help(comando)
    print(cores[0])


def titulo(txt, cor=0):
    tamanho = len(txt) + 4
    print(cores[cor], end='')
    print(f'~'*tamanho)
    print(f'{txt:^{tamanho}}')
    print(f'~'*tamanho)
    print(cores[0], end='')


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Uma função ou biblioteca: ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('PROGRAMA ENCERRADO!', 1)