from time import sleep
alunos = []
media = 0
while True:
    a = str(input('Nome: ')).strip().upper()
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    q = ' '
    alunos.append([a, [nota1, nota2], media])
    while q not in 'SN':
        q = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if q == 'N':
        break
print(f'Nº'.ljust(5), 'NOME'.rjust(10), 'MÉDIA'.rjust(10))
print("-*"*20)
for pos, aluno in enumerate(alunos):
    print(f'{pos+1}{aluno[0]:>15}', f'{aluno[2]:.1f}'.rjust(9))
print("-*"*20)
while True:
    pergunta = int(input('\033[1mVocê quer ver os dados de qual aluno? (999 encerra o programa): \033[m'))
    for pos, aluno in enumerate(alunos):
        if pos + 1 == pergunta:
            print(f'\033[1;32mAs notas de {aluno[0]} são: {aluno[1]}\033[m')
    if pergunta == 999:
        print('\033[1;31mFINALIZANDO...\033[m')
        sleep(1)
        print('\033[1mPrograma finalizado! Tenha um bom dia!\033[m')
        break