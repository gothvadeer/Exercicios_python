#Exercício Python 100: Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from time import sleep
import random
lista_parametros = []


def lista():
    print('Sorteando...')
    lista_parametros.append(random.sample(range(1, 11), 5))
    print(*lista_parametros[-1], sep=' => ', end=' ', flush=True)
    sleep(1)


def somar_pares():
    ultima_lista = lista_parametros[-1]
    soma = sum(filter(lambda x: x % 2 == 0, ultima_lista))
    print(f'\nA soma dos valores pares é {soma}')


lista()
somar_pares()

