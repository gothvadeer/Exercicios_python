alunos = []
while True:
    estudante = str(input('Nome: ')).strip().upper()
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([estudante, [nota1, nota2], media])
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if pergunta not in 'SN':
            print('OPÇÂO INVÁLIDA!')
    if pergunta == 'N':
        break
print(f'Nº'.ljust(5), 'NOME'.ljust(10), 'MÉDIA'.rjust(10))
print('=*'*20)
for i, aluno in enumerate(alunos):
    print(f'{i+1}'.ljust(5), f'{aluno[0]}'.ljust(10), f'{aluno[2]:.1f}'.rjust(10))
print('=*'*20)
while True:
    detalhe = int(input('Qual aluno deseja ver as notas? (999 para sair): '))
    if detalhe == 999:
        print('Fim do programa, volte sempre!')
        break
    if detalhe > len(alunos):
        print('OPÇÃO INVÁLIDA! Tente um número válido.')
    else:
        aluno = alunos[detalhe - 1]
        print(f'As notas de {aluno[0]} são: {aluno[1]}')
