from random import choice

um = str(input('Escreva o nome do primeiro aluno: '))
dois = str(input('Escreva o nome do segundo aluno: '))
três = str(input('Escreva o nome do terceiro aluno: '))
quatro = str(input('Escreva o nome do quarto aluno: '))
l = [um, dois, três, quatro]
print(f'O aluno escolhido foi {choice(l)}')