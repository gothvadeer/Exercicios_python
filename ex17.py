from random import shuffle

a = str(input('Escreva o nome do primeiro aluno: '))
b = str(input('Escreva o nome do segundo aluno: '))
c = str(input('Escreva o nome do terceiro aluno: '))
d = str(input('Escreva o nome do quarto aluno: '))
lista = [a, b, c, d]
shuffle(lista)
print(f'A ordem escolhida será: \n'
      f'{lista}')

