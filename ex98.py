from time import sleep
#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

def linha_fim():
    print('FIM!')
    print('-=' * 20)


def Contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} à {fim}  de {passo} em {passo}')
    if fim > inicio:
        passo = abs(passo)
        fim += 1
    elif fim < inicio:
        passo = -abs(passo)
        fim -= 1
    else:
        print(f'{inicio}')
        linha_fim()
        return
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(0.5)
    linha_fim()


Contador(1, 10, 1)
Contador(0, 10, 1)
print('Agora é a sua vez! Personalize a contagem: ')
while True:
    try:
        inicio = int(input('Inicio: '))
        fim = int(input('Fim: '))
        passo = abs(int(input('Passo: ')))
        Contador(inicio, fim, passo)
        break
    except ValueError:
        print('Por favor, digite apenas números inteiros!')