
#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
pessoa = {}
ficha = [] #minha solução melhorada do programa
data = date.today().year
print('=-'*15)
print('CADASTRO PESSOAL'.center(30))
print('=-'*15)
while True:
    pessoa["Nome"] = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Ano de nascimento: '))
    pessoa["Idade"] = data - idade
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Gênero [M/F]: ')).strip().upper()[0]
        if genero not in 'MF':
            print('OPÇÃO INVÁLIDA')
    pessoa["Gênero"] = genero
    pessoa["CTPS"] = int(input('Carteira de trabalho:  '))
    if pessoa["CTPS"] != 0:
        pessoa["Contratação"] = int(input("Ano de contratação: "))
        pessoa["Aposentadoria"] = pessoa["Idade"] + (35 if pessoa["Gênero"] == "F" else 40) - (data - pessoa["Contratação"])
    ficha.append(pessoa.copy())
    pergunta = ' '
    while pergunta not in "SN":
        pergunta = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if pergunta not in "SN":
            print("OPÇÃO INVÁLIDA")
    if pergunta == "N":
        break
print("=*"*45)
print(f"NOME".rjust(10), "IDADE".rjust(10), "GÊNERO".rjust(10), "CTPS".rjust(10),
      "CONTRATO".rjust(20), "APOSENTADORIA".rjust(20))
print("=-"*45)
for pessoa in ficha:
    print(f'{pessoa["Nome"]:>10}{pessoa["Idade"]:>10}{pessoa["Gênero"]:>10}{pessoa["CTPS"]:>15}', end='')
    if "Contratação" and "Aposentadoria" in pessoa:
        if pessoa["CTPS"] != 0:
            print(f'{pessoa.get("Contratação", ""):>20}{pessoa.get("Aposentadoria", ""):>15}')
        else:
            print(f'{0:>20}{0:>15}')

