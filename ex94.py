#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

lista_pessoas = [] # exercicio resolvido com list comprehension
while True:
    pessoa = dict()
    pessoa["Nome"] = str(input('Nome: ')).strip().title()
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Gênero [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('OPÇÃO INVÁLIDA! Digite "M" para masculino ou "F" para feminino')
    pessoa["Sexo"] = sexo
    pessoa["Idade"] = int(input('Idade: '))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta not in 'SN':
            print('OPÇÃO INVÁLIDA! Digite "S" para continuar ou "N" para interromper o programa')
    lista_pessoas.append(pessoa)
    if resposta == 'N':
        break
print("=*" * 20)
# idades
idades = [pessoa["Idade"] for pessoa in lista_pessoas]
# média
soma = sum(idades)
media = soma / len(lista_pessoas)
# mulheres
mulheres = [pessoa["Nome"] for pessoa in lista_pessoas if pessoa["Sexo"] == "F"]
# idade acima da média
acima_media = [pessoa["Nome"] for pessoa in lista_pessoas if pessoa["Idade"] > media]
print(f'=> Total de pessoas: {len(lista_pessoas)}')
print(f'=> Média de idade do grupo é: {media:.1f}')
print(f'=> As mulheres do grupo são: {mulheres}')
print(f'=> Pessoas que estão acima da média de idade: {acima_media}')
