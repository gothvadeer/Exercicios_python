from time import sleep
# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
# e dizer qual deles é o maior.


def maior(*valores):
    print('=-'*25)
    print('Analisando os valores passados...')
    maior_valor = 0
    for i in valores:
        print(f'=> {i}', end=' ', flush=True)
        sleep(1)
        if i > maior_valor:
            maior_valor = i
    if len(valores) > 0:
        print(f'Foram informados {len(valores)} valores ao todo')
        print(f'O maior valor é {maior_valor}')
    else:
        print(f'{valores} Não foram informados valores.')


maior(6, 8, 9, 10, 34, 78)
maior(2, 5, 8)
maior(1, 2)
maior(6)
maior()
