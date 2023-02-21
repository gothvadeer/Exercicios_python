
estudantes = {}
estudantes["nome"] = str(input('Nome do aluno: ')).strip().capitalize()
estudantes["média"] = float(input(f'Média de {estudantes["nome"]}: '))
print(f'O nome é {estudantes["nome"]}')
print(f'A média é {estudantes["média"]}')
if estudantes["média"] < 7:
    print(f'A situação é REPROVADO(A)!')
else:
    print(f'A situação é APROVADO(A)!')
