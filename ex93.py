#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

goals = []
jogador = dict()
jogador["Nome"] = str(input('Nome do jogador: ')).strip().capitalize()
jogador["Partidas"] = int(input('Partidas jogadas: '))
for g in range(jogador["Partidas"]):
    goals.append(int(input(f'Quantidade de gols na {g+1}ª partida: ')))
jogador["Goals"] = goals
jogador["Total"] = sum(goals)
print(jogador)
print('=*'*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=*'*40)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas:')
for pos, g in enumerate(goals):
    print(f'-> Na {pos+1}ª partida ele fez: {g} gols')
print(f'Ao total ele fez {jogador["Total"]} gols')