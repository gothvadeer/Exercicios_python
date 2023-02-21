#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador, gols=0):
    if jogador is None or jogador == 0:
        jogador = '<desconhecido>'
    return f'O jogador {jogador} fez {gols} gol(s)'


# programa principal
while True:
    jogador = str(input('Nome do jogador: ')).strip().capitalize() or None
    try:
        gols = int(input('Nº de gols: ') or 0)
        print(ficha(jogador, gols))
        break
    except ValueError:
        print('Por favor, digite um número inteiro')

