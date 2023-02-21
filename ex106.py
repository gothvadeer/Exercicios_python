#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
from time import sleep
import pydoc
# minha solução


def linha(txt, cor='\033[m'):
    tamanho = len(txt) + 8
    print(f'{cor}~'*tamanho)
    print(f'{cor}{txt: ^{tamanho}}')
    print(f'{cor}~'*tamanho,'\33[m')


def pyHelp():
    while True:
        linha('Sistema de ajuda PYHELP', '\033[1;45m')
        escolha = str(input('Escreva o nome da função ou biblioteca: ')).strip().lower()
        if escolha == "fim":
            linha('==== ATÉ LOGO ====', '\033[1;33;46m')
            break
        linha(f"Acessando o manual do comando '{escolha}'",'\033[1;43m')
        sleep(1)
        doc = pydoc.render_doc(escolha) #para imprimir os documentos
        print(f'\033[1;47m{doc}\033[m')

    return escolha


print(pyHelp())

