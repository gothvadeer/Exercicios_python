n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int (input('Escreva um último número: '))
print("=*"*20)
#calculando o maior valor
maior = n1
if (n2 > maior):
    maior = n2
    if (n3 > maior):
        maior = n3
print(f'\033[1mMAIOR: {maior}')
#calculando o menor valor
menor = n1
if (n2 < menor):
    menor = n2
    if (n3 < menor):
        menor = n3
print(f'\033[1mMENOR: {menor}')
print("=*"*20)