print('\033[36m=*'*18)
print('''\033[1;35mSOMATÓRIO DE NÚMEROS INTEIROS \nAPERTE [ 999 ] PARA O RESULTADO ''')
print('\033[36m=*'*18)
limite = count = soma = 0
flag = 999
while limite != flag:
    limite = int(input('\033[mDigite um número inteiro: '))
    count += 1
    soma += limite
print(f'Foram digitados {count-1} números, a soma entre eles é igual a: {soma-flag}')
