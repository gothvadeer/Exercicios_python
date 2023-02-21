alunos = {}
estudantes = [] #versão melhorada
while True:
    alunos["nome"] = str(input('Nome: ')).strip().capitalize()
    notas = []
    notas.append(float(input(f'1ª nota de {alunos["nome"]}: ')))
    notas.append(float(input(f'2ª nota de {alunos["nome"]}: ')))
    alunos["notas"] = notas
    alunos["média"] = (alunos["notas"][0] + alunos["notas"][1]) / 2
    alunos["situação"] = 'Aprovado' if alunos["média"] >= 7 else 'Reprovado'
    estudantes.append(alunos.copy())
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if pergunta not in 'SN':
            print('OPÇÃO INVÁLIDA')
    if pergunta == 'N':
        break
print(f'NOME'.ljust(10), 'MÉDIA'.rjust(10), 'SITUAÇÃO'.rjust(15))
print('=*'*30)
for pos, aluno in enumerate(estudantes):
    print(f'{aluno["nome"]:<10}{aluno["média"]:>10.1f}{aluno["situação"]:>17}')
print('=*'*30)
