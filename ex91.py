#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
from time import sleep
jogadores = {}
for c in range(4):
    jogadores[f"Jogador{c+1}"] = random.randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
print('=*'*15)
print(f'RANKING'.center(30))
print('=*'*15)
for pos, i in enumerate(sorted(jogadores, key = jogadores.get, reverse= True)):
    print(f'{pos+1}º lugar {i} com {jogadores[i]}')
