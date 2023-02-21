#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
lista_pessoas = []
soma = 0
while True:
    pessoa = dict()
    pessoa["Nome"] = str(input('Nome: ')).strip().capitalize()
    sexo = ' '
    while True: # faça a validação dessa forma, ocupa menos linha
        pessoa["Gênero"] = str(input('Gênero [M/F]: ')).strip().upper()[0]
        if pessoa["Gênero"] in 'MF':
            break
        print("OPÇÂO INVÁLIDA! Use apenas 'M' ou 'F'")
    pessoa["Idade"] = int(input('Idade: '))
    soma += pessoa["Idade"]
    while True:
        pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if pergunta in "SN":
            break
        print("OPÇÃO INVÁLIDA! Use apenas 'S' ou 'N'")
    lista_pessoas.append(pessoa)
    if pergunta == "N":
        break
print("=*"*20)
media = soma / len(lista_pessoas) # a média
mulheres = " e ".join([pessoa["Nome"] for pessoa in lista_pessoas if pessoa["Gênero"] == "F"]) #use sempre isso
print(f'= > O total de pessoas cadatras: {len(lista_pessoas)}')
print(f'= > A média de idade do grupo: {media:.2f}')
print(f'= > As mulheres cadastradas são: {mulheres}')
print(f'= > Lista de pessoas com idade acima da média: ')
for p in lista_pessoas: # as pessoas acima da média de idade
    if p["Idade"] > media:
        print('     ', end=' ')
        for k, v in p.items():
            print(f' {k} => {v}', end='')