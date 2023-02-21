from time import sleep
#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
jogadores = {} #minha versão melhorada do código
for c in range(4):
    jogadores[c] = {}
    jogadores[c]["Nome"] = str(input(f'Nome do {c+1}º jogador: ')).strip().capitalize()
    jogadores[c]["Jogada"] = random.randint(1, 6)
print('-='*20)
for jogador in jogadores.values():
    print(f'{jogador["Nome"]} jogou: {jogador["Jogada"]}')
    sleep(1)
print("=*"*15)
print("RANKING".center(30))
print("=*"*15)
lista_jogadores = [{"Nome": jogadores[i]["Nome"], "Jogada": jogadores[i]["Jogada"]} for i in jogadores]
lista_jogadores.sort(key=lambda x: x["Jogada"], reverse=True)
for pos, jogador in enumerate(lista_jogadores):
    empate = [jogo["Nome"] for jogo in lista_jogadores if jogo["Jogada"] == jogador["Jogada"]]
    if len(empate) > 1:
        print(f'{pos+1}º lugar: empate {" e ".join(empate)} com {jogador["Jogada"]}')
    else:
        print(f'{pos+1}º lugar: {jogador["Nome"]} com {jogador["Jogada"]}')

