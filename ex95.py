# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
while True:
    goals = []
    nome = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input('Partidas jogadas: '))
    for g in range(partidas):
        goals.append(int(input(f'Quantidade de gols na {g + 1}ª partida: ')))
    jog = {"Nome": nome, "Partidas": partidas, "Goals": goals, "Total": sum(goals)}
    jogadores.append(jog.copy())
    while True:
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if pergunta in "SN":
            break
        print('OPÇÃO INVÁLIDA! Use apenas "S" ou "N"')
    print('=-'*30)
    if pergunta == "N":
        break
print(f"Nª".rjust(5), "NOME".rjust(15), "GOLS".rjust(15), "TOTAL".rjust(15))
print("=-"*30)
for c, jog in enumerate(jogadores):
    print(f'{c+1:>5}{jog["Nome"]:>17}{str(jog["Goals"]):>17}{jog["Total"]:>12}')
print("=-"*30)
while True:
    perg = int(input('Deseja ver os dados de qual jogador? [999 pra sair]: '))
    if perg == 999:
        print('=== FIM DO PROGRAMA ===')
        break
    if perg > len(jogadores):
        print('OPÇÃO INVÁLIDA! Tente um número válido')
    else:
        jogador = jogadores[perg - 1]
        print(f'=> LEVANTAMENTO DO JOGADOR {jogador["Nome"]}:')
        for pos, g in enumerate(jogador["Goals"]): # lembre-se sempre disso, coloque o for dentro do else.
            print(f'-> Na {pos+1}ª partida ele fez: {g} gols')
        print(f'Ao total ele fez {jogador["Total"]} gols')